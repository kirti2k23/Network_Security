import os
import sys
import json

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from NetworkSecurity.exception import MycustomException


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise MycustomException(e,sys)
        
    def cv_to_json_converter(self,filepath):
        try:
            data = pd.read_csv(filepath)
            data.reset_index(drop = True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
            pass
        except Exception as e:
            raise MycustomException(e,sys)
        
    def insert_data_Mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        
        except Exception as e:
            raise MycustomException(e,sys)
        

if __name__ == "__main__":
    Filepath = "Network_Data/phisingData.csv"
    Database = "KirtiV"
    collection = "NetworkData"

    network_obj = NetworkDataExtract()
    records=network_obj.cv_to_json_converter(Filepath)
    print(records)
    no_of_records = network_obj.insert_data_Mongodb(records,Database,collection)
    print(no_of_records)