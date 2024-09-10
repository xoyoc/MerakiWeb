from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import certifi
import os


load_dotenv()

USER=os.getenv(MONGO_USER)
PASSWORD=os.getenv(MONGO_PASSWORD)

uri = "mongodb+srv://"+USER+":"+PASSWORD+"@cluster0.xouxv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Crear un nuevo cliente y conectarse al servidor
client = MongoClient(uri, tlsCAFile=certifi.where())

# Enviar un ping para confirmar que la conexión se ha realizado correctamente
try:
    client.admin.command('ping')
    print("Ping a su despliegue. Se ha conectado correctamente a MongoDB!")
    db = client.aaalac
except Exception as e:
    print(e)