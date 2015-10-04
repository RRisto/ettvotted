# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 08:09:56 2015

@author: risto.hinno
"""
#Python 3.4.3
from bs4 import BeautifulSoup
import urllib.request

#avab tühja faili, loobib läbi URLid ning kirjutab faili ettevõtte nime,
# regkoodi, e-maili, telefoni, kodulehe ja aadressi 
fail = open("ettevotted.txt", "w")
for i in range(1,3):
    url= "http://izzi.ee/catalog/category/Ettev%%C3%%B5tted/page/%s" %i    
    response=urllib.request.urlopen(url)   
    html=response.read()
    soup=BeautifulSoup(html)
    divclass=soup.find_all("div", attrs={"class":"cat_result_description"})
    for i in divclass:
        desc=i.get_text() 
        listitem=desc.split(",") #teeb tekstist listi
        #ükshaaval kirjutab elemendid faili ja eemaldab listist
        fail.write(listitem.pop(0) + ", " + listitem.pop(0) + ", " +\
        abifunktsioon("e-mail:") + ", " + abifunktsioon("tel:") + ", " +\
        abifunktsioon("www.") + ", " + "".join(listitem) + "\n")
 
fail.close()
                 
def abifunktsioon(kanal):
    """kanal(str)->str (kui vastav kanal olemas siis listist listitem tagastab 
    vastava elemendi (kanali) väärtuse, muidu tagastab tühja stringi " ") 
    """
    if len([s for s in listitem if kanal in s])!=0: 
        return listitem.pop(listitem.index("".join([s for s in listitem if kanal in s])))
    else:
        return" "
          
        
            
