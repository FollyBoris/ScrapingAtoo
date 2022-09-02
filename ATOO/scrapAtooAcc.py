import time
import requests
from bs4 import BeautifulSoup

# recherhceEmploiHref fonction permit me to search Employ page link on the website
def rechercheEmploiHref(url):
    print(3)
    reponse = requests.get(url)
    if reponse.ok :
        soup = BeautifulSoup(reponse.text, 'lxml')
        baliseA = soup.findAll('a')
        
        for balisea in baliseA:
            if balisea.text == 'Emploi':
                link = balisea['href']
                
                return link
            else:   
                time.sleep(0)
# recherche the page where all jobs are present
def rechercheJob(url):
    print(4)
    reponse = requests.get(url)
    if reponse.ok :
        soup = BeautifulSoup(reponse.text, 'lxml')
        baliseA = soup.findAll('a')
        
        for balisea in baliseA:
            if balisea.text == 'Emplois':
                link = balisea['href']             
                return link