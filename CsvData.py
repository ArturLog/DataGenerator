from abc import ABC, abstractmethod

class CsvData:
    def __init__(self):
        pass
    
    @abstractmethod
    def get_csv_data(self):
        pass