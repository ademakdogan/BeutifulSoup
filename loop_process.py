# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:48:00 2020

@author: Admin
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from requests.exceptions import ConnectionError
import time
from selenium.webdriver.common.action_chains import ActionChains
from tqdm import tqdm
import beautifulsoup_getting_information as bf
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException,ElementClickInterceptedException
import requests
from bs4 import BeautifulSoup


class Loop_process():
    
    def bf_loop(self):
        
        t0 = time.time()
        final_list = []
        
        headers_param = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
        url = 'https://www.sahibinden.com/otomobil'
        r = requests.get(url, headers = headers_param)
        
        r.content
        r.status_code
        
        soup = BeautifulSoup(r.content, "lxml")
        araba_isim = soup.find_all("li" ,attrs = {"class": "cl2"})
        arac_list = []
        araclink_list = []
        araclink_base_url = "https://www.sahibinden.com"
        
        for i in araba_isim:
            a = i.find("a").text
            arac_list.append(a)
        
        for i in araba_isim:
            connector = []
            a = i.find("a").get("href")
            connector.append(araclink_base_url)
            connector.append(a)
            href = "".join(connector)
            araclink_list.append(href)
        # =============================================================================
        #Alternative Selenium
        
        # driver_path = "C:\\Users\\Admin\\Desktop\\selenium\\chromedriver.exe"
        # browser = webdriver.Chrome(driver_path)
        # #browser.get("https://www.sahibinden.com/kategori/otomobil/alfa-romeo")
        # browser.get("https://www.sahibinden.com/otomobil")
        # 
        # browser.maximize_window()
        # time.sleep(1)
        # 
        # id_ul = browser.find_element_by_id("searchCategoryContainer")
        # ul = id_ul.find_element_by_tag_name("ul")
        # li = ul.find_elements_by_tag_name("li")
        # arac_list = []
        # araclink_list =[]
        # for i in range(1,len(li)+1):
        #     araclar = browser.find_element_by_xpath("//*[@id='searchCategoryContainer']/div/div[1]/ul/li[%d]/a"%i)
        #     araclar.location_once_scrolled_into_view
        # 
        #     #browser.execute_script('arguments[0].scrollIntoView(true);', araclar)
        #     araclink_list.append(araclar.get_attribute("href"))
        #     arac_list.append(araclar.text)
        # time.sleep(1)
        # =============================================================================
        vites_list = ["/manuel","/yari-otomatik","/otomatik"]
        yakit_list = ["/benzin","/benzin-lpg","/dizel","/hybrid","/elektrik"]
        
        
        for i in tqdm(range(0,len(araclink_list))):
            for j in range(len(yakit_list)):
                for k in range(len(vites_list)):
                    while True:
                        try:
                            bf1 = bf.Getting_information(yakit_list[j], vites_list[k], arac_list[i],araclink_list[i])
                            bf1.yakit_vites()
                            df = bf1.information_process()
                            
                        except ConnectionError:
                            print('\033[32m', "\nException'a girildi.Döngü Tekrar Başlatılıyor...",'\033[0m')
                            continue
                        break
                    for l in range(len(df)):
                        if len(df) == 0:
                            pass
                        else:    
                            final_list.append(df[l])
            
         
        t1 = time.time()
        final_time = int(t1-t0)/60
        print('\033[35m',"Veri çekme işlemi tamamlandı. Süresi {} dakika".format(final_time),'\033[0m')
        return final_list


# =============================================================================
# records.insert_many(araclar)
# records.count_documents({})
# records.delete_many({})
# =============================================================================
    
# ConnectionError: ('Connection aborted.', OSError("(10054, 'WSAECONNRESET')")) 
# =============================================================================
# bf1 = bf.Getting_information("/dizel", "/manuel", "Ford","/mazda")
# bf1.yakit_vites()
# aa = bf1.process()
# aa[1]
# 
# =============================================================================
