import random
from CsvData import CsvData
from functions import generate_random_date, generate_random_time

mistake_types = {
    "Przekroczenie prędkości": [10, 20, 30, 40, 50],
    "Parking w niedozwolonym miejscu": [1],
    "Nieprzepisowa zmiana pasa ruchu": [1],
    "Niedostosowanie się do znaku nakazu/zakazu": [1],
    "Gwałtowne hamowanie": [1],
    "Jazda na zbyt wysokich obrotach": [1000, 1500, 2000, 2500, 3000]
}

class Mistake(CsvData):
    def __init__(self, id, t0, t2, rides_amount, locations_amount):
        self.id = id
        self.t0 = t0
        self.t2 = t2
        self.rides_amount = rides_amount
        self.locations_amount = locations_amount
        self.ride_id = random.randint(1, self.rides_amount)
        self.date = generate_random_date(self.t0, self.t2)
        self.time = generate_random_time()
        self.location_id = random.randint(1, self.locations_amount)
        self.mistake_type = random.choice(list(mistake_types.keys()))
        self.deviation = random.choice(list(mistake_types[self.mistake_type]))
    
    def get_csv_data(self):
        return [
            self.id,
            self.ride_id,
            self.date,
            self.time,
            self.location_id,
            self.mistake_type,
            self.deviation
        ]