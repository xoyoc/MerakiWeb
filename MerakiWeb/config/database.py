from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values
import certifi

env = dotenv_values(".env")

USER=env["MONGO_USER"]
PASSWORD=env["MONGO_PASSWORD"]

uri = "mongodb+srv://"+USER+":"+PASSWORD+"@cluster0.xouxv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Crear un nuevo cliente y conectarse al servidor
client = MongoClient(uri, tlsCAFile=certifi.where())

# Enviar un ping para confirmar que la conexión se ha realizado correctamente
try:
    client.admin.command('ping')
    print("Ping a su despliegue. Se ha conectado correctamente a MongoDB!")
    db = client.meraki
except Exception as e:
    print(e)