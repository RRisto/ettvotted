# -*- coding: utf-8 -*-

#Versioon: 0.0.4
#Kuupaev: 05.10.2015

import urllib.request
import csv
from bs4 import BeautifulSoup



with open("data.csv","w", encoding="utf-8") as output_file:
    writer = csv.writer(output_file, delimiter="\t",quoting=csv.QUOTE_ALL)
    for i in range (1,5):
        url = "http://izzi.ee/catalog/category/Ettev%C3%B5tted/page/{}".format(i)
        response =urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        for i in soup.find_all("div", attrs={"class": "cat_result_description"}):
            listitem= i.get_text().split(",")
            row =[listitem[0],listitem[1],listitem[2]]
            writer.writerow([tulp.strip() for tulp in row])
            print (row)



