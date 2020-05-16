# [MealPlanner](https://meal-planner-m3.herokuapp.com/)


MealPlanner is a web application that allows a user to save their own recipes and add them to a calendar in order to plan their meals. Each user has their own account where they can add, edit and delete their recipes and schedule them in the planner. The app can be used on any device, e.g. mobile, tablet, laptop. 

**A test account has been created with some recipes added and scheduled. It can be accessed by using the email address: test@gmail.com, and the password: test.**


#### External user’s goal:

The site users are people who want an easy and clean way to store their recipes and schedule them.

#### Site owner's goal:

The site owner's goal is to use the application themselves and perhaps to charge for extra features in the future, if the app becomes popular.   

 
## UX

The target user group are the people who like to use technological solutions to organise their time in the most efficient way. Additionally, the users are people who enjoy cooking or cook often for other reasons and want to save time by keeping their recipes in one place and easily scheduling for days, weeks or even months and more ahead.  

### User stories

* As a user I want to be able to create an account in the application
* As a user I want to be informed if an account for my email address already exists so that I know the account was created before with my email address
* As a user I want to be able to login into my account so that I can see the content only available to me
* As a user I want to be able to logout from my account so that others cannot access my content
* As a user I want to be informed if the registration or login form was not validated correctly so I know what to change to be able to procees
* As a user I want to be taken to the login page if I try to access pages that require login and then to be redirected to the chosen page
* As a user I want to see short description and screenshots of pages so I can find out what the application does and how it looks like before I decide to register
* As a user I want to have a clear navigation that will take me to different pages in the website
* As a user I want to go back to homepage by clicking the logo
* As a user I want to have a view of recipes planned for the current day, on the homepage after login, so I can immediatelly have this information wthout going to the planner
* As a user I want to be informed o my homepage, after I logged in, that I don't have anything scheduled if that is the case, and I want some actions suggested to me so I know what to do next
* As a user I want to have a page that displays all my recipes so I can see what I have already added
* As a user I want to be able to click a recipe name so that I can access the recipe page with its full description
* As a user I want to have a delete button so I can delete my recipes
* As a user I want to be asked to confirm deletion before my recipe is permanently deleted
* As a user I want to have edit button that will take me to recipe edit page so that I can make changes to existing recipes
* As a user I want to have a shedule button so that I can add my recipe to the planner by choosing a date from datepicker and a time of day
* As a user I want to have an add button so I can add my own recipes, including an image of them and tags to describe them
* As a user I want to have a search field so that I can type recipe name and display the search results as a list of one or more elements
* As a user I want to have a drop down with all the tags so that I can search for recipes with a particular tag
* As a user I want to click a tag in a recipe view so I can see a list of all rcipes with that tag
* As a user I want to have a planner view so I can see what I have planned for the week
* As a user I want to have buttons that let me view next and previous weeks so that I can see what I have planned for them
* As a user I want to have a button that can when clicked displays current week in the planner so I can quickly go back to it
* As a user I want to have a field where I can choose a date so I can move quickly to a specific week in the planner
* As a user I want to be able to have a button that removes the recipe from planner with one click


