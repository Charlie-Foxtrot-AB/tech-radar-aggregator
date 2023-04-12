import dataSources.thoughtWorks
import dataSources.ingka
from docs import generateDocs

thoughtWorks = dataSources.thoughtWorks.getTechList()
ingka = dataSources.ingka.getTechList()

generateDocs(thoughtWorks + ingka)
