from datetime import date
from Generator import Generator

AMOUNT_OF_USERS = 100
AMOUNT_OF_RIDE = 100
AMOUNT_OF_MISTAKE = 100
AMOUNT_OF_CARS = 100
AMOUNT_OF_LOCATIONS = 100
# TODAY_DATE = date(2023, 10, 25)

T0 = date(2001, 1, 1)
T1 = date(2001, 6, 6)
T2 = date(2002, 1, 1)

if __name__ == '__main__':
    generator = Generator(t0=T0, t1=T1, t2=T2,
                          users_amount=AMOUNT_OF_USERS,
                          rides_amount=AMOUNT_OF_RIDE,
                          mistakes_amount=AMOUNT_OF_MISTAKE,
                          cars_amount=AMOUNT_OF_CARS,
                          locations_amount=AMOUNT_OF_LOCATIONS)
    generator.create_all_csv()
    
    
# # # Id, Id_przejazdu, Data, Godzina, Miejsce, Typ,
# # # Odchyl_od_poprawnej_wartosci
    
# # def generateBledyPrzejazdu():
# #     for i in range(AMOUNT_OF_BLAD_PRZEJAZDU):
# #         generateBladPrzejazdu(i)

# # generateBledyPrzejazdu()
# # createCsv(
# #     road_mistakes_data,
# #     ["Id", "Id_przejazdu", "Data", "Godzina", "Miejsce", "Typ", "Odchyl_od_poprawnej_wartosci"],
# #     "road_mistakes.csv"
# #     )
  