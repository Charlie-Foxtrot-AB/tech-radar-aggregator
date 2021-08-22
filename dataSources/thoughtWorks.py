import requests
from bs4 import BeautifulSoup
from docs import category

quarters = [
    ('Techniques', 'https://www.thoughtworks.com/radar/techniques', 'Tech Radar - Techniques'),
    ('Platforms', 'https://www.thoughtworks.com/radar/platforms', 'Tech Radar - Platforms'),
    ('Tools', 'https://www.thoughtworks.com/radar/tools', 'Tech Radar - Tools'),
    ('Languages and frameworks', 'https://www.thoughtworks.com/radar/languages-and-frameworks', 'Tech Radar - Languages-and-frameworks')
]
categories = []

def getTechList():
    for part in quarters:
        newCategory = category(part[0], [])
        newCategory.results = getData(part[1], part[2])
        categories.append( newCategory )
    return categories

def getData(url, eventCategory):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = []

    for entry in soup.find_all('div', {'data-event-category': eventCategory}):
        ranking = entry.find('span', {'class': 'blip-graphic-id'}).text
        name = entry.find('span', {'class': 'blip-name'}).text
        results.append(ranking + ' ' + name)

    return results