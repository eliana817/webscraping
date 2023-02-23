import requests
from bs4 import BeautifulSoup
import csv    

class Toolkit:
    
    def createFile(fieldnames, rows, file):
        with open(file, 'w', encoding='UTF8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        return 