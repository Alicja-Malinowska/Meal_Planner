import os
import datetime
import uuid
from flask import Flask, render_template, redirect, request, url_for, flash, abort
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from forms import RegistrationForm, LoginForm, AddRecipe, SearchName
from passlib.hash import sha256_crypt
from models import User
from helpers import is_safe_url, get_week, get_tags



app = Flask(__name__)

MONGODB_URI = os.getenv("MONGO_URI").replace('"', '')
app.secret_key = os.getenv("SECRET_KEY")
app.config["MONGO_URI"] = MONGODB_URI


mongo = PyMongo(app)
login_manager = LoginManager()
login_manager.init_app(app)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


DATE_INST = datetime.date(datetime.MINYEAR, 1, 1)
TODAY = DATE_INST.today()


def get_week_recipes(current_week):
    '''makes a call to the database to find all the recipes scheduled in a given week
    takes current_week as an argument, which should be return from get_week function'''
    recipes = mongo.db.recipes
    week_dates = []
    for day_tuple in current_week:
        day = day_tuple[0]
        str_day = day.strftime("%Y-%m-%d")
        week_dates.append(str_day)
    week_recipes = recipes.find({'dates': {'$elemMatch': {'$elemMatch': {
                                '$in': week_dates}}}, 'owner': current_user.email})
    week_recipes_data = []
    for recipe in week_recipes:
        recipe_info = []
        for date in recipe['dates']:
            if date[0] in week_dates:
                recipe_info.append(
                    {"name": recipe['name'], "date": date[0], "daytime": date[1], "id": recipe['_id']})
        week_recipes_data += recipe_info
    return week_recipes_data


@app.route('/')
def home():
    ''' renders home view, gets scheduled recipes from database for logged in user'''
    recipes = mongo.db.recipes
    today = TODAY.strftime("%Y-%m-%d")
    today_recipes = []
    message = ""
    if current_user.is_authenticated:
        today_recipes = recipes.find({'dates': {'$elemMatch': {'$elemMatch': {
                                     '$in': [today]}}}, 'owner': current_user.email})
        if recipes.count_documents({'dates': {'$elemMatch': {'$elemMatch': {'$in': [today]}}}, 'owner': current_user.email}) == 0:
            message = "You have nothing scheduled today."
    return render_template('pages/home.html', today_recipes=today_recipes, message=message, title="home")

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    ''' adds a user to database if a user with given email does not already exists'''
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        users = mongo.db.users
        profile = request.form.to_dict()
        if users.count_documents({"email_address": profile["email_address"]}) > 0:
            flash(
                "An account has already been registered for this email address", "errors")
            return render_template('pages/registration.html', form=form, title="register")
        else:
            profile["confirm"] = sha256_crypt.hash(profile["confirm"])
            profile["password"] = sha256_crypt.hash(profile["password"])
            users.insert_one(profile)
            user_obj = User(profile['email_address'], profile['first_name'])
            login_user(user_obj)
            flash("All done! You're registered!", "success")
            return redirect(url_for('home'))

    return render_template('pages/registration.html', form=form, title="register")


