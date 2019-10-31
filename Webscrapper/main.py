import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import time

def get_to_side():
    selskap = input("selskap:")
    for i in range(0, len(selskap)):
        if selskap[i] == " ":
            selskap = selskap.replace(" ", "%20")

    result = requests.get("https://www.proff.no/bransjes%C3%B8k?q=" + selskap)
    #print(result.status_code)
    #print(result.headers)
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
    keyvalarr = [Keyvalues.get_Totalrentabilitet(), Keyvalues.get_Resultat_av_driften(),
                 Keyvalues.get_Egenkapitalens_rentabilitet_før_skatt(), Keyvalues.get_Likviditetsgrad(),
                 Keyvalues.get_Egenkapitalandel(), Keyvalues.get_Gjeldsgrad()]
    with open("keyvalues.json", "w") as outfile:
        json.dump(keyvalarr, outfile)

    print("done")

#main
result_nokkeltall = requests.get(get_to_side())
src_nokkeltall = result_nokkeltall.content
content_nokkel = BeautifulSoup(src_nokkeltall, "html.parser")
write_keyvalues()

#end_main

