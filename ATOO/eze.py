# coding: utf-8
from lxml import etree
import donneAtoo

# creaction d'un fichier xml avec iniation des données
def creationAtoo(url):
    tete = donneAtoo.nameJob(url)
    descapp = donneAtoo.AppaJob(url)
    desc = donneAtoo.descJob(url)
    tests = ""
    for des in desc:
        if des != '\xa0':
            tests = tests + '\n *' +str(des) 
    with open("Atoo.xml", 'wb') as f:
        site = etree.Element("Appo")
        job = etree.SubElement(site, "Job")
        jobTitle = etree.SubElement(job, "JobTitle")
        jobTitle.text = tete[0]
        view= etree.SubElement(job, "View")
        view.text = tete[1]
        entrepriseName= etree.SubElement(job, "EntrepriseName")
        entrepriseName.text = descapp[0]
        contries= etree.SubElement(job, "Contries")
        contries.text = descapp[2]
        recrutementDate= etree.SubElement(job, "RecrutementDate")
        recrutementDate.text = str(descapp[3]) + str(descapp[4])
        jobStatus= etree.SubElement(job, "JobStatus")
        jobStatus.text = descapp[5]
        description= etree.SubElement(job, "Description")
        description.text = tests
        obj = etree.tostring(site, pretty_print=True, xml_declaration=True, encoding='UTF-8')
        f.write(obj)

def updateAtoo(url):
    print('x')