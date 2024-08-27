from pymongo import MongoClient
from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app,resources={"/":{"origins":"*"}})
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/home")
def home():
    return "this is a home page"


client=MongoClient('mongodb://localhost:27017')
db=client['collage']

collection=db['abd']

document={'name':'nandini','age':20,'city':'jaipur','fname':'sharma'}
collection.insert_one(document)



# @app.route("/db/update")
# def update():
#     userOne = collection.find_one({'_id' : 1})
#     user = collection.find_one_and_update({"_id:1"},{'dept' : 'new-dept' , 'name':'new-name'})
#     up = collection.find_one({"_id":1})

#     return {up}

@app.route("/db/remove")
def remove():
    userOne = collection.delete_one({'_id' : 1})

    return {'name':'nandini'}


@app.route("/login",method)
def remove():
    userOne = collection.delete_one({'_id' : 1})

    return {'name':'nandini'}




# from flask import Flask

# app = Flask(__name__)



# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017")
# mdb = client['college']
# collection = mdb['abc']
# @app.route("/db/insert")
# def dataBase1():
#     users =[
#     {
#         '_id' : 1,
#         'name' : "John",
#         'dept' : "CSE"
#         },
#         {
#          '_id' : 2,
#         'name' : "Rohan",
#        'dept' : "CSE"
#         },
#         {
#          '_id' : 3,
#         'name' : "Jack",
#         'dept' : "CSE"
#         },
#         {
#          '_id' : 4,
#         'name' : "Mohan",
#        'dept' : "CSE"
#         },
#         {
#          '_id' : 5,
#         'name' : "Jojo",
#         'dept' : "CSE"
#         }
#     ]
#     collection.insert_many(users)
#     return "database inserted"

# @app.route("/db/read")
# def read():
#     userOne = collection.find_one({'_id' : 1})
#     users = collection.find({'dept' : "CSE"})
#     foundList = []
#     for user in users:
#         foundList.append(user)

#     secondList = []
#     for user in foundList:
#         secondList.append(user)
#     print ('users', users)
#     return{'fountList' : foundList, "secondList": secondList, "userOne": userOne}