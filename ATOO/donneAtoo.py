from subprocess import TimeoutExpired
import time
import requests
from bs4 import BeautifulSoup

def nameJob(url):
    reponse = requests.get(url)
    liste=[]
    if reponse.ok :
        soup = BeautifulSoup(reponse.text, 'html.parser')
        tt = soup.find('h1', class_='page-title')
        tr = tt.get_text().replace('\n', "\t")
        titres = tr.split("\t")
    for titre in titres:
        if titre != '' and titre != ' ':
            liste.append(titre)
    return liste
# Here is a name of apparution description and Entreprise name

def AppaJob(url):
    reponse = requests.get(url)
    liste = []
    if reponse.ok :
        soup = BeautifulSoup(reponse.text, 'html.parser')
        span = soup.find('p', class_='content-meta')
        sp = span.get_text().replace('\n', "\t")
        spans = sp.split("\t")     
    for spa in spans:
        if spa != '' and spa != ' ':
            liste.append(spa)
    return liste
# Description par of Job
def descJob(url):    
    reponse = requests.get(url)
    liste = []
    if reponse.ok :
        soup = BeautifulSoup(reponse.text, 'html.parser')
        balise = soup.find('div', class_= 'job-desc')
        contenue = balise.get_text().replace('\n', '\t')
        contenues =contenue.split("\t")
    for conten in contenues:
        if conten != '' and conten != ' ':
            liste.append(conten)
    return liste
