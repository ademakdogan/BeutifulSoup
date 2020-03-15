# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 01:28:08 2020

@author: Admin
"""
import loop_process
import send_mongo
import pickle

if __name__ == "__main__":
    trigger = loop_process.Loop_process()
    final_list = trigger.bf_loop()
    sender = send_mongo.Mongo()
    #sender.send_mongo("28_01_2020",final_list)
    #records = sender.check_mongo("11_01_2020")
   

# =============================================================================
# from pymongo import MongoClient
# import config
# 
# client = MongoClient(config.mongo)
# db = client.get_database("admin_db")
# a = "11_01_2020"
# records = db[a]
# records.count_documents({})
# records.delete_many({})
# records.drop()
#filename = r"/Users/digitastic/Documents/1-sahibinden/1-beautifulsoup4-sahibinden/data/28_01_2019.sav"
#pickle.dump(final_list, open(filename, "wb"))

# =============================================================================


