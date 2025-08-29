from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import TravelOption, Booking, UserProfile
from django.db import transaction
from django.contrib import messages
import uuid

# Home view: Enforces mandatory registration and login
def home(request):
    """
    Checks if the user is authenticated. If not, redirects them to the registration page.
    This ensures that registration is the mandatory first step.
    """
    if not request.user.is_authenticated:
        return redirect('register')
    return render(request, 'home.html')

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically create a UserProfile for the new user
            UserProfile.objects.create(user=user)
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    recent_bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')[:3]

    if request.method == 'POST':
        user_profile.phone_number = request.POST.get('phone_number')
        user_profile.address = request.POST.get('address')
        user_profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    context = {
        'user_profile': user_profile,
        'recent_bookings': recent_bookings
    }
    return render(request, 'profile.html', context)

@login_required
def travel_options(request):
    options = TravelOption.objects.all()
    # Basic search and filtering
    if request.GET.get('type'):
        options = options.filter(travel_type__icontains=request.GET.get('type'))
    if request.GET.get('source'):
        options = options.filter(source__icontains=request.GET.get('source'))
    if request.GET.get('destination'):
        options = options.filter(destination__icontains=request.GET.get('destination'))

    context = {'travel_options': options}
    return render(request, 'travel_options.html', context)

@login_required
def book_travel(request, travel_id):
    travel_option = get_object_or_404(TravelOption, id=travel_id)
    if request.method == 'POST':
        number_of_seats = int(request.POST.get('seats'))
        if number_of_seats <= 0:
            messages.error(request, 'Please enter a valid number of seats.')
            return redirect('book_travel', travel_id=travel_id)
            
        if number_of_seats > travel_option.available_seats:
            messages.error(request, 'Not enough seats available.')
            return redirect('book_travel', travel_id=travel_id)
        
        with transaction.atomic():
            travel_option.available_seats -= number_of_seats
            travel_option.save()
            
            total_price = travel_option.price * number_of_seats
            booking_id = 'BK-' + str(uuid.uuid4())[:8].upper()
            
            Booking.objects.create(
                booking_id=booking_id,
                user=request.user,
                travel_option=travel_option,
                number_of_seats=number_of_seats,
                total_price=total_price,
                status='Confirmed'
            )
            messages.success(request, 'Booking confirmed successfully!')
            return redirect('my_bookings')
    
    return render(request, 'book_travel.html', {'travel_option': travel_option})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    context = {'bookings': bookings}
    return render(request, 'my_bookings.html', context)

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status == 'Confirmed':
        with transaction.atomic():
            booking.travel_option.available_seats += booking.number_of_seats
            booking.travel_option.save()
            booking.status = 'Cancelled'
            booking.save()
            messages.success(request, 'Booking cancelled successfully.')
    else:
        messages.error(request, 'This booking cannot be cancelled.')
    return redirect('my_bookings')