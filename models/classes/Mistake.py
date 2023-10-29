import random
from models.interfaces.CsvData import CsvData
from functions import generate_random_date, generate_random_time

OBSERVANCE_OF_ROAD_REGULATIONS_MISTAKES_AMOUNT = 4
TECHNICAL_MISTAKES_AMOUNT = 2

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
        
        self.mistake_nature = self.check_mistake_nature()
    
    # Zakładam, że pierwsze sa zawsze wykroczenia
    def check_mistake_nature(self):
        i = 0
        for mistake_type in mistake_types:
            i += 1
            if mistake_type == self.mistake_type and i <= OBSERVANCE_OF_ROAD_REGULATIONS_MISTAKES_AMOUNT:
                return "T"
            else:
                return "O"
    
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