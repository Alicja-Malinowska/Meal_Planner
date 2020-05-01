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

#TODO make tags appear also in after search performed; escape input in name search, consider edge cases (spaces, letter case etc)
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

# REMEMBER TO REMOVE REPLACE BEFORE DEPLOYMENT
#MONGODB_URI = os.getenv("MONGO_URI").replace('"', '')
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
    week_recipes = recipes.find({'dates':{'$elemMatch':{'$elemMatch':{'$in':week_dates}}}, 'owner': current_user.email})
    week_recipes_data = []
    for recipe in week_recipes:
        recipe_info = []
        for date in recipe['dates']:
            if date[0] in week_dates:
                recipe_info.append({"name": recipe['name'], "date": date[0], "daytime": date[1], "id": recipe['_id']})
        week_recipes_data += recipe_info
    return week_recipes_data

def get_tags(all_recipes):
    all_tags = []
    for recipe in all_recipes:
        tags = recipe["tags"]
        all_tags += tags
    all_recipes.rewind()
    tag_set = sorted(set(all_tags))
    return tag_set

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
    return render_template('layout/index.html')


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
@login_required
def next():
    first_week_day = request.form.get('first_week_day')
    date_list = first_week_day.split('-')
    date_obj = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_week = get_week(date_obj + datetime.timedelta(weeks=1))
    first_week_day = str(current_week[0][0])
    week_recipes = get_week_recipes(current_week)
    return render_template('planner.html', current_week=current_week, first_week_day=first_week_day, week_recipes=week_recipes)#morning_recipes=week_recipes[0], afternoon_recipes=week_recipes[1], evening_recipes=week_recipes[2])

@app.route('/planner/previous', methods=['GET', 'POST'])
@login_required
def previous():
    first_week_day = request.form.get('first_week_day')
    date_list = first_week_day.split('-')
    date_obj = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_week = get_week(date_obj - datetime.timedelta(weeks=1))
    first_week_day = str(current_week[0][0])
    week_recipes = get_week_recipes(current_week)
    return render_template('planner.html', current_week=current_week, first_week_day=first_week_day, week_recipes=week_recipes)#morning_recipes=week_recipes[0], afternoon_recipes=week_recipes[1], evening_recipes=week_recipes[2])

@app.route('/planner/jump_to')
@login_required
def jump_to():
    selected_date = request.args.get('jump_to')
    date_list = selected_date.split('-')
    first_week_date = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_week = get_week(first_week_date)
    week_recipes = get_week_recipes(current_week)
    return render_template('planner.html', current_week=current_week, first_week_day=first_week_date, week_recipes=week_recipes)

@app.route('/recipes')
@login_required
def recipes():
    recipes = mongo.db.recipes
    all_recipes = recipes.find({'owner': current_user.email})
    tags = get_tags(all_recipes)
    return render_template('recipes.html', recipes=all_recipes, tags=tags)


@app.route('/recipes/add', methods=['POST', 'GET'])
@login_required
def add_recipe():
    form = AddRecipe()
    if request.method == 'POST' and form.validate_on_submit():
        recipes = mongo.db.recipes
        new_recipe = request.form.to_dict()
        new_recipe['name'] = new_recipe['name'].strip()
        new_recipe['owner'] = current_user.email
        new_recipe['ingredients'] = new_recipe['ingredients'].splitlines(True)
        new_recipe['instructions'] = new_recipe['instructions'].splitlines(True)
        new_recipe['tags'] = new_recipe['tags'].replace(" ", "").strip(";").split(";")
        recipes.insert_one(new_recipe)
        flash('Recipe added!')
        return redirect(url_for('recipes'))
    return render_template('add-recipe.html', form=form)

@app.route('/show_recipe/<recipe_id>')
@login_required
def show_recipe(recipe_id):
    return render_template('selected-recipe.html',
                           recipe=mongo.db.recipes.find({'_id': ObjectId(recipe_id), 'owner': current_user.email}))
   
@app.route('/recipes/delete/<recipe_id>')
@login_required
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipes'))


@app.route('/recipes/edit/<recipe_id>')
@login_required
def edit_recipe(recipe_id):
    form = AddRecipe()
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('edit-recipe.html', the_recipe = the_recipe, form = form)

@app.route('/recipes/save_edits/<recipe_id>', methods=['POST'])
@login_required
def save_edits(recipe_id):
    recipes = mongo.db.recipes
    name = request.form.get('name').strip()
    ingredients = request.form.get('ingredients').splitlines(True)
    instructions = request.form.get('instructions').splitlines(True)
    tags = request.form.get('tags').replace(" ", "").strip(";").split(";")
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'name':request.form.get('name'),
        'ingredients':ingredients,
        'servings': request.form.get('servings'),
        'instructions': instructions,
        'tags':tags,
        'image':request.form.get('image'),
        'owner': current_user.email
    })

    return redirect(url_for('recipes'))


@app.route('/schedule', methods=['POST'])
@login_required
def schedule():
    recipes = mongo.db.recipes
    recipe_id = request.form.get('recipe_id')
    date = request.form.get('schedule_date')
    daytime = request.form.get('daytime')
    recipes.update( {'_id': ObjectId(recipe_id)}, {"$addToSet": {"dates": (date, daytime)}})
    return redirect(request.referrer)

@app.route('/del_from_schedule/<recipe_id>/<date>/<daytime>/<first_week_day>')
@login_required
def del_from_schedule(recipe_id, date, daytime, first_week_day):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)}, {"$pull": {"dates": (date, daytime)}})
    date_list = first_week_day.split('-')
    first_week_date = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_week = get_week(first_week_date)
    week_recipes = get_week_recipes(current_week)
    return render_template('planner.html', current_week=current_week, first_week_day=first_week_date, week_recipes=week_recipes)


@app.route('/search_name')
@login_required
def search_name():
    recipes = mongo.db.recipes
    all_recipes = recipes.find({'owner': current_user.email})
    tags = get_tags(all_recipes)
    recipe_name = request.args.get('recipe-name').strip()
    if recipes.count_documents({ "name": { '$regex' : recipe_name, '$options': 'i'}, 'owner': current_user.email}) > 0:
        search_results = recipes.find({ "name": { '$regex' : recipe_name, '$options': 'i'}, 'owner': current_user.email})
        return render_template('recipes.html', recipes = search_results, tags = tags)
    else:
        flash('No results found')
        return render_template('recipes.html', recipes = [], tags = tags)

@app.route('/search_tag')
@login_required
def search_tag():
    recipes = mongo.db.recipes
    all_recipes = recipes.find({'owner': current_user.email})
    tags = get_tags(all_recipes)
    selected_tag = request.args.get('tag')
    search_results = recipes.find({ "tags": selected_tag , 'owner': current_user.email})
    return render_template('recipes.html', recipes = search_results, tags = tags)



login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(email):
    user = mongo.db.users.find_one({"email_address": email})
    if not user:
        return None
    return User(user['email_address'], user['_id'], user['first_name'])


if __name__ == '__main__':
    app.run()
