import functions as fun
import random as rand
import numpy as np
from datetime import date
from faker import Faker


TODAY_DATE = date(2003, 1, 1)
USER_LICENCE = date(2001, 1, 1)
# Id, PESEL_użytkownika, Nr_rejestracyjny_pojazdu,
# Data_rozpoczecia, Data_zakonczenia,
# Godzina_rozpoczecia, Godzina_zakonczenia,
# Miejsce_rozpoczęcia, Miejsce_zakonczenia,
# Dystans, Ocena_przejazdu, Ocena_techniki_jazdy
# Ocena_przestrzegania_przepisow_drogowych
# Mnoznik_ceny, Koszt_przejazdu
class Ride:
    def __init__(self, id, user, max_days_rent=3, min_distance=1, max_distance=10, 
                 multiplier_zero_digit=7, min_rating=1, max_rating=10, rating_rounding=2,
                 start_price=5, price_per_kilometer=5
                 ):
        fake = Faker()
        self.id = id
        self.user_PESEL = user.PESEL
        self.vehicle_registration_number = "WEJHEROWO" # no trzeba cos wymyslic ciekawego
        self.start_date = fake.date_between_dates(USER_LICENCE, TODAY_DATE) # tu powinno byc user.licence_date, ale sie pierdoli
        self.end_date = fake.date_between_dates(self.start_date, fun.add_years(self.start_date, max_days_rent)) ### funkcja add days do zrobienia
        self.time_start = fake.time()
        self.time_end = fake.time() # do poprawy bo mozna oddac godzine wczesniej
        self.start_place = "BLE" # oznaka miejsca ?
        self.end_place = "ble" # ?
        self.distance = round(rand.uniform(min_distance, max_distance), rating_rounding)
        self.technic_ride_rating = round(rand.uniform(min_rating, max_rating), rating_rounding)
        self.observance_of_road_regulations_rating = round(rand.uniform(min_rating, max_rating), rating_rounding) # od ilosci bledow ?
        self.ride_rating = round(np.mean(self.observance_of_road_regulations_rating + self.technic_ride_rating), rating_rounding)
        self.price_multiplier = round(self.ride_rating/multiplier_zero_digit, rating_rounding)
        self.ride_price = (start_price + self.distance*price_per_kilometer)*self.price_multiplier        
    
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