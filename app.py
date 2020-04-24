import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from forms import RegistrationForm, LoginForm, AddRecipe
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

#   FIGURE OUT HOW TO DEAL WITH SEARCHING IN THE ARRAY OF TUPLES, PERHAPS LOOK FOR A TUPLE (MORNING, AFTERNOON EVENING)
def get_week_recipes(current_week):
    recipes = mongo.db.recipes
    week_dates = []
    for day_tuple in current_week:
        day = day_tuple[0]
        str_day = day.strftime("%Y-%m-%d")
        week_dates.append(str_day)
    '''morning_recipes = []
    afternoon_recipes = []
    evening_recipes = []
    for day in week_dates:
       morning_recipes.append((recipes.find( { 'dates':  [day, 'Morning'], 'owner': current_user.email} ), day))
       afternoon_recipes.append((recipes.find( { 'dates':  [day, 'Afternoon'], 'owner': current_user.email} ), day))
       evening_recipes.append((recipes.find( { 'dates':  [day, 'Evening'], 'owner': current_user.email} ), day))'''
    week_recipes = recipes.find({'dates':{'$elemMatch':{'$elemMatch':{'$in':week_dates}}}, 'owner': current_user.email})
    week_recipes_data = []
    for recipe in week_recipes:
        recipe_info = []
        for date in recipe['dates']:
            if date[0] in week_dates:
                recipe_info.append({"name": recipe['name'], "date": date[0], "daytime": date[1], "id": recipe['_id']})
        week_recipes_data += recipe_info
    return week_recipes_data

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
    week_recipes = get_week_recipes(current_week)
    return render_template('planner.html', current_week=current_week, first_week_day=TODAY, week_recipes=week_recipes)#morning_recipes=week_recipes[0], afternoon_recipes=week_recipes[1], evening_recipes=week_recipes[2])


@app.route('/planner/next', methods=['GET', 'POST'])
def next():
    first_week_day = request.form.get('first_week_day')
    date_list = first_week_day.split('-')
    date_obj = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_week = get_week(date_obj + datetime.timedelta(weeks=1))
    first_week_day = str(current_week[0][0])
    week_recipes = get_week_recipes(current_week)
    return render_template('planner.html', current_week=current_week, first_week_day=first_week_day, week_recipes=week_recipes)#morning_recipes=week_recipes[0], afternoon_recipes=week_recipes[1], evening_recipes=week_recipes[2])

@app.route('/planner/previous', methods=['GET', 'POST'])
def previous():
    first_week_day = request.form.get('first_week_day')
    date_list = first_week_day.split('-')
    date_obj = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_week = get_week(date_obj - datetime.timedelta(weeks=1))
    first_week_day = str(current_week[0][0])
    week_recipes = get_week_recipes(current_week)
    return render_template('planner.html', current_week=current_week, first_week_day=first_week_day, week_recipes=week_recipes)#morning_recipes=week_recipes[0], afternoon_recipes=week_recipes[1], evening_recipes=week_recipes[2])

@app.route('/planner/jump_to')
def jump_to():
    selected_date = request.args.get('jump_to')
    date_list = selected_date.split('-')
    first_week_date = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_week = get_week(first_week_date)
    return render_template('planner.html', current_week=current_week, first_week_day=first_week_date)

@app.route('/recipes')
@login_required
def recipes():
    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find({'owner': current_user.email}))

@app.route('/recipes/add', methods=['POST', 'GET'])
def add_recipe():
    form = AddRecipe()
    if request.method == 'POST' and form.validate_on_submit():
        recipes = mongo.db.recipes
        new_recipe = request.form.to_dict()
        new_recipe['owner'] = current_user.email
        new_recipe['ingredients'] = new_recipe['ingredients'].splitlines()
        new_recipe['instructions'] = new_recipe['instructions'].splitlines()
        recipes.insert_one(new_recipe)
        flash('Recipe added!')
        return redirect(url_for('recipes'))
    return render_template('add-recipe.html', form=form)

@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    return render_template('selected-recipe.html',
                           recipe=mongo.db.recipes.find({'_id': ObjectId(recipe_id)}))
   
@app.route('/recipes/delete/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipes'))


@app.route('/recipes/edit/<recipe_id>')
def edit_recipe(recipe_id):
    form = AddRecipe()
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('edit-recipe.html', the_recipe = the_recipe, form = form)

@app.route('/recipes/save_edits/<recipe_id>', methods=['POST'])
def save_edits(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'name':request.form.get('name'),
        'ingredients':request.form.get('ingredients'),
        'servings': request.form.get('servings'),
        'instructions': request.form.get('instructions'),
        'tags':request.form.get('tags'),
        'image':request.form.get('image'),
        'owner': current_user.email
    })

    return redirect(url_for('recipes'))


@app.route('/schedule', methods=['POST'])
def schedule():
    recipes = mongo.db.recipes
    recipe_id = request.form.get('recipe_id')
    date = request.form.get('schedule_date')
    daytime = request.form.get('daytime')
    recipes.update( {'_id': ObjectId(recipe_id)}, {"$addToSet": {"dates": (date, daytime)}})
    return redirect(url_for('recipes'))

login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(email):
    user = mongo.db.users.find_one({"email_address": email})
    if not user:
        return None
    return User(user['email_address'], user['_id'], user['first_name'])


if __name__ == '__main__':
    app.run()
