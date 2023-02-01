import requests
from bs4 import BeautifulSoup

baseUrl =  "https://www.economist.com"
uri1 = "/mid-terms-2022"

response1 = requests.get(baseUrl + uri1)


#Scrape the data (title, link and small description of the articles from the economist concerning the US midterm politics)

def ecoProcess(soup):
    div = soup.findAll('div', {"class": ["css-1a74g8a e16rqvvr0", "css-1xnjxgi e16rqvvr0"]})
    print(len(div))
    for d in div:
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
            response2 = requests.get(newUrl)
            soup2 = BeautifulSoup(response2.text,'html.parser')
            time = soup2.find('time', {"class": "css-j5ehde e1fl1tsy0"})
            date = time.contents[2]
            try:
                p = d.find('p').get_text().strip()
                print(articleTitle, " - ", newUrl, " - ", p, " - ", date)  
                print()
            except:
                print(articleTitle, " - ", newUrl, " - ", date)
                print()
        except:
            pass
         
        

if response1.ok :
    soup = BeautifulSoup(response1.text,'html.parser')
    ecoProcess(soup)

