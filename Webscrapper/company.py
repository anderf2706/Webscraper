import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from Redditscrapper import Redditscrapper
from Webscrapper import keyvalues


class Company(object):
    def __init__(self, company, yahooticker):
        from Webscrapper import OLD_Keyvalues
        from importlib import reload
        reload(OLD_Keyvalues)
        self.company = str(company)
        self.ticker = str(yahooticker)

    def get_name(self):
        return self.company

    def get_ticker(self):
        return self.ticker

    def generate_keyvalues(self):
        keyvalues.write_keyvalues(self.get_name(), self.get_ticker())




