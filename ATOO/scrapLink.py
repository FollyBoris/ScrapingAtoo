import time
import requests
from bs4 import BeautifulSoup
import scrapAtooAcc
import re

#The first page link recuperation

def liensVoirPlus(url):
    print(1)
    links = []
    reponse = requests.get(url)
    if reponse.ok :
        soup = BeautifulSoup(reponse.text, 'html.parser')
        baliseA = soup.find_all('a', class_= 'btn btn-primary')
        
        for balise in baliseA:    
            link = balise['href']
            if url in link:
                links.append(link)
    return links

#All page can permit to acces the differntes description of the djob

def pageAnexe(url):
    print(2)
    links = []
    for i in range(2, 21, 1):       
        newLink = url + 'page/' + str(i) +'/'
        reponse = requests.get(newLink)
        if reponse.ok :
           soup = BeautifulSoup(reponse.text, 'html.parser')
        baliseA = soup.find_all('a', class_= 'btn btn-primary')
            
        for balise in baliseA:    
            link = balise['href']
            if url in link:
                linka = str(link)+ '\n'
                links.append(linka)
    return links