The page navigation is designed to be intuitive and enable a user to perform required actions quickly and easily. The design offers a user multiple places from where they can view their recipes and perform actions connected to them (delete, edit, schedule, add etc). The overall design is meant to be simple and clear without unnecessary distractions. The colors were chosen using [Material Design colour picking tool](https://material.io/design/color/the-color-system.html#tools-for-picking-colors). The primary colour is #880E4F and the rest were chosen from the primary and complemetary palettes as shown below. 


![colour-palettes-image](https://i.imgur.com/4VLVjxv.jpg)

### Wireframes

These are the wireframes for some pages:

![planner](https://github.com/Alicja-Malinowska/Meal_Planner/blob/master/wireframes/planner.png)
![recipes](https://github.com/Alicja-Malinowska/Meal_Planner/blob/master/wireframes/recipes.png)
![recipe view](https://github.com/Alicja-Malinowska/Meal_Planner/blob/master/wireframes/recipe-view.png)

All the wireframes can be found in the [wirefreames folder](https://github.com/Alicja-Malinowska/Meal_Planner/tree/master/wireframes).


## Features

All the features were added to enhance the UX and make the website easy to use and intuitive to move around. 
 
### Existing Features

* **Fixed navbar**

  This element appears on all the pages. It contains a clickable logo that takes user to the homepage, and links to the remaining pages, as well as Register and Login links when there is no logged in user, and a Logout link instead of them, if a user is logged in. The navbar is expanded on large devices and on smaller ones it is collapsed. When tha hamburger menu is clicked a side bar is triggered and the menu links are available for a user to click. When a user clicks a link the sidebar hides automatically. 

* **Pages with 'login required'**

  Most of the pages require a user to be logged in before they can access them. This is necessary because of the nature of the application - every user should be able to add their own content without it being shared wth others and without seeing content that does not belong to them. When an anonymous user tries to access a page where login is required, they are automatically redirected to the login page, and after successful login they are redirected to the page they tried to access.   

#### Home page - no login

* Screenshots of home page, recipe page and planner page

  The screenshots are there to show an anonymous user what app looks like and what they can expect from it, before they make a decision to register and use the app. This is done to enhance user experience and give the user as much information as possible. Even though the app is free, the user spends their time to fill out registration form, so tbefore they decide to invest this time, they should know what goals they can achieve using the app and this feature provides just that.

* **'Register' and 'Login' links**

  The links are situated immediately below the images. They are there so that registering or logging in is an easier decision for the user to make. Although those links can also be found on the navbar, it is more natural for the user to go from top of the page to bottom, and therefore, a user, after seeing the screenshots, sees the links immediately. Otherwise, they would have to look for the links, which might discourage them from proceeding with login, or, particullarly, registration. 

#### Register and Login forms

* **Link to sign in in register form and link to register in sign in form**

  This is provided in case a user already has an account and by mistake clickd 'register' on the navbar or wanted to register but clicked 'sign in' instead. Thanks to this the user does not have to go back up to the navbar, but can click 'sign in' or 'register' link immediately after they realised that this is not where they need to be. 

* **Field validation**

  This is achieved with backend validation provided by [WTForms](https://wtforms.readthedocs.io/en/stable/). All fields are required. There are extra validators for email address to make sure it is valid, e.g length restriction. There is also a validator checking if the password and confirmed password are the same in the registration form. If the form does not validate, suitable messages are displayed to inform the user what went wrong and how to fix this.

* **Password hashing**

  When a user registers their data is stored in the database. However, before the data is sent to the database the password is hashed for security reasons, using sha256. When password is validated, its hashed versions are compared.

* **Automatic login**

  After successful registration a user is automatically logged in so that they do not need to go to the login page and perfom unnecessary action, and they can access the login-only pages immediately. 

#### Home page - logged in user

* **Today recipes**

  Recipes scheduled for the day are displayed as cards with the recipe image and its name that is a link to the recipe page. This allows a user to quickly see what they have planned for the day without having to go the planner. They can also access the recipes directly from the home page without going to the recipes page or links in the planner. 

* **Additional actions when nothing is scheduled**

  If a user has nothing scheduled for the day, a message is displayed that this is the case. Aditionally, there are some actions suggested in a form of links to planner, recipes and add recipe form. This view is what every new user will see, as they will not have anything schedule after they registered, and therefore the suggested actions are particularly important for them, as they give them some guidance how to move around the app before they get familiar with it. 

#### Planner

* **Week view**

  Planner offers a view of the week (7 consecutive days) starting with the current day. Each day is divided into morning, afternoon and evening for easier planning different meals. On desktop view this is presented in the form of table, where columns are days of the week and rows are daytimes. In the mobile view, this is presented as schedule, where each day is displayed separately in full width. 

* **Scheduled recipes**
  
  The recipes that were scheduled appear in the planner under specific date and daytime in a form of a link that leads to the recipe page. There is also a delete button next to each recipe displayed in the planner, that removes it from the planner. 

* **Next and Previous arrows**

  These are located at the top of the page and allow a user to move to tne previous and following weeks views. 

* **'Current week' button**

  When the button is clicked, the calendar view returns to the current week view.

* **'Custom date' field**

  When clicked, a datepicker is triggered and a user can choose any date within 15-year period (this is datepicker setting and can be changed for longer/shorter period). When the date is chosen, the planner view changes to the week starting with the chosen date. 

* **Link to Recipes**

  This is placed on top of the planner to inform user where they can schedule their recipes so that they appear in the planner. 

#### Recipes page

* **Add new recipe button**

  When the button is clicked, a user is taken to a page that contains a form that enables adding a new recipe.

* **Search by name**

  This allows user to search for a recipe by name. The search is case insensitive and returns all the recipes that include searched string. 

* **Search by tag**

  A drop down that contains all the tags, alphabetically ordered, that the user used in their recipes. The search returns all the recipes that include the chosen tag. 

* **'Back to all recipes' button**

  This button is only visible when a search was performed and is situated below the search results. When clicked, it takes the user back to the view with all the recipes, without any filters. 

* **Recipes collection**

  This is a list of recipes displayed on the page. Each item has a circle-shaped recipe image and a name of the recipe, which is a link to the recipe page. Each item also has three action buttons that allow schedule the recipe, edit the recipe and delete the recipe. 

* **'Add to planner' button**

  When clicked, a modal is triggered. Within the modal, a user chooses a date using datepicker and one of the three options of daytime. Both are required. The success message is flashed when the recipe is added. 

* **'Edit' button**

  When clicked, takes a user to edit form page.

* **'Delete' button**

  Triggers a modal that informs that the recipe will be permanently deleted and asks for confirmation. User can either confirm, which will result in deletion of the recipe or close, which will not result in any action other than modal being dismissed. If user chooses to delete and confirm, a confirmatory message is flashed. 

#### Add recipe page and Edit recipe page

* **Field validation**

  Similarly to registation and login forms, this form was also created using WTForms and has backend validation. The only required field is the recipe name, the rest is optional. There is an addtional validator for name - only letters and spaces are allowed. The reason for this is that a regex search is used to search for recipes name, and if a user would some regex specifi characters (e.g '*') this would cause the app to crash. User is informed about it in placeholder and an errors message is displayed when they try to submit a recipe with a name that has other characters. When file is being uploaded, a check is performed to see if the files has jpg or png format. If not, the validation fails and the recipe is not added. There is also a custom validator written for the tags field that checks if there is at least one semicolon included in the string if the field is not empty. The tags are required to be separated by semicolons, and there is a note in the form that informs a user about it. If a user tries to submit tags without a least one semicolon, an error message appears so that they can quickly learn how to insert the tags. 


* **Image upload**

  When a user uploads an image of recipe, if it's a valid file format, the file is renamed using uuid to ensure that there are no two files with the same name file name. This is important, as the filename is saved in the database and is used to display the image. The file itself is saved on the app server, in the images folder. 


### Features Left to Implement

* **User account actions**

  For this project to be fully functional registration/login feature was essential. However, there were no requirements for this for this project, as this is out of the scope of the module. Therefore, the registration-login system is fairly simple in the application. A user creates an account and can login using the given credentials. The features that could be further implemented are: possibility to update password, edit profile and delete profile. 

* **Adding recipes directly from planner**

  Right now recipes are added to the planner from recipes list or from a recipe page. A new feature could allow user to click in the planner and be able to search for a recipe and add it to the day and daytime that was clicked.

* **Shopping list**

  Another page could be added that would include a shopping list view. A user could add ingredients from selected recipe to the list, as well as type their own items.

* **Recipe import**

  This feature would make it possible to import recipes from popular recipe websites, like AllRecipes, so that the user doesn't have to copy and paste if they want to save a recipe that is already on one of these websites. 

## Database

MongoDB was used to store data for this application. As there are no complex relationships between different entities, a non-relational database seemed to be suitable choice for data storage.

### Collections

There are two collections created for the project: user and recipes.

#### Users

| Key           | Data type     |
| ------------- |:-------------:|
| _id           | ObjectId      |
| first_name    | String        |
| last_name     | String        |
| password      | String(hashed)|

#### Recipes

| Key           | Data type     |
| ------------- |:-------------:|
| _id           | ObjectId      |
| name          | String        |
| servings      | String        |
| ingredients   | Array         |
| instructions  | Array         |
| tags          | Array         |
| image         | String        |
| owner         | String        |
| dates         | Array         |

Please see [schemas folder](https://github.com/Alicja-Malinowska/Meal_Planner/blob/master/schemas) for these data models in json format. 

## Technologies Used

### Languages

  * [Python]https://www.python.org/
  * HTML
  * CSS
  * JavaScript

### Libraries

  * [jQuery](https://jquery.com/)
  * [Flask](https://flask.palletsprojects.com/en/1.1.x/) - to handle http requests and render pages
  * [Flask-login](https://flask-login.readthedocs.io/en/latest/) - to provide login functionality
  * [WTForms](https://wtforms.readthedocs.io/en/2.3.x/) - for forms validation and rendering
  * [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - PyMongo provides a way for Python to work with MongoDB and Flask-Pymongo makes it easier to use PyMongo within Flask framework
  * [PassLib](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) - used to hash and compare hashed passwords
  * [Materialize](http://archives.materializecss.com/0.100.2/) - used for styling based on Matrial Design 
  

### Tools
  * [Visual Studio Code](https://code.visualstudio.com/) - an IDE used to write the code
  * [MongoDB](https://www.mongodb.com/) - used to store and retrieve data
  * [Git](https://git-scm.com/) - used for version control
  

**Note to assessor**: This project used git branching for development. Although 'no fast forward' (--no-ff) merging was used to make this visible in the history, the branches are still visible on GitHub for easier access. It is best practice, however, to remove merged branches. 

## Testing

Please see the separate [testing.md document](https://github.com/Alicja-Malinowska/Meal_Planner/tree/master/testing.md)

## Deployment
This project was developed using the [Visual Studio Code IDE](https://code.visualstudio.com/), committed to Git and pushed to GitHub. 


### How to run this project locally

In order to run this project you will need:

* [Python3](https://www.python.org/download/releases/3.0/) installed
* [PIP](https://pypi.org/project/pip/) installed
* [Git](https://git-scm.com/) installed
* An access to [MongoDB](https://www.mongodb.com/) to store data

To clone this project from GitHub:

1. Follow [this link](https://github.com/Alicja-Malinowska/Meal_Planner) to the Project GitHub repository.
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.

  ```
  https://github.com/Alicja-Malinowska/Meal_Planner.git
  ```
7. Press Enter. Your local clone will be created.

   More about cloning can be found on this [GitHub Help page](https://help.github.com/en/articles/cloning-a-repository).

Next steps:

1. Create a virtual environment so that installations are done only for the project rather than globally. This process will depend on IDE you use. For VS Code intructions can be found on this [Python Enviroments page](https://code.visualstudio.com/docs/python/environments).

2. Use requirements.txt file to install all dependencies.

```
  pip install -r requirements.txt
```

3. Create environment variables:
  * SECRET_KEY - see how to do it in [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
  * MONGO_URI to link to your database. It should look like this:
  
```
  mongodb+srv://root:<password>@firstcluster-5gdmy.mongodb.net/test?retryWrites=true&w=majority
```

4. Make sure that your database is called `meal_planner` and it has two collections `users` and `recipes`.

### Heroku deployment

If you would like to share this app with the world, Heroku platform is one option to do it.

1. Create an account on Heroku and next, create a new app.
2. Requirements.txt and Procfile files are needed for Heroku deployment, and they are included in the project files. If you installed any additional dependencies make sure to update the requirements.txt file:

```
pip freeze > requirements.txt
```

3. Set config vars in Settings on Heroku. You will need to add there your SECRET_KEY and MONGO_URI. Additionally, add IP with value 0.0.0.0 and PORT with value 500. 
4. To see deployment options, go to 'Deploy' tab in your project on Heroku.
5. One of the options is to use [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) - you will need to install it first.
6. You will need to login into Heroku using terminal

```
heroku login
```
7. After all your changes are added and commited in git deploy your app by pushing it to heroku.

```
git push heroku master
```
8. You can see your app by clicking 'Open app' on Heroku platform.

## Credits

### Content

The recipes added in the test account were copied from [Jamie Oliver's website](https://www.jamieoliver.com/recipes/category/course/)


### Media
* The default recipe image and 404 page image were taken from [Pixabay](https://pixabay.com/)
* The recipe images for the test account were taken from [Jamie Oliver's website](https://www.jamieoliver.com/recipes/category/course/)


### Acknowledgements

Thanks to my Mentor [Simen Daehlin](https://github.com/Eventyret) for giving me an idea how to save images uploaded by users. 
