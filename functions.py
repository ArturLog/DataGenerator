import random
from datetime import date, timedelta

date_format = '%d/%m/%Y'  ################################
 
def calculateAge(birthDate):
    today = date.today()
    age = (today.year - birthDate.year - 
           ((today.month, today.day) < (birthDate.month, birthDate.day)))
 
    return age

def add_years(start_date, years):
    try:
        return start_date.replace(year=start_date.year + years)
    except ValueError:
        # if Feb 29th doesn't exist, set to 28th
        return start_date.replace(year=start_date.year + years, day=28)

def generatePESEL(id):
    return id + 10**11

def generate_random_date(start_date, end_date):
    date_range = end_date - start_date
    #print(str(end_date) + "-" + str(start_date) + " = " + str(date_range)) #################################
    random_days = random.randint(0, date_range.days)        
    random_date = start_date + timedelta(days=random_days)
    return random_date

def generate_random_datetime(start_datetime, end_datetime):
    time_difference = end_datetime - start_datetime
    random_time_difference = random.random() * time_difference.total_seconds()
    random_datetime = start_datetime + timedelta(seconds=random_time_difference)
    return random_datetime

def generate_random_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    time = f"{hour:02d}:{minute:02d}"
    
    return time

def create_schema():
  with open('schema.sql', 'w', encoding='utf-8') as file:
    file.write('''
  CREATE DATABASE Baza;
  
  CREATE TABLE Uzytkownik (
      PESEL INTEGER PRIMARY KEY,
      Imie TEXT,
      Nazwisko TEXT,
      Plec TEXT,
      Data_urodzenia DATE,
      Data_uzyskania_prawa_jazdy DATE
  );
   
  CREATE TABLE Przejazd (
      ID INTEGER primary key,
      PESEL_Uzytkownika INTEGER,
      Nr_rejestracyjny_pojazdu TEXT,
      Data_rozpoczecia DATE,
      Godzina_rozpoczecia DATE,
      Data_zakonczenia DATE,
      Godzina_zakonczenia DATE,
      Miejsce_rozpoczecia INTEGER,
      Miejsce_zakonczenia INTEGER,
      Dystans INTEGER,
      Ocena_przejazdu FLOAT,
      Ocena_techniki_jazdy FLOAT,
      Ocena_przestrzegania_przepisow_drogowych FLOAT,
      Mnoznik_ceny FLOAT,
      Koszt_przejazdu FLOAT,
      FOREIGN KEY (PESEL_Uzytkownika) REFERENCES Uzytkownik(PESEL)
  );

  CREATE TABLE Bledy_przejazdu (
      ID INTEGER PRIMARY KEY,
      ID_Przejazdu INTEGER,
      Data DATE,
      Godzina DATE,
      Miejsce TEXT,
      Typ TEXT,
      Odchyl_od_poprawnej_wartosci INTEGER,
      FOREIGN KEY (ID_Przejazdu) REFERENCES Przejazd(ID)
  );
            ''')