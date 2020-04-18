import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from forms import RegistrationForm, LoginForm
from passlib.hash import sha256_crypt
from models import User
import datetime

'''date = datetime.date(datetime.MINYEAR, 1, 1)
today = date.today()
a_week = datetime.timedelta(days=1,weeks=1000)
next = today - a_week
print(next.weekday())'''


'''my_calendar = calendar.Calendar(firstweekday=0)
weeks = my_calendar.monthdatescalendar(2020,4)
for week in weeks:
    print(week)'''


app = Flask(__name__)
# REMEMBER TO REMOVE BEFORE DEPLOYMENT
app.secret_key = b'K/\x81\xc6\xa0R%k[mSm\xfe\xc6\x8a\xa7'
# REMEMBER TO REMOVE REPLACE BEFORE DEPLOYMENT
MONGODB_URI = os.getenv("MONGO_URI").replace('"', '')
app.config["MONGO_URI"] = MONGODB_URI

mongo = PyMongo(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)

WEEK_DAYS = {
    '0': 'Monday',
    '1': 'Tuesday',
    '2': 'Wednesday',
    '3': 'Thursday',
    '4': 'Friday',
    '5': 'Saturday',
    '6': 'Sunday'
}
DATE_INST = datetime.date(datetime.MINYEAR, 1, 1)
TODAY = DATE_INST.today()
def get_week(start_date):
    the_week = [(start_date, WEEK_DAYS[str(start_date.weekday())])]
    for i in range(1,7):
        next_day = start_date + datetime.timedelta(days=i)
        the_week.append((next_day, WEEK_DAYS[str(next_day.weekday())]))
    return the_week

'''def get_day_names(week):
    day_names = []
    for day in week:
        day_names.append(WEEK_DAYS[str(day.weekday())])
    return day_names'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = mongo.db.users.find_one({"email_address": form.email_address.data})
        if user and User.validate_login(form.password.data, user['password']):
            user_obj = User(user['email_address'], user['_id'], user['first_name'])
            print(current_user.is_authenticated)
            login_user(user_obj)
            print(current_user.is_authenticated)
            flash("Logged in successfully!", category='success')
            return redirect(request.args.get("next") or url_for("index"))
        flash("Wrong username or password!", category='error')
    return render_template('login.html', title='login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
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


    

@app.route('/planner')
@login_required
def planner():
    current_week = get_week(TODAY)
    return render_template('planner.html', current_week=current_week, first_week_day=TODAY)

'''@app.route('/planner/change-week', methods=['GET', 'POST'])
def change_week():
    next_counter = 0 if not request.form.get('counter_next') else int(request.form.get('counter_next'))
    prev_counter = 0 if not request.form.get('counter_prev') else int(request.form.get('counter_prev'))
    print(next_counter)
    print(prev_counter)
    direction = request.form.get('direction')
    count_forward = next_counter
    count_backwards = prev_counter
    if direction == 'next':
        count_forward = next_counter + 1 - prev_counter
    if direction == 'previous':
        count_backwards = prev_counter + 1 - next_counter
    time_interval = datetime.timedelta(weeks=count_forward) if direction == 'next' else datetime.timedelta(weeks=count_backwards)
    current_week = get_week(TODAY + time_interval) if direction == 'next' else get_week(TODAY - time_interval)
    days_names = get_day_names(current_week)
    return render_template('planner.html', current_week=current_week, days_names=days_names, count_forward = count_forward, count_backwards = count_backwards)'''
    
'''@app.route('/planner/previous', methods=['GET', 'POST'])
def previous():
    prev_counter = 0 if not request.form.get('counter_prev')  else int(request.form.get('counter_prev'))
    count_forward = 1 if request.form.get('counter_next') == '' else int(request.form.get('counter_next')) + 1 - prev_counter
    time_interval = datetime.timedelta(weeks=count_forward)
    current_week = get_week(TODAY + time_interval)
    days_names = get_day_names(current_week)
    return render_template('planner.html', current_week=current_week, days_names=days_names, count_forward = count_forward)
    next_counter = 0 if not request.form.get('counter_next') else int(request.form.get('counter_next'))
    count_backwards = 1 if request.form.get('counter_prev') == '' else int(request.form.get('counter_prev')) + 1 + next_counter
    time_interval = datetime.timedelta(weeks=count_backwards)
    current_week = get_week(TODAY - time_interval)
    days_names = get_day_names(current_week)
    return render_template('planner.html', current_week=current_week, days_names=days_names, count_backwards = count_backwards)'''

@app.route('/planner/next', methods=['GET', 'POST'])
def next():
    first_week_day = request.form.get('first_week_day')
    date_list = first_week_day.split('-')
    date_obj = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_week = get_week(date_obj + datetime.timedelta(weeks=1))
    first_week_day = str(current_week[0][0])
    return render_template('planner.html', current_week=current_week, first_week_day=first_week_day)

@app.route('/planner/previous', methods=['GET', 'POST'])
def previous():
    first_week_day = request.form.get('first_week_day')
    date_list = first_week_day.split('-')
    date_obj = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_week = get_week(date_obj - datetime.timedelta(weeks=1))
    first_week_day = str(current_week[0][0])
    return render_template('planner.html', current_week=current_week, first_week_day=first_week_day)

@app.route('/planner/jump_to')
def jump_to():
    selected_date = request.args.get('jump_to')
    print(selected_date)
    date_list = selected_date.split('-')
    first_week_date = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_week = get_week(first_week_date)
    return render_template('planner.html', current_week=current_week, first_week_day=first_week_date)


login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(email):
    user = mongo.db.users.find_one({"email_address": email})
    if not user:
        return None
    return User(user['email_address'], user['_id'], user['first_name'])


if __name__ == '__main__':
    app.run()
