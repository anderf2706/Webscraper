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
    Basic = {}
    Deluted = {}
    Total_revenue = {}
    Cost_of_revenue = {}
    Gross_profit = {}
    Research_development = {}
    Selling_general_Administrativ ={}
    Total_operating_expenses = {}
    Operating_income_or_loss = {}
    Interest_expenses = {}
    Total_other_income_or_expenses_net = {}
    Income_before_tax = {}
    Income_tax_expenses = {}
    Income_from_Continuing_Operations = {}


    indexes = ['D(tbr) fi-row Bgc($hoverBgColor):h',
               ]

    for i in range(0, len(indexes)):
        ar = 2018
        for element in content_nokkel.findAll('div', attrs={'class': 'D(tbr) fi-row Bgc($hoverBgColor):h'}):
            nameofvalue = str
            for first_block in element:
                for value in first_block:
                    valuestr = str(value)
                    ar = 2018
                    i = 0
                    #if not value.__contains__("div") and not value.__contains__("span") and i < 6:
                    #    valuestr.replace(".", ",")
                    #    try:
                    #        Basic[ar] = float(value)
                    #    except ValueError:
                    #        Basic[ar] = None
                    #    i += 1
                    #    ar -= 1
                    #if not value.__contains__("div") and not value.__contains__("span") and i > 6:
                    #    valuestr.replace(".", ",")
                    #    try:
                    #        Deluted[ar] = float(value)
                    #    except ValueError:
                    #        Deluted[ar] = None
                    #    i += 1
                    #    ar -= 1
                    #
                    for last2 in value:
                        last2 = str(last2)
                        if last2.__contains__('span'):
                            first = str(last2).split('>')[1]
                            nameofvalue = first.split('<')[0]
                            print("navn " + nameofvalue)
                        if not last2.__contains__('button') and not last2.__contains__('span')\
                                and not nameofvalue == 'Basic' and not nameofvalue == 'Diluted':
                            last2.replace(',', '')
                            print("number" + str(last2))
                        if not nameofvalue == 'Basic' and not nameofvalue == 'Diluted':



                    #if i == 0:
                     #   first = str(value).split('>')[1]
                      #  nameofvalue = first.split('<')[0]
                       # print(nameofvalue)
                        #i = 1
                    #else:
                    #print(str(value))
                    #print("hqllq")
    print(Basic)
    print(Deluted)

generate_content_nokkel('AAPL')
gather_all()

