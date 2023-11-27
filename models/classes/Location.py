import random
from models.interfaces.CsvData import CsvData

cities = ["Warszawa", "Krakow", "Poznan", "Wroclaw", "Gdansk", "Gdynia", "Sopot"]
disctricts = ["Polnoc", "Poludnie", "Wschod", "Zachod", "Centrum", "Stare Miasto"]
streets = ["Grunwaldzka", "Pilsudskiego", "Pogodna", "Mila", "Klonowa", "Sosnowa", "Mickiewicza"]

# Aktulanie moga sie powtarzac
class Location(CsvData):
    def __init__(self, id):
        self.id = id
        self.city = random.choice(cities)
        self.disctrict = random.choice(disctricts)
        self.street = random.choice(streets)
        self.number = f"{random.randint(1, 100)}{random.choice(['A', 'B', 'C'])}"
        self.postcode = f"{random.randint(10, 99)}-{random.randint(100, 999)}"
        
    def get_csv_data(self):
        return [
            self.id,
            self.city,
            self.disctrict,
            self.street,
            self.number,
            self.postcode
        ]