import pandas as pd
import random as rand
from faker import Faker
from datetime import date
from User import User
from Ride import Ride
fake = Faker()

AMOUNT_OF_UZYTKOWNICY = 10
AMOUNT_OF_PRZEJAZD = 100
AMOUNT_OF_BLAD_PRZEJAZDU = 100
TODAY_DATE = date(2023, 10, 25)

T0 = date(2001, 1, 1)
T1 = date(2002, 1, 1)
T2 = date(2003, 1, 1)

road_mistakes_data = []
rides_data = []

def createCsv(data, columns_names, file_name):
    df = pd.DataFrame(data, columns=columns_names)
    df.to_csv(file_name, index=False)
    print(f"Zapisano dane do pliku {file_name}")

def generateUsers(users):
    for i in range(AMOUNT_OF_UZYTKOWNICY):
        users.append(User(i))
        
def generateRaids(raids, users):
    for i in range(AMOUNT_OF_PRZEJAZD):
        raids.append(Ride(i, users[rand.randint(0, AMOUNT_OF_UZYTKOWNICY-1)]))

def generateCsvData(generatedData):
    data = []
    for d in generatedData:
        data.append(d.getCsvData())
    return data
    
    
# # Id, Id_przejazdu, Data, Godzina, Miejsce, Typ,
# # Odchyl_od_poprawnej_wartosci
    
# def generateBledyPrzejazdu():
#     for i in range(AMOUNT_OF_BLAD_PRZEJAZDU):
#         generateBladPrzejazdu(i)

# generateBledyPrzejazdu()
# createCsv(
#     road_mistakes_data,
#     ["Id", "Id_przejazdu", "Data", "Godzina", "Miejsce", "Typ", "Odchyl_od_poprawnej_wartosci"],
#     "road_mistakes.csv"
#     )
  

users = []
generateUsers(users)

rides = []
generateRaids(rides, users)

createCsv(
    generateCsvData(users),
    ["PESEL", "Imie", "Nazwisko", "Plec", "Data_urodzenia", "Data_uzyskania_prawa_jazdy"],
    "users.csv"
    )

createCsv(
    generateCsvData(rides),
    ["Id", "PESEL_uzytkownika", "Nr_rejestracyjny_pojazdu", "Data_rozpoczecia", "Data_zakonczenia",
     "Godzina_rozpoczecia", "Godzina_zakonczenia", "Miejsce_rozpoczecia", "Miejsce_zakonczenia",
     "Dystans", "Ocena_przejazdu", "Ocena_techniki_jazdy", "Ocena_przestrzegania_przepisow_drogowych",
     "Mnoznik_ceny", "Koszt_przejazdu"],
    "rides.csv"
    )