import requests
from bs4 import BeautifulSoup

class Tracklist:
    def __init__(self, url):
        self.url = url
        self.res = self.getHtml(url)
        self.title = self.findTitle(self.res)
        self.tags = self.findTags(self.res)
        

    def getHtml(self, url):
        """
        getHtml(self, url)
        parameter url expects string argument to be a link to a track on soundcloud.com

        Given the url, this function requests the html via python's requests package,
        and uses bs4 to make a BeautifulSoup Object to parse through later
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html5lib')
        return soup

    def findTitle(self, html):
        """
         Expects a bs4 object to be passed as html.
         parses through to return the title of the Soundcloud track in the given bs4 object.
        """
        try:
            title = html.find('a', attrs= {'itemprop':"url"})
            return title.text
        except:
            return None
    
    def findTags(self, html):
        """
         Expects a bs4 object to be passed as html.
         Parses through to return the tags of the Soundcloud track in the given bs4 object.
         Still a WOP -- can I get these without js...
        """
        tags = html.findAll('a', attrs={'class':"sc-tag sc-tag-medium"})
        return tags



    def __repr__(self):
        rep = f'Title: {self.title} \nTags: {self.tags}'
        return rep

new = Tracklist('https://soundcloud.com/derekd2music/jauz-hard-summer-2021')

print(new)


