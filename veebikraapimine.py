# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 08:09:56 2015

@author: risto.hinno
"""

#import BeautifulSoup
from bs4 import BeautifulSoup
import urllib2
#utf8 jaoks, et urle saaks loopida
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
#regrex
import re 
#esialgne
for i in range(1,2):
    url= "http://izzi.ee/catalog/category/Ettevõtted/page/%s" %i
    response=urllib2.urlopen(url)
    html=response.read()
    soup=BeautifulSoup(html)
    divclass2=soup.find_all("div", attrs={"class":"cat_result_description"})
    for i in divclass2:
        desc=i.get_text()
        listitem=desc.split(",")
        print listitem[0]+","+listitem[1]


#proovin koos e-mailiga ja aadressiga andmeid kätte saada 
file = open("newfile.txt", "w")
              
for i in range(1,2):
    url= "http://izzi.ee/catalog/category/Ettevõtted/page/%s" %i
    response=urllib2.urlopen(url)
    html=response.read()
    soup=BeautifulSoup(html)
    divclass2=soup.find_all("div", attrs={"class":"cat_result_description"})
    for i in divclass2:
        desc=i.get_text()
        listitem=desc.split(",")
        u=desc.encode("utf-8")
        if u.find("@")!=-1 and len(listitem)==4:
            file.write(listitem[0]+", "+listitem[1]+", "+\
            re.split("e-mail: ", u)[-1]+", "+listitem[2]+"\n")
        elif u.find("@")!=-1 and len(listitem)>4:
            file.write(listitem[0]+", "+listitem[1]+", "+\
            re.split("e-mail: ", u)[-1]+", "+listitem[2]+", "+\
            listitem[3]+"\n")
        elif u.find("@")==-1:
            file.write(listitem[0]+", "+listitem[1]+",     "+\
            ", "+listitem[2]+"\n")
            
file.close()

#vana ja töötab  
for i in range(1,2):
    url= "http://izzi.ee/catalog/category/Ettevõtted/page/%s" %i
    response=urllib2.urlopen(url)
    html=response.read()
    soup=BeautifulSoup(html)
    divclass2=soup.find_all("div", attrs={"class":"cat_result_description"})
    for i in divclass2:
        desc=i.get_text()
        listitem=desc.split(",")
        u=desc.encode("utf-8")
        if u.find("@")!=-1 and len(listitem)==4:
            print listitem[0]+","+listitem[1]+","+re.split("e-mail: ", u)[-1]+\
            ","+listitem[2]
        elif u.find("@")!=-1 and len(listitem)>4:
            print listitem[0]+","+listitem[1]+","+re.split("e-mail: ", u)[-1]+\
            ","+listitem[2]+","+listitem[3]
        elif u.find("@")==-1:
            print listitem[0]+","+listitem[1]+", "+\
            ","+listitem[2]
        
#lühemalt   
def andmed(soup):
    """soup->kirjutab listi txt faili
    annad sisse veebilehe soup ning tagastab listi ettevõtte nimest, 
    regkoodist ja aadressist, kirjutab selle txt faili
    Kirjutab andmeid faili selliselt:
    11914364, 2WAY OÜ
    11524002, 2WTEAM OÜ
    """
    divclass2=soup.find_all("div", attrs={"class":"cat_result_description"})
    for i in divclass2:
        desc=i.get_text()
        listitem=desc.split(",")
        #file.write(listitem[1]+", "+listitem[0]+"\n")
        file.write(listitem[0]+","+listitem[1]+"\n")
 
file = open("newfile.txt", "w")
for i in range(1,5):
    url= "http://izzi.ee/catalog/category/Ettevõtted/page/%s" %i
    response=urllib2.urlopen(url)
    html=response.read()
    soup=BeautifulSoup(html)
    andmed(soup)

file.close()




