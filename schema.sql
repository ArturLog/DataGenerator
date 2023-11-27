
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
            