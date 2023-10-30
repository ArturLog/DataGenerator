import functions as fun
import random as rand
import numpy as np
import random
from models.interfaces.CsvData import CsvData
from datetime import timedelta

# Id, PESEL_użytkownika, Nr_rejestracyjny_pojazdu,
# Data_rozpoczecia, Data_zakonczenia,
# Godzina_rozpoczecia, Godzina_zakonczenia,
# Miejsce_rozpoczęcia, Miejsce_zakonczenia,
# Dystans, Ocena_przejazdu, Ocena_techniki_jazdy
# Ocena_przestrzegania_przepisow_drogowych
# Mnoznik_ceny, Koszt_przejazdu
class Ride(CsvData):
    def __init__(self, id, t0, t2, users, mistakes, cars, locations):
        self.id = id
        self.t0 = t0
        self.t2 = t2
        self.ride_config()
        
        self.datetime_start = fun.generate_random_datetime(t0, t2)
        self.datetime_end = fun.generate_random_datetime(self.datetime_start, self.datetime_start 
                                                         + timedelta(minutes=(random.randint(5, self.max_days_rent*24*60))))
        self.user = self.find_free_user(users)
        
        self.start_place = random.randint(1, len(locations))
        self.end_place = random.randint(1, len(locations))       
        self.car = self.take_car(cars)
        self.vehicle_registration_number = self.car.registration
        
        self.distance = round(rand.uniform(self.min_distance, self.max_distance), self.rating_rounding)
        self.technic_ride_rating, self.observance_of_road_regulations_rating = self.calculate_rating(mistakes)
        self.ride_rating = round(np.mean([self.observance_of_road_regulations_rating, self.technic_ride_rating]), self.rating_rounding)
        self.price_multiplier = round(self.multiplier_zero_digit/self.ride_rating, self.rating_rounding)
        self.ride_price = round((self.start_price + self.distance*self.price_per_kilometer)*self.price_multiplier, self.rating_rounding)
    
    def ride_config(self, max_days_rent=1, min_distance=1, max_distance=10, 
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
        
    def find_free_user(self, users):
        for user in users:
            #user = random.choice(users)
            if user.alive and user.last_rental < self.datetime_start:
                user.last_rental = self.datetime_start
                return user
            
    
    def take_car(self, cars):
        for car in cars:
            #car = random.choice(cars)
            if car.last_rental < self.datetime_start:
                self.start_place = car.location
                car.last_rental = self.datetime_end
                car.location = self.end_place
                return car
    
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
            self.user.PESEL,
            self.vehicle_registration_number,
            self.datetime_start.date(),
            self.datetime_end.date(),
            self.datetime_start.time(),
            self.datetime_end.time(),
            self.start_place,
            self.end_place,
            self.distance,
            self.ride_rating,
            self.technic_ride_rating,
            self.observance_of_road_regulations_rating,
            self.price_multiplier,
            self.ride_price
        ]