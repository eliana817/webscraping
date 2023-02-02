import requests
from bs4 import BeautifulSoup

baseUrl =  "https://www.economist.com"

response1 = requests.get(baseUrl)


#Scrape the data (title, link and small description of the articles from the economist concerning the US midterm politics)

def ecoProcess(soup, content):
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
                except:
                    print(articleTitle, " - ", newUrl, " - ", date)
                    print()
            except:
                pass
        except:
            pass


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
    return links, linkContent
            

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
            ecoProcess(soup2, content)

