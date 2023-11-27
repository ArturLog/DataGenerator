import random
import string
from datetime import datetime
from models.interfaces.CsvData import CsvData
from functions import generate_random_date

car_brands = {
    "Skoda": ["Fabia", "Octavia", "Suberb"],
    "Audi": ["A3", "A4", "A5"],
    "BMW": ["M3", "M4", "X5", "X6"],
}

#Aktualnie moga sie powtarzac
class Car(CsvData):
    def __init__(self, t0, t2, locations_amount):
        self.t0 = t0
        self.t2 = t2
        self.registration = self.generate_registration()
        self.vin = self.generate_vin()
        self.brand = random.choice(list(car_brands.keys()))
        self.model = random.choice(car_brands[self.brand])
        self.generation = random.randint(1,3)
        self.production_year = random.randint(2010, 2012)
        self.last_inspection = generate_random_date(self.t0, self.t2)
        
        self.last_rental = datetime(1000, 1, 1)
        self.location = random.randint(1, locations_amount)
        
        
    def generate_registration(self):
        city = self.generate_city_part()
        remaining_length = random.randint(4, 5)
        remaining_part = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(remaining_length))
        license_plate = f'{city} {remaining_part}'
        return license_plate
    
    def generate_city_part(self):
        city = ''
        city_length = random.choice([2, 3])
        for _ in range(city_length):
            city += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return city
    
        # Numer VIN składa się z 17 znaków, w tym cyfr i liter.
    def generate_vin(self):
        vin_prefix = "1HG"      # Pierwsze trzy znaki numeru VIN to stałe znaki identyfikacyjne
        vin_digits = ''.join(random.choice(string.digits + string.ascii_uppercase) for _ in range(14))
        vin_check_digit = str(random.choice(string.digits))     # Cyfra kontrolna numeru VIN
        vin = vin_prefix + vin_digits + vin_check_digit
        return vin
    
    def get_csv_data(self):
        return [
            self.registration, 
            self.vin, 
            self.brand, 
            self.model, 
            self.generation, 
            self.production_year, 
            self.last_inspection.date()
            ]