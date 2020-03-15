# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 00:03:30 2020

@author: Admin
"""

from pymongo import MongoClient
import config




class Mongo():
    
    
    def send_mongo(self,collection_name,final_list):
            araclar =[]
            arac_ = {}
            for i in range(len(final_list)):
                arac_[i] = {
                        "Id" : final_list[i][0],
                        "Marka" : final_list[i][1],
                        "Seri" : final_list[i][2],
                        "Model" : final_list[i][3],
                        "Yıl" : final_list[i][4],
                        "Km": final_list[i][5],
                        "Renk": final_list[i][6],
                        "Vites": final_list[i][7],
                        "Yakıt": final_list[i][8],
                        "Sehir": final_list[i][9],
                        "Tarih": final_list[i][10],
                        "Fiyat": final_list[i][11]
                        }
                araclar.append(arac_[i])
            client = MongoClient(config.mongo)
            db = client.get_database("admin_db")
            db.create_collection(name=collection_name)
            #col_name = collection_name
            records = db[collection_name]
            records.insert_many(araclar)
    
    def check_mongo(self,collection_name):
        client = MongoClient(config.mongo)
        db = client.get_database("admin_db")
        
        records = db[collection_name]
        num = records.count_documents({})
        print("Eklenen eleman sayısı : {}".format(num))
# =============================================================================
# records.insert_many(araclar)
# records.count_documents({})
# records.delete_many({})
# =============================================================================
# =============================================================================
# col = db.create_collection(name="Collation-Test")
# col.drop()
# 
# =============================================================================
