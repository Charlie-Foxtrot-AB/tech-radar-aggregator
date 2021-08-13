import requests
from bs4 import BeautifulSoup

quarters = [
    ('Techniques', 'https://www.thoughtworks.com/radar/techniques', 'Tech Radar - Techniques'),
    ('Platforms', 'https://www.thoughtworks.com/radar/platforms', 'Tech Radar - Platforms'),
    ('Tools', 'https://www.thoughtworks.com/radar/tools', 'Tech Radar - Tools'),
    ('Languages and frameworks', 'https://www.thoughtworks.com/radar/languages-and-frameworks', 'Tech Radar - Languages-and-frameworks')
]

def printThoughtWorksList(category, url, eventCategory):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    print('\n' + category + ':')

    for entry in soup.find_all('div', {'data-event-category': eventCategory}):
        ranking = entry.find('span', {'class': 'blip-graphic-id'}).text
        name = entry.find('span', {'class': 'blip-name'}).text
        print(ranking + ' ' + name)

for part in quarters:
    printThoughtWorksList(part[0], part[1], part[2])