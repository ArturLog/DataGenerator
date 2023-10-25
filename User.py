from datetime import date
import functions as fun
from faker import Faker

# PESEL, Imię, Nazwisko, Płeć, Data urodzenia, Data uzyskania prawa jazdy
class User:
    def __init__(self, id, min_age=18, max_age=90, death_at_age=90):
        fake = Faker()
        self.PESEL = fun.generatePESEL(id)
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.sex = fake.random_element(elements=('Mezczyzna', 'Kobieta'))
        self.birth_date = fake.date_of_birth(minimum_age=min_age, maximum_age=max_age)
        self.licence_date = fake.date_between_dates(fun.add_years(self.birth_date, min_age + 1), 
                                                    date.today())
        self.alive = fun.calculateAge(self.birth_date) > death_at_age
    
    def getCsvData(self):
        return [
            self.PESEL,
            self.first_name,
            self.last_name,
            self.sex,
            self.birth_date,
            self.licence_date
        ]