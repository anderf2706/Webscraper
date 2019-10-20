import requests
from bs4 import BeautifulSoup
import json
import praw

redditBot = praw.Reddit()

result = requests.get("https://www.reddit.com/r/stocks/")
print(result.status_code)
print(result.headers)
src = result.content



content = BeautifulSoup(src, "html.parser")
tweetArr = []
for reddit in content.findAll('div', attrs={"style"}):
    redditobject = {

        """
        "author" : tweet.find("h2" , attrs={"class" : "author"}).get_text(),
        "tweet" : tweet.find("p", attrs={"class": "content"}).get_text(),
        "date" : tweet.find("h5", attrs={"class": "dateTime"}).get_text(),
        "likes" : tweet.find("p", attrs={"class": "Likes"}),
        "shares" : tweet.find("p", attrs={"class" : "Shares"})
        """
        "content": reddit.find("h3", attrs={"_eYtD2XCVieq6emjKBH3m"}).get_text()
    }
    print(redditobject)
    #tweetArr.append(redditobject)

with open("twitterData.json", "w") as outfile:
    json.dump(tweetArr, outfile)


print("done")


