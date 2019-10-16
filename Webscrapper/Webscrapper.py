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
        "author" : tweet.find("h2" , attrs={"class" : "author"}.text.encode('utf-8')),
        "tweet" : tweet.find("p", attrs={"class": "content"}.text.encode("utf-8")),
        "date" : tweet.find("h5", attrs={"class": "dateTime"}.text.encode("utf-8")),
        "likes" : tweet.find("p", attrs={"class": "Likes"}.text.encode("utf-8")),
        "shares" : tweet.find("p", attrs={"class" : "Shares"}.text.encode("utf-8"))
    }
    tweetArr.append(tweetobject)
with open("twitterData.json", "w") as outfile:
    json.dump(tweetArr, outfile)


    #print(tweet.text.encode('utf-8'))
print("done")


