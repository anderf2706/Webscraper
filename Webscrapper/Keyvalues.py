from Webscrapper import company



def get_Totalrentabilitet():
    ar = 2018
    totalrentabilitet = {}
    for element in company.content_nokkel.find('tr', attrs={'data-chart-title': 'Totalrentabilitet i %'}):
        for value in element:
            if "\n" not in value and isinstance(value, str):
                value = value.replace(",", ".")
                totalrentabilitet[int(ar)] = float(value)
                ar -= 1
    return totalrentabilitet

def get_Resultat_av_driften():
    ar = 2018
    resultat_av_driften = {}
    for element in company.content_nokkel.find('tr', attrs={'data-chart-title': 'Resultat av driften i %'}):
        for value in element:
            if "\n" not in value and isinstance(value, str):
                value = value.replace(",", ".")
                resultat_av_driften[int(ar)] = float(value)
                ar -= 1
    return resultat_av_driften

def get_Egenkapitalens_rentabilitet_før_skatt():
    ar = 2018
    egenkapitalens_rentabilitet_for_skatt = {}
    for element in company.content_nokkel.find('tr', attrs={'data-chart-title': 'Egenkapitalens rentabilitet før skatt i %'}):
        for value in element:
            if "\n" not in value and isinstance(value, str):
                value = value.replace(",", ".")
                egenkapitalens_rentabilitet_for_skatt[int(ar)] = float(value)
                ar -= 1
    return egenkapitalens_rentabilitet_for_skatt

def get_Likviditetsgrad():
    ar = 2018
    likviditetsgrad = {}
    for element in company.content_nokkel.find('tr', attrs={'data-chart-title': 'Likviditetsgrad'}):
        for value in element:
            if "\n" not in value and isinstance(value, str):
                value = value.replace(",", ".")
                likviditetsgrad[int(ar)] = float(value)
                ar -= 1
    return likviditetsgrad

def get_Egenkapitalandel():
    ar = 2018
    egenkapitalandel = {}
    for element in company.content_nokkel.find('tr', attrs={'data-chart-title': 'Egenkapitalandel i %'}):
        for value in element:
            if "\n" not in value and isinstance(value, str):
                value = value.replace(",", ".")
                egenkapitalandel[int(ar)] = float(value)
                ar -= 1
    return egenkapitalandel

def get_Gjeldsgrad():
    ar = 2018
    gjeldsgrad = {}
    for element in company.content_nokkel.find('tr', attrs={'data-chart-title': 'Gjeldsgrad'}):
        for value in element:
            if "\n" not in value and isinstance(value, str):
                value = value.replace(",", ".")
                gjeldsgrad[int(ar)] = float(value)
                ar -= 1
    return gjeldsgrad

