import pymongo
import certifi


con_str = "mongodb+srv://nrasaily:Asdf1231xserver@cluster0.fgtueht.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("nrasaily")