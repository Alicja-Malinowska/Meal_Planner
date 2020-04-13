import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

MONGODB_URI = os.getenv("MONGO_URI").replace('"', '')
app.config["MONGO_URI"] = MONGODB_URI

mongo = PyMongo(app)


    


if __name__ == '__main__':
    app.run()