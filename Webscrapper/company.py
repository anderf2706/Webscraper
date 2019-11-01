import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import time
from Redditscrapper import Redditscrapper

companylist = []


def get_to_side(selskaplist):
    global selskap
    selskap = input("selskap:")
    if selskaplist is not None:
        selskap = selskaplist
    for i in range(0, len(selskap)):
        if selskap[i] == " ":
            selskap = selskap.replace(" ", "%20")

    result = requests.get("https://www.proff.no/bransjes%C3%B8k?q=" + selskap)
    # print(result.status_code)
    # print(result.headers)
    src = result.content

    content = BeautifulSoup(src, "html.parser")

    for hit in content.findAll(attrs={"class": "addax addax-cs_hl_hit_company_name_click"}):
        strings = str(hit).split('href=')
        dummiestrings = strings[1]
        dummiestrings = dummiestrings.split('>')
        dummiestrings = dummiestrings[0].replace('"', "")
        dummiestrings = dummiestrings.replace('selskap', 'nokkeltall')
        break
    print(dummiestrings)

    return "https://www.proff.no" + dummiestrings


"""
driver = webdriver.Chrome()
driver.get(get_to_side())
"""


def write_keyvalues():
    from Webscrapper import Keyvalues
    from importlib import reload
    reload(Keyvalues)
    keyvaldict = {'Totalrentabilitet': Keyvalues.get_Totalrentabilitet(),
                  'Resultat_av_drift': Keyvalues.get_Resultat_av_driften(),
                  'Egenkap.rentabilitet': Keyvalues.get_Egenkapitalens_rentabilitet_før_skatt(),
                  'Likviditetsgrad': Keyvalues.get_Likviditetsgrad(),
                  'Egenkapitalandel': Keyvalues.get_Egenkapitalandel(), 'Gjeldsgrad': Keyvalues.get_Gjeldsgrad()}

    with open(selskap + "_keyvalues.json", "w") as outfile:
        json.dump(keyvaldict, outfile)

    print("done")


class Company(object):
    def __init__(self, company):
        self.company = str(company)
        result_nokkeltall = requests.get(get_to_side(self.company))
        src_nokkeltall = result_nokkeltall.content
        global content_nokkel
        content_nokkel = BeautifulSoup(src_nokkeltall, "html.parser")

    def generate_keyvalues(self):
        write_keyvalues()

    def gather_redditdata(self, reddittype):
        Redditscrapper.gather_data(self.company)


# main
# result_nokkeltall = requests.get(get_to_side(None))
# src_nokkeltall = result_nokkeltall.content
# content_nokkel = BeautifulSoup(src_nokkeltall, "html.parser")
# write_keyvalues()

def generate_keyvalues_forlist():
    for company in companylist:
        company.generate_keyvalues()

companylist.append(Company('equinor'))
print(companylist[0])
