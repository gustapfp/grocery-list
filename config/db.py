from pymongo import MongoClient

DB_connection = MongoClient('localhost', 27017)

DB_grocery = DB_connection.grocery