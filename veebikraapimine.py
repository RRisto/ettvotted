# -*- coding: utf-8 -*-

#Versioon: 0.0.4
#Kuupaev: 05.10.2015

import urllib.request
import csv
from bs4 import BeautifulSoup
import time
def abifunktsioon(kanal):
    """kanal(str)->str (kui vastav kanal olemas siis listist listitem tagastab
    vastava elemendi (kanali) väärtuse, muidu tagastab tühja stringi " ")
    """
    if len([s for s in listitem if kanal in s])!=0:
        return listitem.pop(listitem.index("".join([s for s in listitem if kanal in s])))
    else:
        return" "

with open("data.csv","w", encoding="utf-8") as output_file:
    writer = csv.writer(output_file, delimiter="\t",quoting=csv.QUOTE_ALL)
    for i in range (6,1000000):
        url = "http://izzi.ee/catalog/category/Ettev%C3%B5tted/page/{}".format(i)
        time.sleep(1)
        response =urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        for i in soup.find_all("div", attrs={"class": "cat_result_description"}):
            desc=i.get_text()
            listitem=desc.split(",") #teeb tekstist listi
            print (listitem)
            #ükshaaval kirjutab elemendid faili ja eemaldab listist
            row = [listitem.pop(0),listitem.pop(0),abifunktsioon("e-mail:"), abifunktsioon("tel:"), \
            abifunktsioon("www."),"".join(listitem),url]
            writer.writerow([tulp.strip() for tulp in row])
            #print (row)



