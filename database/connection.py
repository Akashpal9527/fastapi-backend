from mongoengine import connect
from config.settings import MONGODB_URI,DATABASE_NAME

def connect_to_mongo():
    connect(host=MONGODB_URI,db=DATABASE_NAME)