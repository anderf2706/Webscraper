import requests
from bs4 import BeautifulSoup

result = requests.get("http://ethans_fake_twitter_site.surge.sh/")
print(result.status_code)
print(result.headers)
src = result.content
print(src)

soup = BeautifulSoup(src, "html.parser")
for tweet in soup.findAll('p', attrs={"class": "content"}):
    print(tweet.text.encode('UTF-8'))
    dhe