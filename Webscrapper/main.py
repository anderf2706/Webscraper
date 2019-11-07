from Webscrapper import company
import os


def generate_keyvalues_forlist():
    clear_keyvalues_folder()
    for element in company.companylist:
        element.generate_keyvalues()


def clear_keyvalues_folder():
    i = 0
    for element in company.companylist:
        if os.path.exists("C:/Users/Anders Fredriksen/PycharmProjects/Webscrapper/Keyvalues/" + element.get_name() +
              "_keyvalues.json"):
            i += 1
            os.remove("C:/Users/Anders Fredriksen/PycharmProjects/Webscrapper/Keyvalues/" + element.get_name() +
              "_keyvalues.json")
    print("deleted " + str(i) + " elements")


company.companylist.append(company.Company('Yara Norge'))
company.companylist.append(company.Company('Equinor'))

generate_keyvalues_forlist()

