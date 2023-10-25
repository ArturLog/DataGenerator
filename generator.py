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
def generateUzytkownicy():
    for i in range(AMOUNT_OF_UZYTKOWNICY):
        
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%d-%m-%Y"),
        licence_date = fake.date_of_birth(minimum_age=0, maximum_age=70).strftime("%d-%m-%Y"),  
        
        
        users_data.append([
            i + 10**11,
            fake.first_name(),
            fake.last_name(),
            fake.random_element(elements=('Mezczyzna', 'Kobieta')),
            birth_date,
            licence_date
        ])
        
    # Nazwy kolumn w DataFrame
    csv_columns = ["PESEL", "Imie", "Nazwisko", "Plec", "Data_urodzenia", "Data_uzyskania_prawa_jazdy"]
    # Utworzenie DataFrame z danymi użytkowników
    df = pd.DataFrame(users_data, columns=csv_columns)
    # Nazwa pliku CSV do zapisu danych
    csv_filename = "users.csv"
    # Zapisanie danych do pliku CSV
    df.to_csv(csv_filename, index=False)
    print(f"Zapisano dane użytkowników do pliku {csv_filename}")
        
        
    


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