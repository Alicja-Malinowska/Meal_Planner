import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from registration import RegistrationForm
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = b'K/\x81\xc6\xa0R%k[mSm\xfe\xc6\x8a\xa7'#REMEMBER TO REMOVE BEFORE DEPLOYMENT
MONGODB_URI = os.getenv("MONGO_URI").replace('"', '')#REMEMBER TO REMOVE REPLACE BEFORE DEPLOYMENT
app.config["MONGO_URI"] = MONGODB_URI

mongo = PyMongo(app)
Bootstrap(app)
#login_manager = LoginManager()
#login_manager.init_app(app.py)

@app.route('/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        users = mongo.db.users
        profile = request.form.to_dict()
        if users.count_documents({"email_address": profile["email_address"]}) > 0:
            flash("An account has already been registered for this email address")
            return redirect(url_for('registration'))
        else:
            profile["confirm"] = sha256_crypt.hash(profile["confirm"])
            profile["password"] = sha256_crypt.hash(profile["password"])
            users.insert_one(profile)
            return "All done! You're registered"

    return render_template('registration.html', form=form)

users = mongo.db.users.count_documents({"email_address": "amalinowska.p@gmail.com"})
print(users)



if __name__ == '__main__':
    app.run()