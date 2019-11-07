import requests
from bs4 import BeautifulSoup
import json

def generate_content_nokkel(company):
    global content_nokkel
    try:
        result_nokkeltall = requests.get("https://finance.yahoo.com/quote/"
                                         + str(company) + "/financials?p=" + str(company))
        src_nokkeltall = result_nokkeltall.content
        content_nokkel = BeautifulSoup(src_nokkeltall, "html.parser")
        print(result_nokkeltall)

    except:
        print('no key values available')


def get_Totalrentabilitet():
    ar = 2018
    totalrentabilitet = {}
    for element in content_nokkel.find('div', attrs={'class': 'D(tbr) fi-row Bgc($hoverBgColor):h'}):
        for first_block in element:
            for value in first_block:
                print(value)




generate_content_nokkel('NHY.OL')
get_Totalrentabilitet()

