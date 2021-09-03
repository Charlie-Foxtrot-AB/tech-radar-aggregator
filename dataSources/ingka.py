import requests
from docs import category
import json


class ingkaTechItem:
    def __init__(self, title, description, ring, link, state, quadrant):
        self.title = title
        self.description = description
        self.ring = ring
        self.link = link
        self.state = state
        self.quadrant = quadrant


url = "https://rikta-backend-qxmvllfjea-ez.a.run.app/api/radar-content-light"
categoryMap = {
    0: "Data Management & Integration",
    1: "Languages & Frameworks",
    2: "Practices & Techniques",
    3: "Tools & Platforms",
}


def getTechList():
    charlieCategories = []
    ingkaBuzzwords = getBuzzwords()
    categoriesDictionary = transformToDictionary(ingkaBuzzwords)

    for key, value in categoriesDictionary.items():
        charlieCategories.append(category(key, value))
    return charlieCategories


def transformToDictionary(ingkaBuzzwords):
    results = {}
    for ingkaBuzzword in ingkaBuzzwords:
        categoryName = categoryMap[ingkaBuzzword.quadrant]
        if categoryName not in results:
            results[categoryName] = []
        results[categoryName].append(ingkaBuzzword.title)
    return results


def getBuzzwords():
    response = requests.get(url)
    results = []

    content = json.loads(response.text)

    for buzzWord in content["technologies"]:
        results.append(
            ingkaTechItem(
                buzzWord["title"],
                buzzWord["description"],
                buzzWord["ring"],
                buzzWord["link"],
                buzzWord["state"],
                buzzWord["quadrant"],
            )
        )

    return results
