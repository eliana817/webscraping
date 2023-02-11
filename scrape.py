import requests
from bs4 import BeautifulSoup
import csv

baseUrl =  "https://www.economist.com"

response1 = requests.get(baseUrl)

allLinks = {}
allP = {}
allDates = {}
allTitles = {}

#Scrape the data (title, link and small description of the articles from the economist concerning the US midterm politics)

def ecoProcess(soup, content, allLinks, allP, allDates, allTitles):
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
                articleTitle = a.contents[1]
            elif len(a) == 1:
                articleTitle = a.contents[0]
            else:
                articleTitle = a.contents[2]
        
            try:
                newUrl = baseUrl + a['href']
                date = ecoDate(newUrl)
                try:
                    currentDiv = d
                    p = ecoP(currentDiv)
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


def ecoDate(url):     
    response2 = requests.get(url)
    soup2 = BeautifulSoup(response2.text,'html.parser')
    time = soup2.find('time', {"class": "css-j5ehde e1fl1tsy0"})
    date = time.contents[2]
    return date

def ecoP(div):
    p = div.find('p').get_text().strip()
    return p

def ecoLinks(soup):
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
            

if response1.ok :
    soup = BeautifulSoup(response1.text,'html.parser')
    links, linkContent = ecoLinks(soup)
    for link in links:
        contentIndex = links.index(link)
        content = linkContent[contentIndex]
        print("-" * 50," ", content," ", "-" * 50)
        print()
        response2 = requests.get(baseUrl + link)
        if response2.ok :
            soup2 = BeautifulSoup(response2.text,'html.parser')
            allLinks, allP, allDates, allTitles = ecoProcess(soup2, content, allLinks, allP, allDates, allTitles)
            

rows = []
h = 0
id = 0
for c in linkContent:
    i = 0 #index for the allLinks[c] list
    for k in range (len(allLinks[c])):
        row = {}
        row['id'] = id
        row['theme'] = c
        row['sourceUrl'] = links[h]

        row['articleLink'] = allLinks[c][i]           
        row['summary'] = allP[c][i]           
        row['date'] = allDates[c][i]       
        row['title'] = allTitles[c][i]
            
        rows.append(row)
        i = i + 1
        id = id + 1
    h = h + 1

print(rows)

fieldnames = ['id', 'theme', 'sourceUrl', 'articleLink', 'summary', 'date', 'title']
with open('file.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

    
    

