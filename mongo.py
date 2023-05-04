import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

#  -------------- insert one record

# new_doc = {"first": "douglas", "last": "adams", "dob": "11/03/1952", "hair_color": "grey", "occupation": "writer", "nationality": "british"}

# coll.insert_one(new_doc)

# ---------------insert many records

# new_docs = [{
#     "fist": "terry",
#     "last": "pratchett",
#     "dob": "28/04/1948",
#     "gender": "m",
#     "hair_color": "not_much",
#     "occupation": "writer",
#     "naationality": "british"   
# }, {
#     "fist": "george",
#     "last": "rr martin",
#     "dob": "20/09/1948",
#     "gender": "m",
#     "hair_color": "white",
#     "occupation": "writer",
#     "naationality": "american" 
# }]

# coll.insert_many(new_docs)


# ------------ list all data

# documents = coll.find()


# ---------------find data

# documents = coll.find({"first": "douglas"})

# ---------------remove data

# coll.remove({"first": "douglas"})

# ---------------update one data

# coll.update_one({"last": "adams"}, {"$set": {"hair_color": "maroon"}})

# ---------------update one data

coll.update_many({"nationality": "american"}, {"$set": {"hair_color": "blue"}})

for doc in documents:
    print(doc)

