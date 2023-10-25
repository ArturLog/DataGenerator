import datetime as date
import functions as fun
import random as rand
import numpy as np
from faker import Faker

# Id, PESEL_użytkownika, Nr_rejestracyjny_pojazdu,
# Data_rozpoczecia, Data_zakonczenia,
# Godzina_rozpoczecia, Godzina_zakonczenia,
# Miejsce_rozpoczęcia, Miejsce_zakonczenia,
# Dystans, Ocena_przejazdu, Ocena_techniki_jazdy
# Ocena_przestrzegania_przepisow_drogowych
# Mnoznik_ceny, Koszt_przejazdu
class Raid:
    def __init__(self, id, user, max_days_rent=3, min_distance=1, max_distance=10):
        fake = Faker()
        self.id = id
        self.user_PESEL = user.PESEL
        self.vehicle_registration_number = "WEJHEROWO" #
        self.start_date = fake.date_between_dates(user.licence_date, date.today())     
        self.end_date = fake.date_between_dates(self.start_date, fun.add_years(self.start_date, max_days_rent))
        self.time_start = fake.time()
        self.time_end = fake.time() # do poprawy
        self.start_place = "BLE" #
        self.end_place = "ble" #
        self.distance = round(rand.uniform(min_distance, max_distance), 2)
        self.technic_ride_rating = round(rand.uniform(1, 10), 2)
        self.observance_of_road_regulations_rating = round(rand.uniform(1, 10), 2) #
        self.ride_rating = round(np.mean(self.observance_of_road_regulations_rating + self.technic_ride_rating), 2)
        self.price_multiplier =
        self.ride_price = 
        
    def getCsvData(self):
        return [
            self.id,
            self.user_PESEL,
            self.vehicle_registration_number,
            self.start_date,
            self.end_date,
            self.time_start,
            self.time_end,
            self.start_place,
            self.end_place,
            self.distance,
            self.ride_rating,
            self.technic_ride_rating,
            self.observance_of_road_regulations_rating,
            self.price_multiplier,
            self.ride_price
        ]