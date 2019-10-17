import requests
from bs4 import BeautifulSoup
import json

result = requests.get("http://ethans_fake_twitter_site.surge.sh/")
print(result.status_code)
print(result.headers)
src = result.content

content = BeautifulSoup(src, "html.parser")
tweetArr = []
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetobject = {
        "author" : tweet.find("h2" , attrs={"class" : "author"}).get_text(),
        "tweet" : tweet.find("p", attrs={"class": "content"}).get_text(),
        "date" : tweet.find("h5", attrs={"class": "dateTime"}).get_text(),
        "likes" : tweet.find("p", attrs={"class": "Likes"}),
        "shares" : tweet.find("p", attrs={"class" : "Shares"})
    }
    print(tweetobject)

with open("twitterData.json", "w") as outfile:
    json.dump(tweetArr, outfile)


print("done")


