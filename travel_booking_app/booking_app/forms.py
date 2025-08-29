from django import forms
from .models import TravelOption, Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_seats']

    def clean_number_of_seats(self):
        seats = self.cleaned_data.get('number_of_seats')
        if seats <= 0:
            raise forms.ValidationError("Number of seats must be a positive integer.")
        return seats