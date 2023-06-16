import requests
from constants import API_URL, COUNTRIES

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MacroFiscalData:

    __metaclass__ = Singleton


    def __init__(self) -> None:
        self.gdp = {}
        self.inflation = {}
        self.unemploy = {}
        self.debt = {}
        self.incomes = {}
        self.expenses = {}

    """------------------- Macro economics Data From here -------------------"""

    def get_gdp_pca(self, country:str, year:str):
        """ This function brings gross domestic product per capita in US$ data from the world bank in format json"""
        url = f"{API_URL}country/{country}/indicator/NY.GDP.PCAP.CD?format=json"
        resp = requests.get(url)
        data = resp.json()

        for entry in data[1]:
            if entry["value"] == None:
                print(f"Error, country {country} with year selected has not value of UEM yet,\
                        try another year or select a different country")
                return
            if entry["date"] == str(year):
                return country, str(year), entry["value"], "US$"


    def get_inflation(self, country:str, year:str):
        """ This function brings inflation in annual % data from the world bank in format json"""
        url = f"{API_URL}country/{country}/indicator/FP.CPI.TOTL.ZG?format=json"
        resp = requests.get(url)
        data = resp.json()

        for entry in data[1]:
            if entry["value"] == None:
                print(f"Error, country {country} with year selected has not value of UEM yet,\
                        try another year or select a different country")
                return
            if entry["date"] == str(year):
                return country, str(year), entry["value"], "Annual %"


    def get_uem(self, country:str, year:str):
        """ This function brings unemployment in % of total labor force data from the world bank in format json"""
        url = f"{API_URL}country/{country}/indicators/SL.UEM.TOTL.ZS?format=json"
        resp = requests.get(url)
        data = resp.json()

        for entry in data[1]:
            if entry["value"] == None:
                print(f"Error, country {country} with year selected has not value of UEM yet,\
                        try another year or select a different country")
                return
            if entry["date"] == str(year):
                return country, str(year), entry["value"], "% of total labor force"


    """ ------------------- Fiscal Data From here -------------------"""

    def get_public_debt(self, country:str, year:str):
        """ This function brings central government debt in % of GDP data from the world bank in format json"""
        url = f"{API_URL}country/{country}/indicator/GC.DOD.TOTL.GD.ZS?format=json"
        resp = requests.get(url)
        data = resp.json()

        for entry in data[1]:
            if entry["value"] == None:
                print(f"Error, country {country} with year selected has not value of UEM yet,\
                        try another year or select a different country")
                return
            if entry["date"] == str(year):
                return country, str(year), entry["value"], "% of GDP"

    def get_incomes(self, country:str, year:str):
        """ This function brings the gross national income in US$ data from the world bank in format json"""
        url = f"{API_URL}country/{country}/indicator/NY.GNP.MKTP.CD?format=json"
        resp = requests.get(url)
        data = resp.json()

        for entry in data[1]:
            if entry["value"] == None:
                print(f"Error, country {country} with year selected has not value of UEM yet,\
                        try another year or select a different country")
                return
            if entry["date"] == str(year):
                return country, str(year), entry["value"], "US$"

    def get_tax_expenses(self, country:str, year:str):
        """ This function brings tax expenses in % of GDP data from the world bank in format json"""
        url = f"{API_URL}country/{country}/indicator/GC.XPN.TOTL.GD.ZS?format=json"
        resp = requests.get(url)
        data = resp.json()

        for entry in data[1]:
            if entry["value"] == None:
                print(f"Error, country {country} with year selected has not value of UEM yet,\
                        try another year or select a different country")
                return
            if entry["date"] == str(year):
                return country, str(year), entry["value"], "% of GDP"