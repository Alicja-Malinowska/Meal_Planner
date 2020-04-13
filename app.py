import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from registration import RegistrationForm

app = Flask(__name__)
app.secret_key = b'K/\x81\xc6\xa0R%k[mSm\xfe\xc6\x8a\xa7'#REMEMBER TO REMOVE BEFORE DEPLOYMENT
MONGODB_URI = os.getenv("MONGO_URI").replace('"', '')#REMEMBER TO REMOVE REPLACE BEFORE DEPLOYMENT
app.config["MONGO_URI"] = MONGODB_URI

mongo = PyMongo(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def registration():
    
    return 'dupa'


if __name__ == '__main__':
    app.run()