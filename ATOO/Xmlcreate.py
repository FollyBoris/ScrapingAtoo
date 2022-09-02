# coding: utf-8
from random import randint
from lxml import etree
import donneAtoo
# creaction d'un fichier xml avec iniation des données
def creationAtoo(url):
    tete = donneAtoo.nameJob(url)
    descapp = donneAtoo.AppaJob(url)
    desc = donneAtoo.descJob(url)
    tests = ""
    tesa = ""
    for desq in descapp:
        if desq != '':
            tesa = tesa + '   ' +str(desq) 
    for des in desc:
        if des != '\xa0':
            tests = tests + '\n *' +str(des) 
    with open("Atoo.xml", 'wb') as f:
        site = etree.Element("Appo"+str(randint(1, 300)))
        job = etree.SubElement(site, "Job")
        jobTitle = etree.SubElement(job, "JobTitle")
        jobTitle.text = tete[0]
        view= etree.SubElement(job, "View")
        view.text = tete[1]
        entrepriseName= etree.SubElement(job, "EntrepriseInfo")
        entrepriseName.text = tesa
        description= etree.SubElement(job, "Description")
        description.text = tests
        obj = etree.tostring(site, pretty_print=True, xml_declaration=True, encoding="utf-8")
        f.write(obj)

def updateAtoo(url):
    tete = donneAtoo.nameJob(url)
    descapp = donneAtoo.AppaJob(url)
    desc = donneAtoo.descJob(url)
    tests = ""
    tesa = ""
    for desq in descapp:
        if desq != '':
            tesa = tesa + '   ' +str(desq) 
    for des in desc:
        if des != '\xa0':
            tests = tests + '\n *' +str(des) 
    with open("Atoo.xml", 'ab') as f:
        site = etree.Element("Appo"+str(randint(1, 300)))
        job = etree.SubElement(site, "Job")
        jobTitle = etree.SubElement(job, "JobTitle")
        jobTitle.text = tete[0]
        view= etree.SubElement(job, "View")
        view.text = tete[1]
        entrepriseName= etree.SubElement(job, "EntrepriseInfo")
        entrepriseName.text = tesa
        description= etree.SubElement(job, "Description")
        description.text = tests
        obj = etree.tostring(site, pretty_print=True, encoding="utf-8")
        f.write(obj)
