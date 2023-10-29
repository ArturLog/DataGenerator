import pandas as pd
import random as rand
from faker import Faker
from datetime import date
from models.classes.User import User
from models.classes.Ride import Ride
from models.classes.Car import Car
from models.classes.Mistake import Mistake

class Generator:
    def __init__(self, t0, t1, t2, users_amount=100, rides_amount=100, mistakes_amount=100, cars_amount=100, locations_amount=100):
        self.users = []
        self.rides = []
        self.mistakes = []
        self.cars = []
        self.locations = []
        self.t0 = t0
        self.t1 = t1
        self.t2 = t2
        self.users_amount = users_amount
        self.rides_amount = rides_amount
        self.mistakes_amount = mistakes_amount
        self.cars_amount = cars_amount
        self.locations_amount = locations_amount
        
        self.generate_users()
        #self.generate_rides()
        self.generate_cars()
        self.generate_mistakes()
        
    def generate_users(self):
        for i in range(self.users_amount):
            self.users.append(User(i))
    
    def generate_cars(self):
        for i in range(self.cars_amount):
            self.cars.append(Car(t0=self.t0, t2=self.t1))
        
    def generate_rides(self):
        for i in range(self.rides_amount):
            self.rides.append(Ride(i, self.users[rand.randint(0, self.users_amount-1)]))
            
    def generate_mistakes(self):
        for i in range(self.mistakes_amount):
            self.mistakes.append(Mistake((i-1), self.t0, self.t2, self.rides_amount, self.locations_amount))

    def generate_csv_data(self, generatedData):
        data = []
        for d in generatedData:
            data.append(d.get_csv_data())
        return data
        
    def create_all_csv(self):
        self.create_csv(
            data=self.generate_csv_data(self.users),
            columns_names=["PESEL", "Imie", "Nazwisko", "Plec", "Data_urodzenia", "Data_uzyskania_prawa_jazdy"],
            file_name="csv/users.csv"
            )

        # self.create_csv(
        #     self.generate_csv_data(self.rides),
        #     ["Id", "PESEL_uzytkownika", "Nr_rejestracyjny_pojazdu", "Data_rozpoczecia", "Data_zakonczenia",
        #     "Godzina_rozpoczecia", "Godzina_zakonczenia", "Miejsce_rozpoczecia", "Miejsce_zakonczenia",
        #     "Dystans", "Ocena_przejazdu", "Ocena_techniki_jazdy", "Ocena_przestrzegania_przepisow_drogowych",
        #     "Mnoznik_ceny", "Koszt_przejazdu"],
        #     "csv/rides.csv"
        #     )
        
        self.create_csv(
            data=self.generate_csv_data(self.mistakes),
            columns_names=["ID", "ID_przejazdu", "Data", "Godzina", "Miejsce", "Typ", "Odchył_od_poprawnej_wartości"],
            file_name="csv/mistakes.csv"
        )
        
        self.create_csv(
            data=self.generate_csv_data(self.cars),
            columns_names=["Rejestracja", "VIN", "Marka", "Model", "Generacja", "Rok_produkcji", "Data_ostatniego_przeglądu"],
            file_name="csv/cars.csv"
        )
        
        
    def create_csv(self, data, columns_names, file_name):
        df = pd.DataFrame(data, columns=columns_names)
        df.to_csv(file_name, index=False)
        print(f"Zapisano dane do pliku {file_name}")