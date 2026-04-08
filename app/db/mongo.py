from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["viralgen_ai"]

jobs_collection = db["jobs"]