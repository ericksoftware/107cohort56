import pymongo
import certifi

con_str = "mongodb+srv://e1291222:8qqs6kg1@cluster0.eycc1r5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("store")