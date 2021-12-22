import requests as r
from bs4 import BeautifulSoup as BS

surl = "https://steamcommunity.com/sharedfiles/filedetails/?id="
print("Введите ID коллекции:")
wsc = input()

for el in BS(r.get(surl + wsc).content, "html.parser").select(".collectionItem"):
    print("resource.AddWorkshop('" + el.find("a").attrs["href"].replace(surl, "") + "')" + " -- " + el.select(".collectionItemDetails a")[0].text + " -- by " + el.select(".collectionItemDetails .workshopItemAuthorName a")[0].text)