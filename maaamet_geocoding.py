# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:01:57 2015

@author: Risto
"""
import os
os.chdir(r"C:\Users\Risto\Documents\Python ettevõtted\ettevõtted geocoding")

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

#määrame koha, kust loopimine pooleli jäi
alguskoht=data["viitepunkt_y"].last_valid_index()+1
#alustame loopimist
for i in range(alguskoht,20000):    
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
                data.loc[i,"viitepunkt_x"]=j.split(",")[0]
                data.loc[i,"viitepunkt_y"]=j.split(",")[1]
                data.loc[i, "taisaadress"] = adresses["taisaadress"]
                print(i, adresses["taisaadress"])
            except:
                data.loc[i,"viitepunkt_x"]="NA"
                data.loc[i,"viitepunkt_y"]="NA"
                data.loc[i, "taisaadress"]="NA"
                print(i, data["taisaadress"][i])
                continue
        except:
            data.loc[i,"viitepunkt_x"]="NA"
            data.loc[i,"viitepunkt_y"]="NA"
            data.loc[i, "taisaadress"]="NA"
            print(i, data["taisaadress"][i])
            continue
        

#saveime
data.to_csv("maaamet_arireg.csv", sep=";")
