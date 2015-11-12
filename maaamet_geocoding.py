# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 18:47:37 2015

@author: Risto
"""
import os
os.chdir(r"C:\Users\Risto\Documents\Python Scripts")
#geokodeerimine maa-ameti rakenduse kaudu
import pandas as pd
data=pd.read_csv("31_10_2015_arireg.csv", sep=";", encoding="latin-1")

#liidan aadressi ühte lahtrisse kokku
data["kogu_aadress"]=data["asukoht_ettevotja_aadressis"]+" "+\
data["asukoha_ehak_tekstina"]
#loobin läbi ja lisan longi ja lati
import requests
import json
aadressid=data["kogu_aadress"][1:3]
for i in range(0,len(data["kogu_aadress"])):
for i in range(0,5):   
    aadress=data["kogu_aadress"][i]
    url="http://inaadress.maaamet.ee/inaadress/gazetteer?callback=v&appartment=1&address="+\
    aadress
    cont=requests.get(url).content.decode("utf-8")
    cont=str(cont).strip("'<>( ) 'v") #muidu ei saa aru, et on json
    parsedJson=json.loads(cont)
    data["lat"][i]=parsedJson["addresses"][0]["viitepunkt_y"]
    data["lon"][i]=parsedJson["addresses"][0]["viitepunkt_x"]
    
    

    
 