import requests
from bs4 import BeautifulSoup

url = "https://medcomfhir.dk/ig/homecareobservation/"

r = requests.get(url, timeout=20)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")

print(soup.get_text(separator="\n", strip=True))