import pymongo
import certifi


con_str = "mongodb+srv://FSDI:FSDI1234@cluster0.fgtueht.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("Organica_ch56")