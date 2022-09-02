import time
import requests
from bs4 import BeautifulSoup
import scrapLink
import scrapAtooAcc
from Xmlcreate import *

url1 = 'http://www.atoo.ci'

if __name__ == '__main__':
    url2 = scrapAtooAcc.rechercheEmploiHref(url1)
    url3 = scrapAtooAcc.rechercheJob(url2)
    url4 = scrapLink.liensVoirPlus(url3)
    url5 = scrapLink.pageAnexe(url3)
    for url in url4:
        if url != "" and url!= " ":
            tit = "Atoo.xml"
            try:
                with open(tit):
                    print('a')
                    updateAtoo(url)
            except IOError:
                print('b')
                creationAtoo(url)
    for url in url5:
        if url != "" and url!= " ":
            tit = "Atoo.xml"
            try:
                with open(tit):
                    print('a')
                    updateAtoo(url)
            except IOError:
                print('b')
                creationAtoo(url)
else:
    print('Erreur')