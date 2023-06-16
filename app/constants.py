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
    "Venezuela": "VEN",
    "Ecuador": "ECU",
    "Paraguay": "PRY",
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
    "Venezuela": "ve",
    "Ecuador": "ec",
    "Paraguay": "py",
}