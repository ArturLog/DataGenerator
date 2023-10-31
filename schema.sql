
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
            