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


![colour-pallettes-image](https://imgur.com/a/KkYcXEG)

### Wireframes/mockups

These are the mockups for some pages:

![planner](https://github.com/Alicja-Malinowska/Meal_Planner/blob/master/mockups/planner.png)
![recipes](https://github.com/Alicja-Malinowska/Meal_Planner/blob/master/mockups/recipes.png)
![recipe view](https://github.com/Alicja-Malinowska/Meal_Planner/blob/master/mockups/recipe-view.png)

All the wireframes can be found in the [mockups folder](https://github.com/Alicja-Malinowska/Meal_Planner/tree/master/mockups).


## Features

All the features were added to enhance the UX and make the website easy to use and intuitive to move around. 
 
### Existing Features

* Fixed navbar

  This element appears on all the pages. It contains a clickable logo that takes user to the homepage, and links to the remaining pages, as well as Register and Login links when there is no logged in user, and a Logout link instead of them, if a user is logged in. The navbar is expanded on large devices and on smaller ones it is collapsed. When tha hamburger menu is clicked a side bar is triggered and the menu links are available for a user to click. When a user clicks a link the sidebar hides automatically. 

* Pages with 'login required'

  Most of the pages require a user to be logged in before they can access them. This is necessary because of the nature of the application - every user should be able to add their own content without it being shared wth others and without seeing content that does not belong to them. When an anonymous user tries to access a page where login is required, they are automatically redirected to the login page, and after successful login they are redirected to the page they tried to access.   

#### Home page - no login

* Screenshots of home page, recipe page and planner page

  The screenshots are there to show an anonymous user what app looks like and what they can expect from it, before they make a decision to register and use the app. This is done to enhance user experience and give the user as much information as possible. Even though the app is free, the user spends their time to fill out registration form, so tbefore they decide to invest this time, they should know what goals they can achieve using the app and this feature provides just that.

* 'Register' and 'Login' links

  The links are situated immediately below the images. They are there so that registering or logging in is an easier decision for the user to make. Although those links can also be found on the navbar, it is more natural for the user to go from top of the page to bottom, and therefore, a user, after seeing the screenshots, sees the links immediately. Otherwise, they would have to look for the links, which might discourage them from proceeding with login, or, particullarly, registration. 

#### Register and Login forms

* Link to sign in in register form and link to register in sign in form

  This is provided in case a user already has an account and by mistake clickd 'register' on the navbar or wanted to register but clicked 'sign in' instead. Thanks to this the user does not have to go back up to the navbar, but can click 'sign in' or 'register' link immediately after they realised that this is not where they need to be. 

* Field validation

  This is achieved with backend validation provided by [WTForms](https://wtforms.readthedocs.io/en/stable/). All fields are required. There are extra validators for email address to make sure it is valid, e.g length restriction. There is also a validator checking if the password and confirmed password are the same in the registration form. If the form does not validate, suitable messages are displayed to inform the user what went wrong and how to fix this.

* Password hashing

  When a user registers their data is stored in the database. However, before the data is sent to the database the password is hashed for security reasons, using sha256. When password is validated, its hashed versions are compared.

* Automatic login

  After successful registration a user is automatically logged in so that they do not need to go to the login page and perfom unnecessary action, and they can access the login-only pages immediately. 

#### Home page - logged in user

* Today recipes

  Recipes scheduled for the day are displayed as cards with the recipe image and its name that is a link to the recipe page. This allows a user to quickly see what they have planned for the day without having to go the planner. They can also access the recipes directly from the home page without going to the recipes page or links in the planner. 

* Additional actions when nothing is scheduled

  If a user has nothing scheduled for the day, a message is displayed that this is the case. Aditionally, there are some actions suggested in a form of links to planner, recipes and add recipe form. This view is what every new user will see, as they will not have anything schedule after they registered, and therefore the suggested actions are particularly important for them, as they give them some guidance how to move around the app before they get familiar with it. 

#### Planner

* Week view

  Planner offers a view of the week (7 consecutive days) starting with the current day. Each day is divided into morning, afternoon and evening for easier planning different meals. On desktop view this is presented in the form of table, where columns are days of the week and rows are daytimes. In the mobile view, this is presented as schedule, where each day is displayed separately in full width. 

* Scheduled recipes
  
  The recipes that were scheduled appear in the planner under specific date and daytime in a form of a link that leads to the recipe page. There is also a delete button next to each recipe displayed in the planner, that removes it from the planner. 

* Next and Previous arrows

  These are located at the top of the page and allow a user to move to tne previous and following weeks views. 

* 'Current week' button

  When the button is clicked, the calendar view returns to the current week view.

* 'Custom date' field

  When clicked, a datepicker is triggered and a user can choose any date within 15-year period (this is datepicker setting and can be changed for longer/shorter period). When the date is chosen, the planner view changes to the week starting with the chosen date. 

* Link to Recipes

  This is placed on top of the planner to inform user where they can schedule their recipes so that they appear in the planner. 

#### Recipes page

* Add new recipe button

  When the button is clicked, a user is taken to a page that contains a form that enables adding a new recipe.

* Search by name

  This allows user to search for a recipe by name. The search is case insensitive and returns all the recipes that include searched string. 

* Search by tag

  A drop down that contains all the tags, alphabetically ordered, that the user used in their recipes. The search returns all the recipes that include the chosen tag. 

* 'Back to all recipes' button

  This button is only visible when a search was performed and is situated below the search results. When clicked, it takes the user back to the view with all the recipes, without any filters. 

* Recipes collection

  This is a list of recipes displayed on the page. Each item has a circle-shaped recipe image and a name of the recipe, which is a link to the recipe page. Each item also has three action buttons that allow schedule the recipe, edit the recipe and delete the recipe. 

* 'Add to planner' button

  When clicked, a modal is triggered. Within the modal, a user chooses a date using datepicker and one of the three options of daytime. Both are required. The success message is flashed when the recipe is added. 

* 'Edit' button

  When clicked, takes a user to edit form page.

* 'Delete' button

  Triggers a modal that informs that the recipe will be permanently deleted and asks for confirmation. User can either confirm, which will result in deletion of the recipe or close, which will not result in any action other than modal being dismissed. If user chooses to delete and confirm, a confirmatory message is flashed. 

#### Add recipe page and Edit recipe page

* Field validation

  Similarly to registation and login forms, this form was also created using WTForms and has backend validation. The only required field is the recipe name, the rest is optional. There is an addtional validator for name - only letters and spaces are allowed. The reason for this is that a regex search is used to search for recipes name, and if a user would some regex specifi characters (e.g '*') this would cause the app to crash. User is informed about it in placeholder and an errors message is displayed when they try to submit a recipe with a name that has other characters. When file is being uploaded, a check is performed to see if the files has jpg or png format. If not, the validation fails and the recipe is not added. There is also a custom validator written for the tags field that checks if there is at least one semicolon included in the string if the field is not empty. The tags are required to be separated by semicolons, and there is a note in the form that informs a user about it. If a user tries to submit tags without a least one semicolon, an error message appears so that they can quickly learn how to insert the tags. 


* Image upload

  When a user uploads an image of recipe, if it's a valid file format, the file is renamed using uuid to ensure that there are no two files with the same name file name. This is important, as the filename is saved in the database and is used to display the image. The file itself is saved on the app server, in the images folder. 


### Features Left to Implement

* User account actions

  For this project to be fully functional registration/login feature was essential. However, there were no requirements for this for this project, as this is out of the scope of the module. Therefore, the registration-login system is fairly simple in the application. A user creates an account and can login using the given credentials. The features that could be further implemented are: possibility to update password, edit profile and delete profile. 

* Adding recipes directly from planner

  Right now recipes are added to the planner from recipes list or from a recipe page. A new feature could allow user to click in the planner and be able to search for a recipe and add it to the day and daytime that was clicked.

* Shopping list

  Another page could be added that would include a shopping list view. A user could add ingredients from selected recipe to the list, as well as type their own items.

* Recipe import

  This feature would make it possible to import recipes from popular recipe websites, like AllRecipes, so that the user doesn't have to copy and paste if they want to save a recipe that is already on one of these websites. 

## Database

MongoDB was used to store data for this application. As there are no complex relationships between different entities, a non-relational database seemed to be suitable choice for data storage.

### Collections

There are two collections created for the project: user and recipes.

#### Users

| Key           | Data type     |
| ------------- |:-------------:|
| first_name    | String        |
| last_name     | String        |
| password      | String(hashed)|

#### Recipes

| Key           | Data type     |
| ------------- |:-------------:|
| name          | String        |
| ingredients   | Array         |
| servings      | String        |
| instructions  | Array         |
| tags          | Array         |
| image         | String        |
| owner         | String        |
| dates         | Array         |


## Technologies Used

* Python
* HTML
* CSS
* jQuery
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - to handle http requests and render pages
* [Flask-login](https://flask-login.readthedocs.io/en/latest/) - to provide login functionality
* [WTForms](https://wtforms.readthedocs.io/en/2.3.x/) - for forms validation and rendering
* [MongoDB](https://www.mongodb.com/) - used to store and retrieve data
* [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - PyMongo provides a way for Python to work with MongoDB and Flask-Pymongo makes it easier to use PyMongo within Flask framework
* [PassLib](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.html) - used to hash and compare hashed passwords
* [Materialize](http://archives.materializecss.com/0.100.2/) - used for styling based on Matrial Design 
* [Visual Studio Code](https://code.visualstudio.com/) - an IDE used to write the code
* [Git](https://git-scm.com/) - used for version control



## Testing

### Automated testing

* [W3 HTML validator](https://validator.w3.org/) was used on all the html files. There were some errors displayed but it seems they all were connected to th usage of the templating language, which the validator does not seem to recognise. There was one misplaced closing tag in home.html and one h5 tag that was supposed to be a closing tag but it was an opening tag - these two were fixed. 

* [W3 CSS validator](https://jigsaw.w3.org/css-validator/) was used to check the CSS file. No errors were found. 

### Manual testing 

#### Features testing

* Fixed navbar

  - All the links in the navbar work properly and take a user where it was intended
  - The navbar is collapsed on mobile devices and the side bar shows when the hamburger menu is clicked
  - When scrolling down the navbar is visible for user all the time
  

* Pages with 'login required'

  - When Planner or Recipes are clicked on the navbar and a user is not logged in, they are redirected to the login page, and after successful login, back to the selected page

  - When an existing address is typed or pasted (e.g. for a particular recipe) while user is not logged in, they are also redirected to login page and then back to the selected page

* User-specific content

  - On Recipes page only recipes that belong the logged in user are displayed
  - On Home page only recipes planned for the particular day by the logged in user are displayed
  - If a user tries to use a url of another user's recipe, it will not be displayed
  - On Planner page a user can only see their recipes scheduled  

#### Home page - no login


* 'Register' and 'Login' links

  - The links work properly and take user to Register and Login pages respectively 

#### Register and Login forms

* Link to sign in in register form and link to register in sign in form

  - Both links work properly and take user where they are intended to 

* Field validation

  - If required fields are not filled in and user attempts to submt form, the form is not submitted and an error message is displayed informing what user should do

  - If, for whatever reason, the email address is not valid, an error message appears and the form is not submitted

  - If passwords do not match in registration form, an error message appears and the form is not submitted

  - If a user tries to register with an email address that has already been used to register, a message informing about it appears and the for is not submitted

  - If register form validates properly, an account is created and user is able to login with given email address and password

  - If in login form user enters an email address and a password that are not a part of the same user docuement, a message informing that the password or username are wrong appears

  - If there password matched the email address, user is logged in and is redirected to the home page or a page they tried to access before login


* Automatic login

  - After successful registration a user is automatically logged in and taken to the home page

#### Home page - logged in user

* Today recipes

  - Recipes scheduled for current day are displayed
  - If a user schedules a new recipe fot the current day and goes back to home page, it is displayed in addition to other, earlier scheduled recipes, if any

* Additional actions when nothing is scheduled

  - Links are displayed when nothing is scheduled only
  - Links work and take user where they are intended to
   

#### Planner

* Week view

  - Planner shows a view of the current week, with current day as first day
  - Planner displayed as table for desktop and as a schedule, one day under another on mobile view

* Scheduled recipes
  
  - If any recipes were scheduled by user, they appear under correct day and daytime in the planner
  - When recipe name is cliced in the planner, user is take to that recipe page
  - When x icon is clicked next to the scheduled recipe, the recipe is removed from the schedule

* Next and Previous arrows

  - When 'next' arrow clicked, the planner view changes to the next seven days from current view
  - When 'previous' arrow clicked, the planner view changes to the previous seven days from current view

* 'Current week' button

 - When 'Current week' button clicked, the planner view goes back to the current week, regardless what view was displayed previously

* 'Custom date' field

  - When clicked a datepicker appears
  - When 'Custom date' selected, the view changes to the week with the selected date as the first day

* Link to Recipes

  - The link works and takes user to the recipes view

#### Recipes page

* Add new recipe button

  - The button work and takes a user to 'add recipe' form

* Search by name

  - The search returns all the recipes that incude searched string
  - The search is case insensitive and ignores trailing spaces
  - If there are no results matching the searched string, a message informing about it is displayed
  - If a search string cosists of other characters than spaces or letters, an error message is displayed
  - If search button is cliked woithout any input, a user is prompted that the field cannot be empty and the form is not submitted


* Search by tag

  - All the user's tag are displayed as select options in the drop down, and ordered alphabetically
  - When tag is selected from the drop down, all the recipes that include it as a tag are displayed in a list
    

* 'Back to all recipes' button

  - The button is only visible when a search was performed 
  - When clicked, all the recipes are displayed correctly in a list

* Recipes collection

  - All the recipes are displayed correctly for the user

* 'Add to planner' button

  - Modal is triggered when the button is clicked
  - If 'schedule' is clicked and either date or datetime (or both) are not selected, the form is not submitted and the user is informed why
  - When correctly added, a message is displayed that this was added
  - After addition, the recipe is immediately visible in the planner under chosen date and daytime

* 'Edit' button

  - The button works correctly and takes user to the edit page

* 'Delete' button

  - When clicked, a modal asking for confirmation is triggered
  - When 'Close' clicked within modal, the modal disappears and recipe remains visible
  - When 'Confirm' clicked within modal, the modal disappears and recipe is deleted from database, so it does not display on recipe page, it is also deleted from planner if it was scheduled
  - If a user tries to view the recipe using its link, a 404 page will be displayed

#### Add recipe page and Edit recipe page

* Field validation

 - If name is not provided the form won't submit
 - If there are tag entered but there is no semicolon, the form won't submit and a message will display asking user to make sure they used semicolons to separate their tags
 - If a file is not in png or jpg format, the form is not submitted and an error message appears
 - When the above requirements are satisfied, the form validates succesfully and is submited, user is redirected to the Recipes page and a message appears that the recipe was added



* Image upload

   - If a file is not uploaded, a filename is saved as default.png so that a default image would be added when the recipe is displayed 

#### Browser support

* The website was tested and works properly on: Chrome v77, Chrome v77 on Android, Opera v63, Firefox and Edge
* There was an issue on IE11 - all the elements that used JavaScript or jQuery did not work (e.g. modal would not be triggered, drop down didn't show options, collapsed navbar would not show etc.). In the console there was a syntax error in one of the functions. It used arrow functions so I changed it to regular functions, however another error came up: "Object doesn't support property or method 'forEach'". I googled it and found a solution on [GitHub](https://github.com/miguelcobain/ember-paper/issues/1058), where people were reporting issues. I used a polyfill that adds forEach to the node list and the issue was resolved. The application works properly on IE11 now.
* There is a small issue on Safari - the date picker in the modal need to be scrolled because in appeard to be in the modal not on top of it, like it is in other browsers. This problem occured in Chrome while developing but was solverd by setting 'transform: none !important;' for the modal. However, this doesn't seem to have effect in Safari. Unfortunately, I did not have possibility to investigate further as I do not own a device with Safari on it. The issue does not prevent a user to fully utilise the app, but it creats a slightly worse user experience of scheduling a recipe. 

#### Responsive design

* The website was tested using Google Chrome Developer Tools to check how it looks like in case of different width and height by choosing 'Responsive' option and resizing the window. Using Chrom Dev Tools, it was also tested how the website looks on: Galaxy S5, Pixel 2, Pixel 2XL, iPhone 5/6/7/8/X, iPad and iPad Pro. In all these views the website is responsive and shows content properly.
* The website was also tested on the following devices: Samsung Galaxy A3, Asus laptop 15", Dell laptop 13.3", a 24" monitor. On all of this devices the website is responsive and shows content properly. 
* On mobiles and tablets the navbar collapses into a 'hamburger menu' and can be expanded to reveal the items by clicking/touching it, on desktop it contains the visisble list of all the items
* The images on the home page before login are displayed in a row on desktop but one under another on mobile devices
* Today recipes are displayed 3 in a row in desktop view, two in a row on tablets and 1 in a row on mobile phones
* Planner is displayed as a table on desktop view and as schedule (one day under another) on mobile devices


### Known bugs/limitations

* Image upload

  Image upload is an ectra feature in this project, as it is beyond the scope of the module. However, adding images enhances user experience and therefore is fairly important functionality in this application. Ideally, the images would be saved externally, using another server, however for the scope of this project the solution of saving them in a folder within the project itself seemed sufficient. The biggest issue is that there is no size limit when uploading the image, which can cause an overload and break the app. To fix this, I tried to use Flask's MAX_CONTENT_LENGTH builtin configuration value, however this causd another issue. Whenevr a file was above the set limit, the application would crash and the connection was reset, and should return 403 error. However, writing an 403 error handler didn't work and the app would crash anyway. This seems to be a [known issue](https://github.com/pallets/flask/issues/2188?fbclid=IwAR3yls9p6gEIZcY-cF-RzQm4xmIYQ3OrvloA7asQYrdDRmWgPSMHkM2CTyg) and it is said that when deployed, that should no longer be a problem. However, after deploying it to Heroku, the issue persisted. The issue might occur because of the way modern browsers interact with Werkzeug WGSI. In search of solution for this problem I found [this code snipped](https://www.cocept.io/blog/development/flask-file-upload-connection-reset/?fbclid=IwAR1SSM7KVOc12CqCUpsKq4LwKkeLLDhBBG_p2yYwU5k5JPLPqI69uOV3xyA), however it also did not solve the problem. As this seems to be a quite complex issue, I decided not to investigate further, due to time constraints and not having enough experience with such issues. 

  Another issue is that saved images are not deleted when the recipe is deleted or the image is changed while editing the recipe. As mentioned before, image upload is beyond scope of the project, and therefore I decided to focus on the core functionalities more. However, it is worth noticing that this would become a problem if the project would scale up and would be user by many people. 


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
4. In your local IDE open Git Bash.
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
2. Requirements.txt and Procfile files are needed for Heroku deployment, so make sure they exists.
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
