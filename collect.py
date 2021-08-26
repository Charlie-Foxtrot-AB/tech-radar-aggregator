import dataSources.thoughtWorks
from docs import generateDocs

categories = dataSources.thoughtWorks.getTechList()

generateDocs(categories)