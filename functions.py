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

def generate_template_time(datatime):
    hour = datatime.hour
    minute = datatime.minute
    second = datatime.second
    time = f"{hour:02d}:{minute:02d}:{second:02d}"
    
    return time

def create_schema():
  with open('schema.sql', 'w', encoding='utf-8') as file:
    file.write('''
  CREATE DATABASE Baza;
  
  CREATE TABLE Uzytkownik (
      PESEL BIGINT PRIMARY KEY,
      Imie VARCHAR(50),
      Nazwisko VARCHAR(50),
      Plec VARCHAR(20),
      Data_urodzenia DATE,
      Data_uzyskania_prawa_jazdy DATE
  );
   
  CREATE TABLE Przejazd (
      ID INTEGER primary key,
      PESEL_Uzytkownika BIGINT,
      Nr_rejestracyjny_pojazdu VARCHAR(30),
      Data_rozpoczecia DATE,
      Godzina_rozpoczecia TIME,
      Data_zakonczenia DATE,
      Godzina_zakonczenia TIME,
      Miejsce_rozpoczecia INTEGER,
      Miejsce_zakonczenia INTEGER,
      Dystans DECIMAL(5,2),
      Ocena_przejazdu DECIMAL(5,2),
      Ocena_techniki_jazdy DECIMAL(5,2),
      Ocena_przestrzegania_przepisow_drogowych DECIMAL(5,2),
      Mnoznik_ceny DECIMAL(5,2),
      Koszt_przejazdu DECIMAL(5,2),
      FOREIGN KEY (PESEL_Uzytkownika) REFERENCES Uzytkownik(PESEL)
  );

  CREATE TABLE Bledy_przejazdu (
      ID INTEGER PRIMARY KEY,
      ID_Przejazdu INTEGER,
      Data DATE,
      Godzina TIME,
      Miejsce INTEGER,
      Typ VARCHAR(50),
      Odchyl_od_poprawnej_wartosci INTEGER,
      FOREIGN KEY (ID_Przejazdu) REFERENCES Przejazd(ID)
  );
            ''')