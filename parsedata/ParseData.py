import json
import company
import pandas as pd

def convert_to_json(name):
    with open("C:/Users/Anders Fredriksen/PycharmProjects/Webscrapper/Webscrapper/" + name + "_keyvalues.json") as json_data:
        return json.load(json_data)


def into_panda():
    pand = pd.read_json("C:/Users/Anders Fredriksen/PycharmProjects/Webscrapper/Webscrapper/Equinor_keyvalues.json")
    pand2 = pd.read_json((pand['Totalrentabilitet']).to_json(), orient='index')
    print(pand2)

def compare_values(name1, name2, value):
    json1 = convert_to_json(str(name1))
    list1 = []
    for i in json1[value]:
        list1.insert(int(i), 0)

    json2 = convert_to_json(str(name2))
    list2 = json2[str(value)].values()
    return list1

    #plt.plot(list1)
    #plt.show()

print(compare_values('Equinor', 'Norsk Hydro', 'Totalrentabilitet'))
