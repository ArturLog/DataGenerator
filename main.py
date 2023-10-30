from datetime import datetime
from services.Generator import Generator

AMOUNT_OF_USERS_FIRST_PERIOD = 1000
AMOUNT_OF_USERS_SECOND_PERIOD = 500
AMOUNT_OF_RIDES_FIRST_PERIOD = 1000
AMOUNT_OF_RIDES_SECOND_PERIOD = 500
AMOUNT_OF_MISTAKES_FIRST_PERIOD = 1000
AMOUNT_OF_MISTAKES_SECOND_PERIOD = 500
AMOUNT_OF_CARS_FIRST_PERIOD = 1000
AMOUNT_OF_CARS_SECOND_PERIOD = 500
AMOUNT_OF_LOCATIONS_FIRST_PERIOD = 1000
AMOUNT_OF_LOCATIONS_SECOND_PERIOD = 500

T0 = datetime(2001, 1, 1, 0, 0, 1)
T1 = datetime(2001, 6, 6, 0, 0, 1)
T2 = datetime(2002, 1, 1, 0, 0, 1)

if __name__ == '__main__':
    generator = Generator()
    generator.config(start_date=T0, end_date=T1,
                          users_amount=AMOUNT_OF_USERS_FIRST_PERIOD,
                          rides_amount=AMOUNT_OF_RIDES_FIRST_PERIOD,
                          mistakes_amount=AMOUNT_OF_MISTAKES_FIRST_PERIOD,
                          cars_amount=AMOUNT_OF_CARS_FIRST_PERIOD,
                          locations_amount=AMOUNT_OF_LOCATIONS_FIRST_PERIOD)
    generator.generate_all(modify=False)
    generator.create_all_csv("first")
    generator.config(     
                          start_date=T0, end_date=T2,
                          users_amount=AMOUNT_OF_USERS_SECOND_PERIOD,
                          rides_amount=AMOUNT_OF_RIDES_SECOND_PERIOD,
                          mistakes_amount=AMOUNT_OF_MISTAKES_SECOND_PERIOD,
                          cars_amount=AMOUNT_OF_CARS_SECOND_PERIOD,
                          locations_amount=AMOUNT_OF_LOCATIONS_SECOND_PERIOD)
    generator.generate_all(modify=True)
    generator.create_all_csv("second")
  