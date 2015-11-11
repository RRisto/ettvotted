# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:01:57 2015

@author: Risto
"""
import os
os.chdir(r"C:\Users\Risto\Documents\GitHub\GeoJson--riregistri-andmetest")

import pandas
from geopy.geocoders import Nominatim
import requests
import json
import time
import numpy as np

data=pandas.read_csv("maaamet_arireg.csv", sep=";", encoding="latin-1")
#vaja teha ainult esimesele sisselugemisel
#data["aadressid"] = data["asukoht_ettevotja_aadressis"]+","+data["asukoha_ehak_tekstina"]
#data["viitepunkt_y"]=""
#data["viitepunkt_x"]=""
#data["taisaadress"]=""

#
alguskoht=len(data["viitepunkt_y"])-data["viitepunkt_y"].isnull().sum()
#for i in range(alguskoht,len(data["aadressid"])):
for i in range(alguskoht,20):    
        url = "http://inaadress.maaamet.ee/inaadress/gazetteer?address="+data["aadressid"][i]
        r = requests.get(url)
        j = r.content
        json_str = j.decode("utf-8")
        parsed_json = json.loads(json_str)
        try:
            adresses = parsed_json["addresses"][0]
            url="http://www.maaamet.ee/rr/geo-lest/url/?xy="+adresses["viitepunkt_x"]+","+ adresses["viitepunkt_y"]
            try:            
                j = requests.get(url).content.decode("utf-8")
                data["viitepunkt_x"][i]=j.split(",")[0]
                data["viitepunkt_y"][i]=j.split(",")[1]
                data["taisaadress"][i] = adresses["taisaadress"]
                #row = (x+";"+y+";"+taisaadress)
                #output.write(row+"\n")
            except:
                #row = ("NA"+";"+"NA"+";"+taisaadress)
                #output.write(row+"\n")
                data["viitepunkt_x"][i]="NA"
                data["viitepunkt_y"][i]="NA"
                data["taisaadress"][i]="NA"
                continue
        except:
            data["viitepunkt_x"][i]="NA"
            data["viitepunkt_y"][i]="NA"
            data["taisaadress"][i]="NA"
            continue
        


#saveime
data.to_csv("maaamet_arireg.csv", sep=";")

