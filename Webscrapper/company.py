import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from Redditscrapper import Redditscrapper
from Webscrapper import keyvalues

companylist = []


class Company(object):
    def __init__(self, company, yahooticker):
        from Webscrapper import OLD_Keyvalues
        from importlib import reload
        reload(OLD_Keyvalues)
        self.company = str(company)
        self.ticker = str(yahooticker)
    def get_name(self):
        return self.company

    def generate_keyvalues(self):
        keyvalues.generate_content_nokkel(self.ticker)
        keyvalues.write_keyvalues()

    def gather_redditdata(self, reddittype):
        Redditscrapper.gather_data(self.company)



