import requests 

r = requests.get('https://medcomfhir.dk/ig/homecareobservation/')


print(r.status_code)
print(r.url)
print(r.text)