import requests
from bs4 import BeautifulSoup
import csv    

from EconomistEntry import EconomistEntry
from Economist import Economist
from Toolkit import Toolkit

from clean import *
import pandas as pd
import numpy as np
import re

class ToScrape:
    
    def __init__(self, instance, file):
        self.instance = instance
        self.file = file

    def soup(self, baseUrl, fieldnames):
        allLinks = {}
        allP = {}
        allDates = {}
        allTitles = {}
        response1 = requests.get(baseUrl)
        if response1.ok :
            soup = BeautifulSoup(response1.text,'html.parser')
            links, linkContent = self.instance.ecoLinks(soup)
        for link in links:
            contentIndex = links.index(link)
            content = linkContent[contentIndex]
            print("-" * 50," ", content," ", "-" * 50)
            print()
            response2 = requests.get(baseUrl + link)
            if response2.ok :
                soup2 = BeautifulSoup(response2.text,'html.parser')
                allLinks, allP, allDates, allTitles = self.instance.ecoProcess(soup2, content, allLinks, allP, allDates, allTitles)

        eco = EconomistEntry('id', 'theme', 'sourceUrl', 'articleLink', 'summary', 'date', 'title')
        rows = []
        h = 0
        id = 0
        for c in linkContent:
            i = 0 #index for the allLinks[c] list
            for k in range (len(allLinks[c])):
                rows = eco.dictEntry(rows, id, c, links, h, allLinks, i, allP, allDates, allTitles)

                i = i + 1
                id = id + 1
            h = h + 1

        print(rows)

        Toolkit.createFile(fieldnames, rows, self.file)

        data = pd.read_csv(self.file)
        duplicated = data.duplicated()
        dupl(duplicated, data, self.file)
        
        changeDateType(data, 'date')

        return self
    
    def exec(self):
        self.soup(self.instance.baseUrl, self.instance.fieldnames)
 
