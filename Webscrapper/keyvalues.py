import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path

def generate_content_nokkel(company):
    try:
        result_nokkeltall = requests.get("https://finance.yahoo.com/quote/"
                                         + str(company) + "/financials?p=" + str(company))
        print(str(company))
        src_nokkeltall = result_nokkeltall.content

        return BeautifulSoup(src_nokkeltall, "html.parser")
    except:
        print('no key values available')
        return None


def make_lists():
    lists = {'Basic': {}, 'Diluted': {}, 'Total_Revenue': {}, 'Cost_of_Revenue': {}, 'Gross_Profit': {},
             'Research_Development': {}, 'Selling_General_and_Administrative': {},
             'Total_Operating_Expenses': {}, 'Operating_Income_or_Loss': {}, 'Interest_Expense': {},
             'Total_Other_Income/Expenses_Net': {}, 'Income_Before_Tax': {},
             'Income_Tax_Expense': {}, 'Income_from_Continuing_Operations': {},
             'Net_Income': {}, 'Net_Income_available_to_common_shareholders': {}, 'EBITDA': {}}
    return lists


def gather_all(company):
    list_of_dict = make_lists()
    print(list_of_dict)
    indexes = ['D(tbr) fi-row Bgc($hoverBgColor):h',
               ]
    content_nokkel = generate_content_nokkel(company)

    ar = 2019
    for i in range(0, len(indexes)):
        for element in content_nokkel.findAll('div', attrs={'class': 'D(tbr) fi-row Bgc($hoverBgColor):h'}):
            nameofvalue = str
            for first_block in element:
                i = 0
                for value in first_block:

                    valuestr = str(value)

                    for last2 in value:
                        last2 = str(last2)
                        if last2.__contains__('span'):
                            first = str(last2).split('>')[1]
                            nameofvalue = first.split('<')[0]
                            if nameofvalue == 'Operating Expenses' or nameofvalue == 'Reported EPS'\
                                    or nameofvalue == 'Weighted average shares outstanding':
                                continue
                            print("navn " + nameofvalue)
                        if not last2.__contains__('button') and not last2.__contains__('span') \
                                and not nameofvalue == 'Basic' and not nameofvalue == 'Diluted':
                            try:
                                number = int(last2.replace(',', ''))

                            except ValueError:
                                number = None
                            print("number", number)
                            nametosearch = nameofvalue.replace(' ', '_')
                            if ar < 2015:
                                ar = 2019
                            list_of_dict[nametosearch][ar] = number
                            ar -= 1

                    if not (valuestr.__contains__("div") or valuestr.__contains__("span")) and i < 12:
                        if valuestr.__contains__('-'):
                            basicvalue = None
                        else:
                            basicvalue = float(valuestr)
                        print('test', basicvalue, nameofvalue)
                        nametosearch = nameofvalue.replace(' ', '_')
                        if ar < 2015:
                            ar = 2019
                        list_of_dict[nametosearch][ar] = basicvalue
                        i += 1
                        ar -= 1
    return list_of_dict


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def write_keyvalues(name, yahooticker):
    keyvaldict = gather_all(yahooticker)
    selskapforjson = name
    with open("Companies/" + selskapforjson + "/" + selskapforjson +
              "_keyvalues.json", "w") as outfile:
        json.dump(keyvaldict, outfile)


