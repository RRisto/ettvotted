# -*- coding: utf-8 -*-
import pandas
from geopy.geocoders import Nominatim
import requests
import json
import time

data = pandas.read_csv('list.csv',sep=";",encoding="utf-8")
aadressid = data["asukoht_ettevotja_aadressis"]+","+data["asukoha_ehak_tekstina"]
with open("test.txt","w") as output:
    for aadress in aadressid:
        url = "http://inaadress.maaamet.ee/inaadress/gazetteer?address="+aadress
        r = requests.get(url)
        j = r.content
        json_str = j.decode("utf-8")
        parsed_json = json.loads(json_str)
#siia vahele tuleb try teha
        adresses = parsed_json["addresses"][0]
        y = adresses["viitepunkt_y"]
        x = adresses["viitepunkt_x"]
        taisaadress = adresses["taisaadress"]
        row = (x+";"+y+";"+taisaadress)
        output.write(row+"\n")
        time.sleep(1)