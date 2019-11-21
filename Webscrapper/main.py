from company import Company
import os
from pathlib import Path

companylist = []


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def generate_keyvalues_forlist():
    clear_keyvalues_folder()
    for element in companylist:
        element.generate_keyvalues()


def clear_keyvalues_folder():
    i = 0
    for element in companylist:
        if os.path.exists("Keyvalues/" + element.get_name() +
                          "_keyvalues.json"):
            i += 1
            os.remove("Keyvalues/" + element.get_name() +
                      "_keyvalues.json")
    print("deleted " + str(i) + " elements")


companylist.append(Company('Amazon', 'AMZN'))

#generate_keyvalues_forlist()
clear_keyvalues_folder()
