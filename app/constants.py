import os

from dotenv import load_dotenv
load_dotenv()

API_URL = os.getenv("API_URL")
COUNTRIES = {
    "Colombia": "CO",
    "El Salvador": "SLV",
    "Guatemala": "GTM",
    "Honduras": "HND",
    "Nicaragua": "NIC",
    "Panamá": "PAN",
    "México": "MEX",
    "Argentina": "ARG",
    "Bolivia": "BOL",
    "Brasil": "BRA",
    "Chile": "CHL",
    "Perú": "PER",
    "Ecuador": "ECU",
    "Paraguay": "PRY",
    "Costa Rica": "CRI",
    "Uruguay": "URY"
}
FLAGS = {
    "Colombia": "co",
    "El Salvador": "sv",
    "Guatemala": "gt",
    "Honduras": "hn",
    "Nicaragua": "ni",
    "Panamá": "pa",
    "México": "mx",
    "Argentina": "ar",
    "Bolivia": "bo",
    "Brasil": "br",
    "Chile": "cl",
    "Perú": "pe",
    "Ecuador": "ec",
    "Paraguay": "py",
    "Costa Rica": "cr",
    "Uruguay": "uy"
}

YEARS = [
    "2021", "2020", "2019", "2018", "2017",
    "2016", "2015", "2014", "2013", "2012",
    "2011", "2010", "2009", "2008", "2007",
    "2006", "2005", "2004", "2003", "2002",
    ]