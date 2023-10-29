import functions as fun
import random as rand
import numpy as np
from models.interfaces.CsvData import CsvData
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
class Ride(CsvData):
    def __init__(self, id, users, mistakes, cars, locations):
        fake = Faker()
        self.id = id
        self.ride_config()
        
        self.user_PESEL = ''
        
        self.vehicle_registration_number, self.start_place, self.end_place = self.take_car(cars, locations)
        
        self.start_date = fake.date_between_dates(USER_LICENCE, TODAY_DATE) # tu powinno byc user.licence_date, ale sie pierdoli
        self.end_date = fake.date_between_dates(self.start_date, fun.add_years(self.start_date, self.max_days_rent)) ### funkcja add days do zrobienia
        self.time_start = fake.time()
        self.time_end = fake.time() # do poprawy bo mozna oddac godzine wczesniej
        
        self.distance = round(rand.uniform(self.min_distance, self.max_distance), self.rating_rounding)
        self.technic_ride_rating, self.observance_of_road_regulations_rating = self.calculate_rating(mistakes)
        self.ride_rating = round(np.mean([self.observance_of_road_regulations_rating, self.technic_ride_rating]), self.rating_rounding)
        self.price_multiplier = round(self.multiplier_zero_digit/self.ride_rating, self.rating_rounding)
        self.ride_price = round((self.start_price + self.distance*self.price_per_kilometer)*self.price_multiplier, self.rating_rounding)
    
    def ride_config(self, max_days_rent=3, min_distance=1, max_distance=10, 
                 multiplier_zero_digit=7, min_rating=1, max_rating=10, 
                 rating_rounding=2, start_price=5, price_per_kilometer=5):
        self.max_days_rent = max_days_rent
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.multiplier_zero_digit = multiplier_zero_digit
        self.min_rating = min_rating
        self.max_rating = max_rating
        self.rating_rounding = rating_rounding
        self.start_price = start_price
        self.price_per_kilometer = price_per_kilometer
    
    def take_car(self, cars, locations):
        return "WEJHEROWO", 1, 1
    
    # Trzeba zoptymalizowac, bo bedzie sie robic w chuj
    def calculate_rating(self, mistakes):
        technic_ride_rating = self.max_rating
        observance_of_road_regulations_rating = self.max_rating
        for mistake in mistakes:
            if mistake.ride_id == self.id:
                if mistake.mistake_nature == "T":
                    technic_ride_rating -= 1
                else:
                    observance_of_road_regulations_rating -= 1
        if observance_of_road_regulations_rating < 1:
            observance_of_road_regulations_rating = 1
        if technic_ride_rating < 1:
            technic_ride_rating = 1
        return technic_ride_rating, observance_of_road_regulations_rating
        
    
    def get_csv_data(self):
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