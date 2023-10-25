import pandas as pd
import numpy as np
import functions as fun
from faker import Faker
from datetime import date
from User import User
fake = Faker()

AMOUNT_OF_UZYTKOWNICY = 10
AMOUNT_OF_PRZEJAZD = 100
AMOUNT_OF_BLAD_PRZEJAZDU = 100

T0 = date(2001, 1, 1)
T1 = date(2002, 1, 1)
T2 = date(2003, 1, 1)

road_mistakes_data = []
rides_data = []

def createCsv(data, columns_names, file_name):
    df = pd.DataFrame(data, columns=columns_names)
    df.to_csv(file_name, index=False)
    print(f"Zapisano dane do pliku {file_name}")


def generateNrRejestracyjny():
    return 0


def generateUsers(users):
    for i in range(AMOUNT_OF_UZYTKOWNICY):
        users.append(User(i))
        
def generateUserData(users):
    users_data = []
    for user in users:
        users_data.append(user.getCsvData())
    return users_data
        

# def generatePrzejazd(id):
#     rides_data.append([
#         id,
#         generatePESEL(id), # tutaj randomowy musi byc
#         generateNrRejestracyjny(), # zalezny od pliku excel, sprawdzanie po dacie, zeby nie zostal wypozyczony ten sam 2 razy w tym samym momencie sry za dlugi koment
        
#     ])
    
# def generatePrzejazdy():
#     for i in range(AMOUNT_OF_PRZEJAZD):
#         generatePrzejazd(i)
    
# # Id, Id_przejazdu, Data, Godzina, Miejsce, Typ,
# # Odchyl_od_poprawnej_wartosci
# def generateBladPrzejazdu(id):
#     print("Generuje błędy przejazdu")
    
# def generateBledyPrzejazdu():
#     for i in range(AMOUNT_OF_BLAD_PRZEJAZDU):
#         generateBladPrzejazdu(i)

# generatePrzejazdy()
# createCsv(
#     rides_data,
#     ["Id", "PESEL_uzytkownika", "Nr_rejestracyjny_pojazdu", "Data_rozpoczecia", "Data_zakonczenia",
#      "Godzina_rozpoczecia", "Godzina_zakonczenia", "Miejsce_rozpoczecia", "Miejsce_zakonczenia",
#      "Dystans", "Ocena_przejazdu", "Ocena_techniki_jazdy", "Ocena_przestrzegania_przepisow_drogowych",
#      "Mnoznik_ceny", "Koszt_przejazdu"],
#     "rides.csv"
#     )

# generateBledyPrzejazdu()
# createCsv(
#     road_mistakes_data,
#     ["Id", "Id_przejazdu", "Data", "Godzina", "Miejsce", "Typ", "Odchyl_od_poprawnej_wartosci"],
#     "road_mistakes.csv"
#     )
  

users = []
generateUsers(users)
createCsv(
    generateUserData(users),
    ["PESEL", "Imie", "Nazwisko", "Plec", "Data_urodzenia", "Data_uzyskania_prawa_jazdy"],
    "users.csv"
    )