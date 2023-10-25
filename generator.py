import pandas as pd
import numpy as np
from faker import Faker
from datetime import date
fake = Faker()

AMOUNT_OF_UZYTKOWNICY = 10
AMOUNT_OF_PRZEJAZD = 100
AMOUNT_OF_BLAD_PRZEJAZDU = 100

T0 = date(2001, 1, 1)
T1 = date(2002, 1, 1)
T2 = date(2003, 1, 1)


# PESEL, Imię, Nazwisko, Płeć, Data urodzenia, Data uzyskania prawa jazdy
users_data = []

def generateUzytkownik(id):
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%d-%m-%Y"),
    licence_date = fake.date_of_birth(minimum_age=0, maximum_age=70).strftime("%d-%m-%Y"),  
        
    users_data.append([
        id + 10**11,
        fake.first_name(),
        fake.last_name(),
        fake.random_element(elements=('Mezczyzna', 'Kobieta')),
        birth_date,
        licence_date
    ])

def generateUzytkownicy():
    for i in range(AMOUNT_OF_UZYTKOWNICY):
        generateUzytkownik(i)
        

def createCsv(data, columns_names, file_name):
    df = pd.DataFrame(data, columns=columns_names)
    df.to_csv(file_name, index=False)
    print(f"Zapisano dane do pliku {file_name}")
            



    


# # Id, PESEL_użytkownika, Nr_rejestracyjny_pojazdu,
# # Data_rozpoczecia, Data_zakonczenia,
# # Godzina_rozpoczecia, Godzina_zakonczenia,
# # Miejsce_rozpoczęcia, Miejsce_zakonczenia,
# # Dystans, Ocena_przejazdu, Ocena_techniki_jazdy
# # Ocena_przestrzegania_przepisow_drogowych
# # Mnoznik_ceny, Koszt_przejazdu
# def generatePrzejazd():
#     print("Generuje przejazdy")
    
    
# # Id, Id_przejazdu, Data, Godzina, Miejsce, Typ,
# # Odchyl_od_poprawnej_wartosci
# def generateBladPrzejazdu():
#     print("Generuje błędy przejazdu")
    
    

generateUzytkownicy()
createCsv(
    users_data,
    ["PESEL", "Imie", "Nazwisko", "Plec", "Data_urodzenia", "Data_uzyskania_prawa_jazdy"],
    "users.csv"
    )