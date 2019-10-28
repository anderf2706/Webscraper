import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import time


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

result_nokkeltall = requests.get("https://www.proff.no" + dummiestrings)
src_nokkeltall = result_nokkeltall.content
content_nokkel = BeautifulSoup(src_nokkeltall, "html.parser")

ar = 2018
Totalrentabilitet = {}
for element in content_nokkel.find_all('tr', attrs={'data-chart-title': 'Totalrentabilitet i %'}):
    Totalrentabilitet[ar] = element.find('td').get_text()
    ar -= 1
    print(ar)

print(Totalrentabilitet.keys())
print(Totalrentabilitet.values())

ar = 2018
Resultat_Drift = {}
for element in content_nokkel.find_all('tr', attrs={'data-chart-title': 'Resultat av driften i %'}):
    Resultat_Drift[ar] = element.find('td').get_text()
    ar -= 1
    print(ar)

print(Resultat_Drift.keys())
print(Resultat_Drift.values())


Egenkapitalens_rentabilitet_preSkatt = []
Likviditetsgrad = []
Egenkapitalandel = []
Gjeldsgrad = []

driver = webdriver.Chrome()
driver.get("https://www.proff.no" + dummiestrings)





"""""

with open("twitterData.json", "w") as outfile:
    json.dump(tweetArr, outfile)

print("done")
"""
