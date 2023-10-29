import functions as fun
import sys
from datetime import date
from faker import Faker
sys.path.append("models/interfaces")
from CsvData import CsvData

MIN_AGE = 18
MAX_AGE = 90
DEATH_AT_AGE = 90

# PESEL, Imię, Nazwisko, Płeć, Data urodzenia, Data uzyskania prawa jazdy
class User(CsvData):
    def __init__(self, id, min_age=MIN_AGE, max_age=MAX_AGE, death_at_age=DEATH_AT_AGE):
        fake = Faker()
        self.PESEL = fun.generatePESEL(id)
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.sex = fake.random_element(elements=('Mezczyzna', 'Kobieta'))
        self.birth_date = fake.date_of_birth(minimum_age=min_age, maximum_age=max_age)
        self.licence_date = fun.generate_random_date(fun.add_years(self.birth_date, min_age), 
                                                    date.today())
        self.alive = fun.calculateAge(self.birth_date) > death_at_age
    
    def get_csv_data(self):
        return [
            self.PESEL,
            self.first_name,
            self.last_name,
            self.sex,
            self.birth_date,
            self.licence_date
        ]