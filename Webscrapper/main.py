from Webscrapper import company


def generate_keyvalues_forlist():
    for element in company.companylist:
        element.generate_keyvalues()


company.companylist.append(company.Company('Yara Norge'))
company.companylist.append(company.Company('Equinor'))
company.companylist.append(company.Company('Norsk Hydro'))


generate_keyvalues_forlist()