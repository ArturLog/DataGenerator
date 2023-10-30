import os
import pandas as pd
import random
import functions as fun
from datetime import datetime
from models.classes.User import User
from models.classes.Ride import Ride
from models.classes.Car import Car
from models.classes.Mistake import Mistake
from models.classes.Location import Location

class Generator:
    def __init__(self):
        self.users_amount = 0
        self.rides_amount = 0
        self.mistakes_amount = 0
        self.cars_amount = 0
        self.locations_amount = 0 
        self.users = []
        self.rides = []
        self.mistakes = []
        self.cars = []
        self.locations = []
        # Cars
        self.unique_cars = set()
        self.car_registrations = []
        self.car_vins = []
        # Users
        self.unique_users = set()
        self.user_pesels = []
        # Locations
        self.unique_locations = set()
        # Mistakes
        self.unique_mistakes = set()

    
    def config(self, start_date, end_date, users_amount=100, rides_amount=100, mistakes_amount=100, cars_amount=100, locations_amount=100):
        self.start_date = start_date
        self.end_date = end_date
        self.users_amount += users_amount
        self.rides_amount += rides_amount
        self.mistakes_amount += mistakes_amount
        self.cars_amount += cars_amount
        self.locations_amount += locations_amount    
        
    def generate_all(self, modify=False):
        self.generate_locations(modify=modify)
        self.generate_cars(modify=modify)
        self.generate_users(modify=modify)
        self.generate_mistakes(modify=modify)
        self.generate_rides(modify=modify)
        
    def generate_users(self, modify=False):
        if modify:
            for i in range(len(self.users)):
                if random.random() < 0.04:
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] Modyfing user {i + 1}...")
                    if self.users[i].sex == 'Kobieta':
                        self.users[i].sex = 'Mezczyzna'
                    else:
                        self.users[i].sex = 'Kobieta'
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Generating users...")
        current_index = len(self.users) + 1
        while len(self.unique_users) < self.users_amount:
            new_user = User(current_index)
            if new_user.PESEL not in self.user_pesels:
                self.unique_users.add(tuple(new_user.get_csv_data()))
                self.user_pesels.append(new_user.PESEL)
                if len(self.unique_users) == current_index:
                    current_index = current_index + 1
                    self.users.append(new_user)
        # for i in range(self.users_amount):
        #     self.users.append(User(i))
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Users generated")

    def generate_cars(self, modify=False):
        if modify:
            for i in range(len(self.cars)):
                if random.uniform(0, 1) < 0.04:
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] Modyfing car {i + 1}...")
                    self.cars[i].last_inspection = fun.generate_random_date(self.cars[i].last_inspection, self.end_date)
                    
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Generating cars...")
        while len(self.unique_cars) < self.cars_amount:
            new_car = Car(t0=self.start_date, t2=self.end_date, locations_amount=self.locations_amount)
            if new_car.registration not in self.car_registrations and new_car.vin not in self.car_vins:
                self.unique_cars.add(tuple(new_car.get_csv_data()))
                self.car_registrations.append(new_car.registration)
                self.car_vins.append(new_car.vin)
                self.cars.append(new_car)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Cars generated!")

    def generate_locations(self, modify=False):
        if modify:
            for i in range(len(self.locations)):
                if random.uniform(0, 1) < 0.001:
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] Modyfing location {i + 1}...")
                    self.locations[i].street = random.choice(['Wajdeloty', 'Politechniczna', 'Uniwersytecka'])
                    
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Generating locations...")
        current_index = len(self.locations) + 1
        while len(self.unique_locations) < self.locations_amount:
            new_location = Location(current_index)
            self.unique_locations.add(tuple(new_location.get_csv_data())[1:])
            if len(self.unique_locations) == current_index:
                current_index = current_index + 1
                self.locations.append(new_location)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Locations generated!")
    
    def generate_rides(self, modify=False):
        if modify:
            for i in range(len(self.rides)):
                if random.uniform(0, 1) < 0.005:
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] Modyfing ride {i + 1}...")
                    self.rides[i].ride_price = round(self.rides[i].ride_price - (random.random() * self.rides[i].ride_price), 2)

        print(f"[{datetime.now().strftime('%H:%M:%S')}] Generating rides...")
        for i in range(len(self.rides) + 1, self.rides_amount+1):
            self.rides.append(Ride(id=i, t0=self.start_date, t2=self.end_date, users=self.users, mistakes=self.mistakes, 
                                   cars=self.cars, locations=self.locations))
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Rides generated!")
            
    def generate_mistakes(self, modify=False):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Generating mistakes...")
        current_index = len(self.mistakes) + 1
        while len(self.mistakes) < self.mistakes_amount:
            new_mistake = Mistake(current_index, self.start_date, self.end_date, self.rides_amount, self.locations_amount)
            self.unique_mistakes.add(tuple(new_mistake.get_csv_data()[1:]))
            if len(self.unique_mistakes) == current_index:
                current_index = current_index + 1
                self.mistakes.append(new_mistake)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Mistakes generated!")

    def generate_csv_data(self, generatedData):
        data = []
        for d in generatedData:
            data.append(d.get_csv_data())
        return data
        
    def create_all_csv(self, suffix):
        self.create_csv(
            data=self.generate_csv_data(self.users),
            columns_names=["PESEL", "Imie", "Nazwisko", "Plec", "Data_urodzenia", "Data_uzyskania_prawa_jazdy"],
            file_name=f"csv/{suffix}/users" + ".csv",
            suffix=suffix
            )

        self.create_csv(
            self.generate_csv_data(self.rides),
            ["Id", "PESEL_uzytkownika", "Nr_rejestracyjny_pojazdu", "Data_rozpoczecia", "Data_zakonczenia",
            "Godzina_rozpoczecia", "Godzina_zakonczenia", "Miejsce_rozpoczecia", "Miejsce_zakonczenia",
            "Dystans", "Ocena_przejazdu", "Ocena_techniki_jazdy", "Ocena_przestrzegania_przepisow_drogowych",
            "Mnoznik_ceny", "Koszt_przejazdu"],
            f"csv/{suffix}/rides" + ".csv",
            suffix=suffix
            )
        
        self.create_csv(
            data=self.generate_csv_data(self.mistakes),
            columns_names=["ID", "ID_przejazdu", "Data", "Godzina", "Miejsce", "Typ", "Odchył_od_poprawnej_wartości"],
            file_name=f"csv/{suffix}/mistakes" +".csv",
            suffix=suffix
        )
        
        self.create_csv(
            data=self.generate_csv_data(self.cars),
            columns_names=["Rejestracja", "VIN", "Marka", "Model", "Generacja", "Rok_produkcji", "Data_ostatniego_przeglądu"],
            file_name=f"csv/{suffix}/cars" + ".csv",
            suffix=suffix
        )
        
        self.create_csv(
            data=self.generate_csv_data(self.locations),
            columns_names=["ID", "Miasto", "Dzielnica", "Ulica", "Numer ulicy", "Kod pocztowy"],
            file_name=f"csv/{suffix}/locations" + ".csv",
            suffix=suffix
        )
        
        
    def create_csv(self, data, columns_names, file_name, suffix):
        if not os.path.exists("./csv"):
            os.mkdir("./csv")
        if not os.path.exists(f"./csv/{suffix}"):
            os.mkdir(f"./csv/{suffix}")
        df = pd.DataFrame(data, columns=columns_names)
        df.to_csv(file_name, index=False)
        print(f"Zapisano dane do pliku {file_name}")