from django.db import migrations
from django.utils import timezone

def create_initial_travel_options(apps, schema_editor):
    TravelOption = apps.get_model('booking_app', 'TravelOption')
    from datetime import datetime

    travel_options_data = [
        # Flights
        {'travel_id': 'F101', 'travel_type': 'Flight', 'source': 'New York', 'destination': 'London', 'date_time': datetime(2025, 10, 20, 9, 30), 'price': 850.00, 'available_seats': 150},
        {'travel_id': 'F102', 'travel_type': 'Flight', 'source': 'London', 'destination': 'Paris', 'date_time': datetime(2025, 10, 21, 14, 0), 'price': 120.00, 'available_seats': 80},
        {'travel_id': 'F103', 'travel_type': 'Flight', 'source': 'Tokyo', 'destination': 'New York', 'date_time': datetime(2025, 10, 22, 18, 45), 'price': 1200.00, 'available_seats': 200},

        # Trains
        {'travel_id': 'T201', 'travel_type': 'Train', 'source': 'Paris', 'destination': 'Berlin', 'date_time': datetime(2025, 10, 25, 7, 15), 'price': 95.50, 'available_seats': 100},
        {'travel_id': 'T202', 'travel_type': 'Train', 'source': 'Berlin', 'destination': 'Rome', 'date_time': datetime(2025, 10, 26, 11, 20), 'price': 150.00, 'available_seats': 75},
        {'travel_id': 'T203', 'travel_type': 'Train', 'source': 'Rome', 'destination': 'Madrid', 'date_time': datetime(2025, 10, 27, 20, 0), 'price': 110.00, 'available_seats': 60},

        # Buses
        {'travel_id': 'B301', 'travel_type': 'Bus', 'source': 'London', 'destination': 'Manchester', 'date_time': datetime(2025, 10, 28, 10, 0), 'price': 30.00, 'available_seats': 50},
        {'travel_id': 'B302', 'travel_type': 'Bus', 'source': 'Manchester', 'destination': 'Edinburgh', 'date_time': datetime(2025, 10, 29, 12, 30), 'price': 45.00, 'available_seats': 40},

        # Domestic Flights (India)
        {'travel_id': 'F-DEL-BOM', 'travel_type': 'Flight', 'source': 'Delhi', 'destination': 'Maharashtra', 'date_time': datetime(2025, 11, 15, 10, 0), 'price': 5500.00, 'available_seats': 180},
        {'travel_id': 'F-MAA-BLR', 'travel_type': 'Flight', 'source': 'Tamil Nadu', 'destination': 'Karnataka', 'date_time': datetime(2025, 11, 16, 15, 30), 'price': 3200.00, 'available_seats': 120},
        {'travel_id': 'F-KOL-HYD', 'travel_type': 'Flight', 'source': 'West Bengal', 'destination': 'Telangana', 'date_time': datetime(2025, 11, 17, 18, 0), 'price': 4800.00, 'available_seats': 150},
        {'travel_id': 'F-JAI-CCU', 'travel_type': 'Flight', 'source': 'Rajasthan', 'destination': 'West Bengal', 'date_time': datetime(2025, 11, 18, 12, 45), 'price': 6100.00, 'available_seats': 165},

        # Domestic Trains (India)
        {'travel_id': 'T-NDLS-LKO', 'travel_type': 'Train', 'source': 'Delhi', 'destination': 'Uttar Pradesh', 'date_time': datetime(2025, 11, 20, 7, 0), 'price': 850.00, 'available_seats': 300},
        {'travel_id': 'T-PAT-RNC', 'travel_type': 'Train', 'source': 'Bihar', 'destination': 'Jharkhand', 'date_time': datetime(2025, 11, 21, 9, 30), 'price': 650.00, 'available_seats': 250},
        {'travel_id': 'T-BBS-PUN', 'travel_type': 'Train', 'source': 'Odisha', 'destination': 'Punjab', 'date_time': datetime(2025, 11, 22, 14, 10), 'price': 1500.00, 'available_seats': 200},
        {'travel_id': 'T-GHY-AGL', 'travel_type': 'Train', 'source': 'Assam', 'destination': 'Tripura', 'date_time': datetime(2025, 11, 23, 19, 20), 'price': 780.00, 'available_seats': 180},

        # Domestic Buses (India)
        {'travel_id': 'B-CHD-KAS', 'travel_type': 'Bus', 'source': 'Chandigarh', 'destination': 'Himachal Pradesh', 'date_time': datetime(2025, 11, 25, 6, 0), 'price': 450.00, 'available_seats': 45},
        {'travel_id': 'B-GOA-PUNE', 'travel_type': 'Bus', 'source': 'Goa', 'destination': 'Maharashtra', 'date_time': datetime(2025, 11, 26, 8, 30), 'price': 650.00, 'available_seats': 55},
        {'travel_id': 'B-TVM-MDU', 'travel_type': 'Bus', 'source': 'Kerala', 'destination': 'Tamil Nadu', 'date_time': datetime(2025, 11, 27, 22, 0), 'price': 580.00, 'available_seats': 50},
        {'travel_id': 'B-DEL-JNK', 'travel_type': 'Bus', 'source': 'Delhi', 'destination': 'Jammu and Kashmir', 'date_time': datetime(2025, 11, 28, 11, 0), 'price': 1800.00, 'available_seats': 40},
    ]

    for data in travel_options_data:
        TravelOption.objects.create(**data)

class Migration(migrations.Migration):

    dependencies = [
        # Replace '0001_initial' with the actual last migration name if different
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_travel_options),
    ]
