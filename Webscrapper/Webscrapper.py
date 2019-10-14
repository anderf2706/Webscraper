import requests
import bs4
from bs4 import BeautifulSoup


result = requests.get("https://www.google.com/")
print(result.status_code)
print(result.headers)
src = result.content
print(src)
