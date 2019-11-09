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


def gather_all():
    indexes = ['D(tbr) fi-row Bgc($hoverBgColor):h'
               ]
    
    for i in range(0, len(indexes)):
        ar = 2018
        totalrentabilitet = {}
        i = 0
        for element in content_nokkel.find('div', attrs={'class': 'D(tbr) fi-row Bgc($hoverBgColor):h'}):
            nameofvalue = str
            for first_block in element:
                for value in first_block:
                    if i == 0:
                        first = str(value).split('>')[1]
                        nameofvalue = first.split('<')[0]
                        print(nameofvalue)
                        i = 1
                    else:
                        print(str(value))


generate_content_nokkel('GOOGL')
gather_all()

