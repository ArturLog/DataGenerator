from faker import Faker


class User:
    def __init__(self, id):
        fake = Faker()
        self.PESEL = id + 10**11
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.sex = fake.random_element(elements=('Mezczyzna', 'Kobieta'))
        self.birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%d-%m-%Y"),
        self.licence_date = fake.date_of_birth(minimum_age=0, maximum_age=70).strftime("%d-%m-%Y"), 