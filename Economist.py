import requests
from bs4 import BeautifulSoup
import csv
from EconomistEntry import EconomistEntry
from Toolkit import Toolkit

class Economist:

    def __init__(self, baseUrl, fieldnames):
        self.baseUrl = baseUrl
        self.fieldnames = fieldnames

        #Scrape the data (title, link and small description of the articles from the economist concerning the US midterm politics)
    def ecoProcess(self, soup, content, allLinks, allP, allDates, allTitles):
        allLinks[content] = []
        allP[content] = []
        allDates[content] = []
        allTitles[content] = []
        div = soup.findAll('div', {"class": ["css-1a74g8a e16rqvvr0", "css-1xnjxgi e16rqvvr0", "css-mi70rv e16rqvvr0"]})
        #print(len(div))
        for d in div:
            
            try:
                h3 = d.find('h3')
                a = h3.find('a')
                
                if len(a) == 2 :
                    articleTitle = a.contents[1] #or a.getText()
                elif len(a) == 1:
                    articleTitle = a.contents[0]
                else:
                    articleTitle = a.contents[2]
            
                try:
                    newUrl = self.baseUrl + a['href']
                    date = self.ecoDate(newUrl)
                    try:
                        currentDiv = d
                        p = self.ecoP(currentDiv)
                        print(articleTitle, " - ", newUrl, " - ", p, " - ", date)  
                        print()
                        allLinks[content].append(newUrl)
                        allP[content].append(p)
                        allDates[content].append(date)
                        allTitles[content].append(articleTitle)
                    except:
                        print(articleTitle, " - ", newUrl, " - ", date)
                        print()
                        allLinks[content].append(newUrl)
                        allP[content].append(None)
                        allDates[content].append(date)
                        allTitles[content].append(articleTitle)
                except:
                    pass
            except:
                pass
        return allLinks, allP, allDates, allTitles

    def ecoDate(self, url):     
        response2 = requests.get(url)
        soup2 = BeautifulSoup(response2.text,'html.parser')
        time = soup2.find('time', {"class": "css-j5ehde e1fl1tsy0"})
        date = time.contents[2]
        return date

    def ecoLinks(self, soup):
        links = []
        linkContent = []
        theme = soup.findAll('ul', {'class': ['ds-navigation-list-items--section', 'is-selected', '']})
        for t in theme:
            a = t.findAll('a')
            for a in a:
                uri = a['href']
                links.append(uri)
                span = a.find('span')
                linkContent.append(span.contents[0])
        return links, linkContent #links of the navbar
    
    def ecoP(self, div):
        p = div.find('p').get_text().strip()
        return p
    
        