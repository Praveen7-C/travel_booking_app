from django.contrib import admin
from .models import TravelOption, Booking, UserProfile

admin.site.register(TravelOption)
admin.site.register(Booking)
admin.site.register(UserProfile)