from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta
from .models import TravelOption, Booking, UserProfile

class TravelBookingTestCase(TestCase):
    def setUp(self):
        """
        Set up the necessary objects for testing.
        """
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a UserProfile for the test user
        UserProfile.objects.create(user=self.user)

        # Create a sample TravelOption
        self.flight = TravelOption.objects.create(
            travel_id='F123',
            travel_type='Flight',
            source='New York',
            destination='London',
            date_time=datetime.now() + timedelta(days=7),
            price=500.00,
            available_seats=150
        )
        self.train = TravelOption.objects.create(
            travel_id='T456',
            travel_type='Train',
            source='Paris',
            destination='Berlin',
            date_time=datetime.now() + timedelta(days=14),
            price=120.00,
            available_seats=50
        )

    def test_travel_option_creation(self):
        """
        Test that TravelOption model instances are created correctly.
        """
        self.assertEqual(self.flight.travel_id, 'F123')
        self.assertEqual(self.flight.travel_type, 'Flight')
        self.assertEqual(self.flight.available_seats, 150)

    def test_user_profile_creation(self):
        """
        Test that a UserProfile is created when a new user is created.
        """
        self.assertIsInstance(self.user.userprofile, UserProfile)
        self.assertEqual(self.user.userprofile.user, self.user)

    def test_booking_creation_and_seat_deduction(self):
        """
        Test that a booking is created and the available seats are correctly
        deducted from the TravelOption.
        """
        self.client.login(username='testuser', password='testpassword')
        initial_seats = self.flight.available_seats
        seats_to_book = 2

        response = self.client.post(
            reverse('book_travel', args=[self.flight.id]),
            {'seats': seats_to_book},
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Booking confirmed successfully!')

        # Refresh the instance from the database
        self.flight.refresh_from_db()

        # Check that the number of available seats has decreased
        self.assertEqual(self.flight.available_seats, initial_seats - seats_to_book)

        # Check that a booking was created for the user
        booking = Booking.objects.get(user=self.user)
        self.assertEqual(booking.number_of_seats, seats_to_book)
        self.assertEqual(booking.travel_option, self.flight)
        self.assertEqual(booking.status, 'Confirmed')
        self.assertEqual(booking.total_price, self.flight.price * seats_to_book)

    def test_booking_cancellation_and_seat_refund(self):
        """
        Test that canceling a booking refunds the seats and updates the status.
        """
        self.client.login(username='testuser', password='testpassword')
        
        # First, create a booking
        seats_to_book = 3
        self.client.post(
            reverse('book_travel', args=[self.train.id]),
            {'seats': seats_to_book}
        )
        booking = Booking.objects.get(user=self.user)
        initial_seats = self.train.available_seats - seats_to_book
        
        # Now, cancel the booking
        response = self.client.get(
            reverse('cancel_booking', args=[booking.id]),
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Booking cancelled successfully.')

        # Refresh instances from the database
        booking.refresh_from_db()
        self.train.refresh_from_db()

        # Check that the status is now 'Cancelled'
        self.assertEqual(booking.status, 'Cancelled')

        # Check that the available seats have been refunded
        self.assertEqual(self.train.available_seats, initial_seats + seats_to_book)

    def test_booking_with_insufficient_seats(self):
        """
        Test that booking fails when there are not enough seats.
        """
        self.client.login(username='testuser', password='testpassword')
        seats_to_book = self.flight.available_seats + 1

        response = self.client.post(
            reverse('book_travel', args=[self.flight.id]),
            {'seats': seats_to_book},
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Not enough seats available.')
        
        # Ensure no booking was created
        self.assertEqual(Booking.objects.count(), 0)