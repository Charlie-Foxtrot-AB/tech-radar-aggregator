class category:
    def __init__(self, name, results): 
        self.name = name
        self.results = results

def generateDocs(categories):
  md_filename = "docs/index.md"
  md = "Lazy is such an ugly word. I prefer to call it selective participation."

  for category in categories:
    md += "\n\ncollection: " + category.name + "\n"
    for result in category.results:
      md += result + "\n"
  
  with open(md_filename, 'w') as f:
    f.write(md)