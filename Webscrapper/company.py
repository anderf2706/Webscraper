import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from Redditscrapper import Redditscrapper
from Webscrapper import Keyvalues

companylist = []


class Company(object):
    def __init__(self, company):
        from Webscrapper import Keyvalues
        from importlib import reload
        reload(Keyvalues)
        self.company = str(company)
    def get_name(self):
        return self.company

    def generate_keyvalues(self):
        Keyvalues.generate_content_nokkel(self.company)
        Keyvalues.write_keyvalues()

    def gather_redditdata(self, reddittype):
        Redditscrapper.gather_data(self.company)



