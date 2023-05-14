import requests
import urllib
from bs4 import BeautifulSoup as bs4
import json
import os

class goodWill():
    

    def __init__(self):
        loc = requests.get("https://ipinfo.io/json")
        
        open("data.json","wb").write(loc.content)
        
        self.postal = json.load(open("data.json"))["postal"]
        
        os.remove("data.json")
        
        
    def setSearch(self, keywords):
        for char in keywords:
            if char == " ":
                return 404
            
        self.url = (f"https://shopgoodwill.com/categories/{keywords}")
        return self.url
        
    def getListings(self, keywords):
        searchPage = requests.get(self.setSearch(keywords))
        
        resultPage = bs4(searchPage.content, "html.parser")
        
        results = resultPage.find_all("a", class_ = "feat-item_name ng-star-inserted")
        
        for result in results:
            print("Listing found")
            print(result.get("title"))
            