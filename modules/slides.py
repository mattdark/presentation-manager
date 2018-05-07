import json

def listslides():
    with open('./static/slides.json') as data_file:
        data = json.load(data_file)

    id = list()
    title = list()

    list1 = []

    for i in range(len(data["slides"])):
        id = data["slides"][i]["id"]
        title = data["slides"][i]["title"]
        list1.append((id, title))

    return list1

def showslide(id):
    with open('./static/slides.json') as data_file:
        data = json.load(data_file)
    id = int(id)
    title = data["slides"][id-1]["title"]
    filen = data["slides"][id-1]["file"]
    description = data["slides"][id-1]["description"]
    style = data["slides"][id-1]["style"]

    return title, filen, description, style
