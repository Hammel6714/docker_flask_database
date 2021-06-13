from pymongo import MongoClient
from bson.objectid import ObjectId

conn = MongoClient("mongodb://rs1:27041/") 
db = conn.test
collection = db.col

#collection.stats

collection.insert_one({"aa":"222"})

