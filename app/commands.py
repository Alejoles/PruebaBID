import requests
from constants import API_URL, COUNTRIES, YEARS

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MacroFiscalData:

    __metaclass__ = Singleton

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
            This function brings gross domestic product per capita in US$ data from the world bank in format json
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
        """ This function brings inflation in annual % data from the world bank in format json"""
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
        """ This function brings unemployment in % of total labor force data from the world bank in format json"""
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
        """ This function brings central government debt in % of GDP data from the world bank in format json"""
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
        """ This function brings the gross national income in US$ data from the world bank in format json"""
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
        """ This function brings tax expenses in % of GDP data from the world bank in format json"""
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