# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:55:24 2020

@author: Admin
"""
from bs4 import BeautifulSoup
import requests    
from selenium import webdriver
import re
import json


class Getting_information():
    
    def __init__(self, yakit, vites, arac_markasi,araclink):
        self.yakit = yakit
        self.vites = vites
        self.model_list = []
        self.value_list = []
        self.price_list = []
        self.date_list = []
        self.province_list = []
        self.id_list = []
        self.yakit_list = []
        self.vites_list = []
        self.arac_markasi = arac_markasi
        self.araclink = araclink
        self.marka_list = []

    def yakit_vites(self):
        headers_param = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
        #main_url = "https://www.sahibinden.com"
        url_list = [self.araclink, self.yakit, self.vites]
        url = "".join(url_list)
        r = requests.get(url, headers = headers_param)
        while True:
            
            soup = BeautifulSoup(r.content, "lxml")
            seri_model = soup.find_all("td", attrs ={"class":"searchResultsTagAttributeValue"})
            value =  soup.find_all("td", attrs ={"class":"searchResultsAttributeValue"})
            price =  soup.find_all("td", attrs ={"class":"searchResultsPriceValue"})
            date =  soup.find_all("td", attrs ={"class":"searchResultsDateValue"})
            province =  soup.find_all("td", attrs ={"class":"searchResultsLocationValue"})
            id2 = soup.find_all("tr", attrs ={"class":"searchResultsItem"})
            #sonraki = soup.find("a", attrs ={"class":"prevNextBut"}).get("href")
            
            
            for i in seri_model:
                a = i.text.strip()
                self.model_list.append(a)
                
            for i in value:
            
                a = i.text.strip()
                self.value_list.append(a)
            
            for i in price:
                a = i.text.strip()
                self.price_list.append(a)
            
            for i in date:
                a = i.text.strip()
                a = " ".join(a.split())
                self.date_list.append(a)
                
            for i in province:
                a = i.next_element.strip()
                self.province_list.append(a)
                
            for i in range(len(price)):
                if self.yakit == "/benzin":
                    self.yakit_list.append("Benzin")
                elif self.yakit == "/benzin-lpg":
                    self.yakit_list.append("Benzin & LPG")
                elif self.yakit == "/dizel" : 
                    self.yakit_list.append("Dizel")
                elif self.yakit == "/hybrid":
                    self.yakit_list.append("Hybrid")
                elif self.yakit == "/elektrik":
                    self.yakit_list.append("Elektrik")
                    
                if self.vites == "/manuel":
                    self.vites_list.append("Manuel")
                elif self.vites == "/yari-otomatik":
                    self.vites_list.append("Yarı Otomatik")
                elif self.vites == "/otomatik" :
                    self.vites_list.append("Otomatik")
                self.marka_list.append(self.arac_markasi)
            
# =============================================================================
#             for i in range(len(price)):
#                 self.yakit_list.append(self.yakit)
#                 self.vites_list.append(self.vites)
#                 self.marka_list.append(self.arac_markasi)
#                 
# =============================================================================
            for i in id2:
                a = i.get("data-id")
                if a == None:
                    pass
                else:
                    self.id_list.append(a)
                    
            try:
                sonraki = soup.find("a", attrs ={"title":"Sonraki"}).get("href")
                b = re.findall(r"[?]\w+[= / ? ,]*\w+",sonraki)
                url_list = [url, b[0]]
                new_url = "".join(url_list)
                r = requests.get(new_url, headers = headers_param)
                soup = BeautifulSoup(r.content, "lxml")
                
                continue
            except AttributeError:
                break
            
    def information_process(self):
        
        list2 = []
        list3 = []
        for i in range(len(self.value_list)):
            if len(list3) < 3:
                list3.append(self.value_list[i])
            elif len(list3) == 3:
                list2.append(list3)
                list3 = []
                list3.append(self.value_list[i])
        if len(list3) == 0:
            pass
        else:
            list2.append(list3)
        
        #Model List
        list4 = []
        list3 = []
        for i in range(len(self.model_list)):
            if len(list3) < 2:
                list3.append(self.model_list[i])
            elif len(list3) == 2:
                list4.append(list3)
                list3 = []
                list3.append(self.model_list[i])
        if len(list3) == 0:
            pass
        else:
            list4.append(list3)
        #Model list, id_list ve value list birleştirme
        
        for i in range(len(list4)):
            if len(list4[i]) == 1:
                
                list2[i].insert(0,list4[i][0])
                list2[i].insert(0,list4[i][0])
                list2[i].insert(0,self.marka_list[i])
                list2[i].insert(0, self.id_list[i])
            else:
                
                list2[i].insert(0, list4[i][1])
                list2[i].insert(0,list4[i][0])
                list2[i].insert(0,self.marka_list[i])
                list2[i].insert(0, self.id_list[i])
            
        
            
        
        #Vites List, yakit list 
        for i in range(len(self.vites_list)):
            list2[i].append(self.vites_list[i])
            list2[i].append(self.yakit_list[i])
          
        
        
        #Province 
        for i in range(len(self.province_list)):
            #a = re.findall(r"(\w+)",self.province_list[i])
            list2[i].append(self.province_list[i])
        
        #Date List
            
        
        for i in range(len(self.date_list)):
            if "\n" in self.date_list[i]:
                a = self.date_list[i].replace("\n"," ")
                list2[i].append(a)
            else:
                list2[i].append(self.date_list[i])
        #Price list
                
        for i in range(len(self.price_list)):
            list2[i].append(self.price_list[i])
        
        return list2
            
            
            
