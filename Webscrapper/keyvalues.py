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


def make_lists():
    lists = {'Basic': {}, 'Deluted': {}, 'Total_Revenue': {}, 'Cost_of_Revenue': {}, 'Gross_Profit': {},
             'Research_Development': {}, 'Selling_General_and_Administrative': {},
             'Total_Operating_Expenses': {}, 'Operating_Income_or_Loss': {}, 'Interest_Expense': {},
             'Total_Other_Income/Expenses_Net': {}, 'Income_Before_Tax': {},
             'Income_Tax_Expense': {}, 'Income_from_Continuing_Operations': {},
             'Net_Income': {}, 'Net_Income_available_to_common_shareholders': {}}
    return lists


def gather_all():
    list_of_dict = make_lists()
    print(list_of_dict)
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

                    for last2 in value:
                        last2 = str(last2)
                        if last2.__contains__('span'):
                            first = str(last2).split('>')[1]
                            nameofvalue = first.split('<')[0]
                            if nameofvalue == 'Operating Expenses' or nameofvalue == 'Reported EPS':
                                continue
                            print("navn " + nameofvalue)
                        if not last2.__contains__('button') and not last2.__contains__('span') \
                                and not nameofvalue == 'Basic' and not nameofvalue == 'Diluted':
                            number = last2.replace(',', '')
                            print("number", number)
                            nametosearch = nameofvalue.replace(' ', '_')
                            #list_of_dict[nametosearch][ar] = number

                                # if nametosearch == dict
                        # if nameofvalue == 'Basic' or nameofvalue == 'Diluted':

                    if not (valuestr.__contains__("div") or valuestr.__contains__("span")) and i < 6:
                        print('test', value)
                        # valuestr.replace(".", ",")
                        # try:
                        #    Basic[ar] = float(value)
                        # except ValueError:
                        #    Basic[ar] = None
                        # i += 1
                        # ar -= 1
                    if not (valuestr.__contains__("div") or valuestr.__contains__("span")) and i > 6:
                        print('test', value)
                        # valuestr.replace(".", ",")
                        # try:
                        #    Deluted[ar] = float(value)
                        # except ValueError:
                        #    Deluted[ar] = None
                        # i += 1
                        # ar -= 1

                    # if i == 0:
                    #   first = str(value).split('>')[1]
                    #  nameofvalue = first.split('<')[0]
                    # print(nameofvalue)
                    # i = 1
                    # else:
                    # print(str(value))
                    # print("hqllq")


generate_content_nokkel('AAPL')
gather_all()
