import requests
from bs4 import BeautifulSoup

def getData(url, eventCategory):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = []

    for entry in soup.find_all('div', {'data-event-category': eventCategory}):
        ranking = entry.find('span', {'class': 'blip-graphic-id'}).text
        name = entry.find('span', {'class': 'blip-name'}).text
        results.append(ranking + ' ' + name)

    return results