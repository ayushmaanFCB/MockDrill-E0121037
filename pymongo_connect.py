from pymongo.mongo_client import MongoClient
import configparser
from bson import ObjectId

config = configparser.ConfigParser()
config.read('./configs/config.ini')
uri = config.get('MONGODB_ATLAS', 'key')

try:
    cluster = MongoClient(uri)
    db = cluster["MockDrills"]
    collection = db["Property_Rental"]
    collection2 = db['Booking_History']
    print("\nConnection to Database Successfull !!! \n")
except Exception as e:
    print("Failed to connect to Mongo DB Database : ", e)


def pushToDB(post):
    result = collection.insert_one(post)
    return result


def pushToBooking(post):
    result = collection2.insert_one(post)


def fetchAllRecords():
    return collection.find({})


def fetchHistory(email):
    return collection2.find({"email": email})


def fetchProperty(id):
    return collection.find({"_id": id})


def bookRemove(id):
    filter = {'_id': ObjectId(id)}

    update = {
        '$set': {
            'status': 'booked',
        }
    }

    result = collection.update_one(filter, update)
