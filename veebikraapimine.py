# -*- coding: utf-8 -*-

#Versioon: 0.0.6
#Kuupaev: 21.10.2015

import urllib.request
import csv
from bs4 import BeautifulSoup
import time
import re
with open("data.csv","w", encoding="utf-8") as output_file:
    writer = csv.writer(output_file, delimiter="\t",quoting=csv.QUOTE_ALL)
    for i in range (2219,2802):
        url = "http://izzi.ee/catalog/category/Ettev%C3%B5tted/page/{}".format(i)
        time.sleep(1)
        response =urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        for i in soup.find_all("div", attrs={"class": "cat_result_description"}):
            desc=i.get_text()
            listitem=desc.split(",") #teeb tekstist listi
            try:

                nimi = listitem[0]
                regkood = listitem[1]
                email = re.findall(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?",desc)
                emailclean = ",".join(email)
                telefon372 = re.findall("3725\d{6,7}",desc)
                telefon372clean = ",".join(telefon372)
                telefon = re.findall("5\d{6,7}",desc)
                telefonclean = ",".join(telefon)
                aadress = re.findall('1\d{7},\s(.*?)tel:|1\d{7},\s(.*?)e-mail:|1\d{7},\s(.*?)$',desc)
                aadressclean= "".join(aadress[0])
            except:
                print ("error: ")
            row = (nimi,regkood,aadressclean,emailclean,telefonclean,telefon372clean,url)

            writer.writerow([tulp.strip() for tulp in row])
            try:
                print (row)
            except:
                print ("Error printimisel")

