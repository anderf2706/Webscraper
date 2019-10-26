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
    break
print(dummiestrings)

result_new = requests.get("https://www.proff.no" + dummiestrings)
driver = webdriver.Chrome()
driver.get("https://www.proff.no" + dummiestrings)


with open("twitterData.json", "w") as outfile:
    json.dump(tweetArr, outfile)

print("done")

