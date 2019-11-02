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
        result_nokkeltall = requests.get(Keyvalues.get_to_side(self.company))
        src_nokkeltall = result_nokkeltall.content
        global content_nokkel
        content_nokkel = BeautifulSoup(src_nokkeltall, "html.parser")

    def generate_keyvalues(self):
        Keyvalues.write_keyvalues()

    def gather_redditdata(self, reddittype):
        Redditscrapper.gather_data(self.company)