@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' logs user in if email address and password match'''
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = mongo.db.users.find_one(
            {"email_address": form.email_address.data})
        if user and User.validate_login(form.password.data, user['password']):
            user_obj = User(user['email_address'], user['first_name'])
            login_user(user_obj)
            flash("Logged in successfully!", 'success')
            next = request.args.get('next')
            if not is_safe_url(next):
                return abort(400)
            return redirect(next or url_for('home'))
        flash("Wrong username or password!", 'errors')
    return render_template('pages/login.html', title='login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route('/planner')
@login_required
def planner():
    current_week = get_week(TODAY)
    week_recipes = get_week_recipes(current_week)
    return render_template('pages/planner.html', current_week=current_week, first_week_day=TODAY, week_recipes=week_recipes, title="planner")


@app.route('/planner/next', methods=['GET', 'POST'])
@login_required
def next():
    ''' calculates dates for +1 week from last view'''
    first_week_day = request.form.get('first_week_day')
    date_list = first_week_day.split('-')
    date_obj = datetime.date(int(date_list[0]), int(
        date_list[1]), int(date_list[2]))
    current_week = get_week(date_obj + datetime.timedelta(weeks=1))
    first_week_day = str(current_week[0][0])
    week_recipes = get_week_recipes(current_week)
    return render_template('pages/planner.html', current_week=current_week, first_week_day=first_week_day, week_recipes=week_recipes, title="planner")


@app.route('/planner/previous', methods=['GET', 'POST'])
@login_required
def previous():
    ''' calculates dates for -1 week from last view'''
    first_week_day = request.form.get('first_week_day')
    date_list = first_week_day.split('-')
    date_obj = datetime.date(int(date_list[0]), int(
        date_list[1]), int(date_list[2]))
    current_week = get_week(date_obj - datetime.timedelta(weeks=1))
    first_week_day = str(current_week[0][0])
    week_recipes = get_week_recipes(current_week)
    return render_template('pages/planner.html', current_week=current_week, first_week_day=first_week_day, week_recipes=week_recipes, title="planner")


@app.route('/planner/jump_to')
@login_required
def jump_to():
    ''' renders a view of week starting with a date chosen by user'''
    selected_date = request.args.get('jump_to')
    date_list = selected_date.split('-')
    first_week_date = datetime.date(
        int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_week = get_week(first_week_date)
    week_recipes = get_week_recipes(current_week)
    return render_template('pages/planner.html', current_week=current_week, first_week_day=first_week_date, week_recipes=week_recipes, title="planner")


@app.route('/recipes')
@login_required
def recipes():
    ''' gets all user's recipes from database'''
    form = SearchName()
    recipes = mongo.db.recipes
    all_recipes = recipes.find({'owner': current_user.email})
    tags = get_tags(all_recipes)
    return render_template('pages/recipes.html', recipes=all_recipes, tags=tags, form=form, title="recipes")


@app.route('/recipes/add', methods=['POST', 'GET'])
@login_required
def add_recipe():
    ''' created a new recipe document in database with user's data'''
    form = AddRecipe()
    target = os.path.join(
        APP_ROOT, 'static/images/recipe-images/')  # folder path
    if not os.path.isdir(target):
        os.mkdir(target)     # create folder if not exits
    if request.method == 'POST' and form.validate_on_submit():
        recipes = mongo.db.recipes
        new_recipe = request.form.to_dict()
        image = request.files[form.image.name]

        if image.filename:  # if image was uploaded
            name, file_extension = os.path.splitext(image.filename)
            filename = secure_filename(
                str(uuid.uuid1()) + file_extension)  # get a unique filename
            # create path to save the file
            destination = "".join([target, filename])
            image.save(destination)
        else:
            filename = 'default.png'
        new_recipe['name'] = new_recipe['name'].strip()
        new_recipe['owner'] = current_user.email
        new_recipe['ingredients'] = new_recipe['ingredients'].splitlines(True)
        new_recipe['instructions'] = new_recipe['instructions'].splitlines(
            True)
        new_recipe['tags'] = new_recipe['tags'].lower().replace(
            " ", "").strip(";").split(";")
        new_recipe['image'] = filename
        recipes.insert_one(new_recipe)
        flash('Recipe added!', 'success')
        return redirect(url_for('recipes'))
    return render_template('pages/add-recipe.html', form=form, title="add recipe")


@app.route('/show_recipe/<recipe_id>')
@login_required
def show_recipe(recipe_id):
    ''' gets a demanded recipe from database '''
    recipes = mongo.db.recipes
    # the validity check is needed in case user tries to type the url themselves
    if ObjectId.is_valid(recipe_id) and recipes.count_documents({'_id': ObjectId(recipe_id), 'owner': current_user.email}) > 0:
        recipe = recipes.find(
            {'_id': ObjectId(recipe_id), 'owner': current_user.email})
    else:
        return abort(404)
    return render_template('pages/selected-recipe.html', this_recipe=recipe, title="recipe")


@app.route('/recipes/delete', methods=['POST'])
@login_required
def delete_recipe():
    ''' removes recipe document from database '''
    recipe_id = request.form.get('recipe_id')
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    flash('Recipe deleted!', 'success')
    return redirect(url_for('recipes'))


@app.route('/recipes/edit/<recipe_id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    ''' saves a recipe with user changes in the database '''
    form = AddRecipe()
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    target = os.path.join(APP_ROOT, 'static/images/recipe-images/')
    if request.method == 'POST' and form.validate_on_submit():
        recipes = mongo.db.recipes
        name = request.form.get('name').strip()
        ingredients = request.form.get('ingredients').splitlines(True)
        instructions = request.form.get('instructions').splitlines(True)
        tags = request.form.get('tags').lower().replace(
            " ", "").strip(";").split(";")
        image = request.files[form.image.name]
        if image:  # if a new file was uploaded
            file_name, file_extension = os.path.splitext(image.filename)
            filename = secure_filename(str(uuid.uuid1()) + file_extension)
            destination = "".join([target, filename])
            image.save(destination)
        else:
            filename = recipes.find_one({'_id': ObjectId(recipe_id)})['image']
        recipes.update({'_id': ObjectId(recipe_id)},
                       {
            'name': name,
            'ingredients': ingredients,
            'servings': request.form.get('servings'),
            'instructions': instructions,
            'tags': tags,
            'image': filename,
            'owner': current_user.email,
            'dates': the_recipe["dates"]
        })
        flash('Changes saved!', 'success')
        return redirect(url_for('recipes'))
    return render_template('pages/edit-recipe.html', the_recipe=the_recipe, form=form, title="edit recipe")


@app.route('/schedule', methods=['POST'])
@login_required
def schedule():
    ''' adds chosen date to dates array in the recipe document '''
    recipes = mongo.db.recipes
    recipe_id = request.form.get('recipe_id')
    date = request.form.get('schedule_date')
    daytime = request.form.get('daytime')
    recipes.update({'_id': ObjectId(recipe_id)}, {
                   "$addToSet": {"dates": (date, daytime)}})
    flash('Recipe added to the planner!', 'success')
    return redirect(request.referrer)


@app.route('/del_from_schedule/<recipe_id>/<date>/<daytime>/<first_week_day>')
@login_required
def del_from_schedule(recipe_id, date, daytime, first_week_day):
    ''' removes date from dates array in the recipe document '''
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)}, {
                   "$pull": {"dates": (date, daytime)}})
    date_list = first_week_day.split('-')
    first_week_date = datetime.date(
        int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_week = get_week(first_week_date)
    week_recipes = get_week_recipes(current_week)
    return render_template('pages/planner.html', current_week=current_week, first_week_day=first_week_date, week_recipes=week_recipes, title="planner")


@app.route('/search_name',  methods=['GET', 'POST'])
@login_required
def search_name():
    ''' performs a case insensitive search for user's recipe documents including searched string '''
    form = SearchName()
    recipes = mongo.db.recipes
    all_recipes = recipes.find({'owner': current_user.email})
    tags = get_tags(all_recipes)
    if form.validate_on_submit():
        recipe_name = request.form.get('name').strip()
        searched = 'name'
        if recipes.count_documents({"name": {'$regex': recipe_name, '$options': 'i'}, 'owner': current_user.email}) > 0:
            search_results = recipes.find(
                {"name": {'$regex': recipe_name, '$options': 'i'}, 'owner': current_user.email})
            return render_template('pages/recipes.html', recipes=search_results, tags=tags, searched=searched, recipe_name=recipe_name, form=form, title="recipes")
        else:
            flash('No results found', "errors")
            return render_template('pages/recipes.html', recipes=[], tags=tags, searched=searched, recipe_name=recipe_name, form=form, title="recipes")
    return render_template('pages/recipes.html', recipes=all_recipes, tags=tags, form=form, title="recipes")


@app.route('/search_tag')
@login_required
def search_tag():
    ''' retrievs all user's recipes with selected tag '''
    form = SearchName()
    recipes = mongo.db.recipes
    all_recipes = recipes.find({'owner': current_user.email})
    tags = get_tags(all_recipes)
    selected_tag = request.args.get('tag')
    searched = 'tag'
    search_results = recipes.find(
        {"tags": selected_tag, 'owner': current_user.email})
    return render_template('pages/recipes.html', recipes=search_results, tags=tags, searched=searched, tag=selected_tag, form=form, title="recipes")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html', title="Error"), 404


# view to be loaded if user is not logged in and login is required to access a page
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(email):
    user = mongo.db.users.find_one({"email_address": email})
    if not user:
        return None
    return User(user['email_address'], user['first_name'])

deb = True

app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")), debug=deb)
