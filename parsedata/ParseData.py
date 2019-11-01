import json
with open("C:/Users/Anders Fredriksen/PycharmProjects/Webscrapper/Webscrapper/keyvalues.json") as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
    print(i['2018'])

