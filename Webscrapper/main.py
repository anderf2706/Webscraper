from company import Company
import os
from pathlib import Path
import shutil

namelist = []
companylist = []


def add(*names):
    for x in names:
        namelist.append(str(x))


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def generate_keyvalues_forlist(delete_previous, generate_keyvalues):
    if delete_previous:
        clear_folder()
        delete_folder()

    if generate_keyvalues:
        for name in namelist:
            companylist.append(Company(name))
        for element in companylist:
            element.generate_keyvalues()


def clear_folder():
    i = 0
    for element in namelist:
        if os.path.exists("Companies/" + element +
                          '/' + element + '_keyvalues.json'):
            i += 1
            os.remove("Companies/" + element +
                      '/' + element + '_keyvalues.json')
    print("deleted " + str(i) + " files")


def delete_folder():
    i = 0
    for element in namelist:
        if os.path.exists("Companies/" + element):
            shutil.rmtree('Companies/' + element, ignore_errors=True)
            i += 1
    print("deleted " + str(i) + " folders")


add('Equinor', 'Microsoft', 'NorskHydro')
generate_keyvalues_forlist(True, True)
# clear_keyvalues_folder()
