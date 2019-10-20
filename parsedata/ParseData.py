import json
with open("C:/Users/Anders Fredriksen/PycharmProjects/Webscrapper/Webscrapper/twitterData.json") as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
    if "31/07/2014" in i["date"]:
        print(i["date"])

