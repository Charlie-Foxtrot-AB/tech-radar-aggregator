import dataSources.thoughtWorks
from docs import category, generateDocs

quarters = [
    ('Techniques', 'https://www.thoughtworks.com/radar/techniques', 'Tech Radar - Techniques'),
    ('Platforms', 'https://www.thoughtworks.com/radar/platforms', 'Tech Radar - Platforms'),
    ('Tools', 'https://www.thoughtworks.com/radar/tools', 'Tech Radar - Tools'),
    ('Languages and frameworks', 'https://www.thoughtworks.com/radar/languages-and-frameworks', 'Tech Radar - Languages-and-frameworks')
]

categories = []

for idx, part in enumerate(quarters):
    newCategory = category(part[0], [])
    newCategory.results = dataSources.thoughtWorks.getData(part[1], part[2])
    categories.append( newCategory )

generateDocs(categories)