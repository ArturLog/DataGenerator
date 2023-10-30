import functions as fun
import sys
from datetime import date, datetime
from faker import Faker
sys.path.append("models/interfaces")
from CsvData import CsvData

fake = Faker()
# PESEL, Imię, Nazwisko, Płeć, Data urodzenia, Data uzyskania prawa jazdy
class User(CsvData):
    def __init__(self, id):
        self.user_config()
        self.PESEL = fun.generatePESEL(id)
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.sex = fake.random_element(elements=('Mezczyzna', 'Kobieta'))
        self.birth_date = fake.date_of_birth(minimum_age=self.min_age, maximum_age=self.max_age)
        self.licence_date = fun.generate_random_date(fun.add_years(self.birth_date, self.min_age), 
                                                    date.today())
        self.alive = fun.calculateAge(self.birth_date) < self.death_at_age
        self.last_rental = datetime(1000, 1, 1)
        
    def user_config(self, min_age=18, max_age=90, death_at_age=90):
        self.min_age = min_age
        self.max_age = max_age
        self.death_at_age = death_at_age
    
    def get_csv_data(self):
        return [
            self.PESEL,
            self.first_name,
            self.last_name,
            self.sex,
            self.birth_date,
            self.licence_date
        ]