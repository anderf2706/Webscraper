import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from Redditscrapper import Redditscrapper
from Webscrapper import keyvalues
import os
import googlesearch


class Company(object):
    def __init__(self, company):
        from Webscrapper import OLD_Keyvalues
        from importlib import reload
        reload(OLD_Keyvalues)
        self.company = str(company)
        self.ticker = self.generate_ticker()
        self.ensure_dir()

    def ensure_dir(self):
        if not (os.path.exists('Companies/' + self.get_name())):
            os.makedirs('Companies/' + self.get_name())

    def get_name(self):
        return self.company

    def generate_ticker(self):
        global url
        for url in googlesearch.search("Yahoo finance" + self.get_name() + "Ticker", stop=1):
            url = str(url)

            print(url)
            try:
                url = url.split('=')[1]
            except IndexError:
                url = url.split('/')[4]
                print(url)

            break
        return url

    def get_ticker(self):
        return self.ticker

    def generate_keyvalues(self):
        keyvalues.write_keyvalues(self.get_name(), self.get_ticker())

