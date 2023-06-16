import requests
from constants import API_URL, COUNTRIES, YEARS

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MacroFiscalData(metaclass=Singleton):
    """
        Class that contains all the methods to do requests to
        the World Bank API, also is a singleton class which
        allow us to have only one instance of variables in
        the execution of the program.
    """

    gdp = {}
    inflation = {}
    unemploy = {}
    debt = {}
    incomes = {}
    expenses = {}

    def __init__(self) -> None:
        self.get_gdp_pca()


    """------------------- Macro economics Data From here -------------------"""

    def get_gdp_pca(self):
        """
            This method brings gross domestic product per capita in US$ data from the world bank in format json
            Output:
                -
        """
        for country in COUNTRIES.values():
            url = f"{API_URL}country/{country}/indicator/NY.GDP.PCAP.CD?format=json"
            resp = requests.get(url)
            data = resp.json()

            MacroFiscalData.gdp[country] = {}
            for entry in data[1]:
                if entry["value"] == None:
                    continue
                if entry["date"] in YEARS:
                    MacroFiscalData.gdp[country][entry["date"]] = entry["value"]
        MacroFiscalData.gdp["Currency"] = "US$"


    def get_inflation(self):
        """ This method brings inflation in annual % data from the world bank in format json"""
        for country in COUNTRIES.values():
            url = f"{API_URL}country/{country}/indicator/FP.CPI.TOTL.ZG?format=json"
            resp = requests.get(url)
            data = resp.json()

            MacroFiscalData.inflation[country] = {}
            for entry in data[1]:
                if entry["value"] == None:
                    continue
                if entry["date"] in YEARS:
                    MacroFiscalData.inflation[country][entry["date"]] = entry["value"]
        MacroFiscalData.inflation["Currency"] ="Annual %"


    def get_uem(self):
        """ This method brings unemployment in % of total labor force data from the world bank in format json"""
        for country in COUNTRIES.values():
            url = f"{API_URL}country/{country}/indicators/SL.UEM.TOTL.ZS?format=json"
            resp = requests.get(url)
            data = resp.json()

            MacroFiscalData.unemploy[country] = {}
            for entry in data[1]:
                    if entry["value"] == None:
                        continue
                    if entry["date"] in YEARS:
                        MacroFiscalData.unemploy[country][entry["date"]] = entry["value"]
        MacroFiscalData.unemploy["Currency"] = "% of total labor force"


    """ ------------------- Fiscal Data From here -------------------"""

    def get_public_debt(self):
        """ This method brings central government debt in % of GDP data from the world bank in format json"""
        for country in COUNTRIES.values():
            url = f"{API_URL}country/{country}/indicator/GC.DOD.TOTL.GD.ZS?format=json"
            resp = requests.get(url)
            data = resp.json()

            MacroFiscalData.debt[country] = {}
            for entry in data[1]:
                    if entry["value"] == None:
                        continue
                    if entry["date"] in YEARS:
                        MacroFiscalData.debt[country][entry["date"]] = entry["value"]
        MacroFiscalData.debt["Currency"] = "% of GDP"

    def get_incomes(self):
        """ This method brings the gross national income in US$ data from the world bank in format json"""
        for country in COUNTRIES.values():
            url = f"{API_URL}country/{country}/indicator/NY.GNP.MKTP.CD?format=json"
            resp = requests.get(url)
            data = resp.json()

            MacroFiscalData.incomes[country] = {}
            for entry in data[1]:
                    if entry["value"] == None:
                        continue
                    if entry["date"] in YEARS:
                        MacroFiscalData.incomes[country][entry["date"]] = entry["value"]
        MacroFiscalData.incomes["Currency"] = "US$"

    def get_tax_expenses(self):
        """ This method brings tax expenses in % of GDP data from the world bank in format json"""
        for country in COUNTRIES.values():
            url = f"{API_URL}country/{country}/indicator/GC.XPN.TOTL.GD.ZS?format=json"
            resp = requests.get(url)
            data = resp.json()

            MacroFiscalData.expenses[country] = {}
            for entry in data[1]:
                    if entry["value"] == None:
                        continue
                    if entry["date"] in YEARS:
                        MacroFiscalData.expenses[country][entry["date"]] = entry["value"]
        MacroFiscalData.expenses["Currency"] = "% of GDP"