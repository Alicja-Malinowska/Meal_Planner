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


The page navigation is designed to be intuitive and enable a user to perform required actions quickly and easily. The design offers a user multiple places from where they can view their recipes and perform actions connected to them (delete, edit, schedule, add etc). The overall design is meant to be simple and clear without unnecessary distractions. The colors were chosen using [Material Design colour picking tool](https://material.io/design/color/the-color-system.html#tools-for-picking-colors). The primary colour is #880E4F and the rest were chosen from the primary and complemetary palletes as shown below. 

<div align="center">
    <img src="https://imgur.com/a/KkYcXEG" alt="Colour palletes image"/>
</div>
<br>


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

  A drop down that contains all the tags that the user used in their recipes. The search returns all the recipes that include the chosen tag. 

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

  Similarly to registation and login forms, this form was also created using WTForms and has backend validation. The only required field is the recipe name, the rest is optional. When file is being uploaded, a check is performed to see if the files has jpg or png format. If not, the validation fails and the recipe is not added. There is also a custom validator written for the tags field that checks if there is at least one semicolon included in the string if the field is not empty. The tags are required to be separated by semicolons, and there is a note in the form that informs a user about it. If a user tries to submit tags without a least one semicolon, an error message appears so that they can quickly learn how to insert the tags. 


* Image upload

  When a user uploads an image of recipe, if it's a valid file format, the file is renamed using uuid to ensure that there are no two files with the same name file name. This is important, as the filename is saved in the database and is used to display the image. The file itself is saved on the app server, in the images folder. 


### Features Left to Implement

* User account actions

  For this project to be fully functional registration/login feature was essential. However, there were no requirements for this for this project, as this is out of the scope of the module. Therefore, the registration-login system is fairly simple in the application. A user creates an account and can login using the given credentials. The features that could be further implemented are: possibility to update password, edit profile and delete profile. 


## Technologies Used

* HTML
* CSS
* jQuery
* [Bootstrap](https://getbootstrap.com/) - used for the responsive design, collapsable navbar, modals and collapsed text
* [Visual Studio Code](https://code.visualstudio.com/) - an IDE used to write the code
* [Git](https://git-scm.com/) - used for version control
* [Font Awesome](https://fontawesome.com/) - all the icons on the website 


## Testing

### Automated testing

* [W3 HTML validator](https://validator.w3.org/) was used on both html files. There was an error pointing to the same id's in the form in the contact section and the form in the modal. The id's' names in the modal have been changed. Another error was an illegal character ("|") in the link to Google Fonts (the link was generated from there). To fix this I removed the link from the head and added @import in the CSS file. Since there are four html files and one CSS file this is a better solution. 

* [W3 CSS validator](https://jigsaw.w3.org/css-validator/) was used to check the CSS file. No errors were found. 

### Manual testing 

#### Features testing

* All the navigation links take a user to the assigned section.
* When the logo is clicked the page scrolls to the top.
* When Polish flag is clicked, a Polish version is displayed. When British flag is clicked, an English version is displayed.
* Book now button opens a modal with a contact form. When the sumit button is pressed on an empty form an error message appears. Similarly if any of the fields is empty (all are rquired) or when email address doesn't have a proper format (no @). The form in the Contact section behaves simiarly. When it is sumitted correctly, the modal closes.  
* The reviews link opens in a new tab and takes a user to a Google page containing the reviews.
* When the arrow-down icon is clicked on the homepage it takes a user to the further part of the section (similarly in What to Expect section).
* More about button on the cards takes a user to What to Expect section where they can read more about the test
* The phone link/icon when touched on mobile or tablet dials the number. On desktop it is possible to open it using several applications (e.g. Skype -  dependant on the individual user settings).
* When download icons are clicked/touched a file is being downloaded.
* When arrows in the pricing sections are clicked they expand and reveal more details about the price category.
* When the email address/icon is clicked/touched a new email message opens (or suggested apps to open it with - dependant on the individual user settings)
* When the contact form in the 'Contact' section is completed and submitted correctly a success page appears. This was not implemented with the modal because it would defeat the whole purpose of the modal for UX.
* When Facebook icon clicked/touched a new tab opens with the company's Facebook page.


#### Browser support

* The website was tested and works properly on: Chrome v77, Chrome v77 on Android, Opera v63
* On Firefox there was an issue with the flipcards on desktop - the cover of the card would still be visible when flipped. This was solved using a solution from [Stack Overflow](https://stackoverflow.com/questions/9604982/backface-visibility-not-working-properly-in-firefox-works-in-safari). After this fix the flipcards work properly on Firefox v69
* On Edge there was an issue with the background-blend-mode which resulted in pictures on the flipcards not being 'dimmed' and text not being readable. To fix this I decided not to display the background pictures on the cards on Edge and I used the idea from the [fastcodefix](https://www.fastcodefix.com/fix-for-internet-explorer-and-edge-css-layout-problems/) website to do that. After this fix flipcard work properly on Microsoft Edge v44, but the images are not displayed. 
* On IE the flipcards didn't work properly at all so I decided to keep them static as they are on tablet and mobile. To do this I applied the solution I found on [Stack Overflow](https://stackoverflow.com/questions/48412244/apply-css-to-all-browsers-except-ie-using-media-query/48422293). After this fix the cards work properly on Internet Explorer v11, although they are not animated in the desktop view, they also do not have background images in any view. 
* The flipcards do not work properly on Safari and Chrome on Mac - the content doesn't show when the card is flipped. Although I tried to fix this bug I could not find a good solution. As I work in Windows environment I did not have proper resources to investigate this further.

#### Responsive design

* The website was tested using Google Chrome Developer Tools to check how it looks like in case of different width and height by choosing 'Responsive' option and resizing the window. Using Chrom Dev Tools, it was also tested how the website looks on: Galaxy S5, Pixel 2, Pixel 2XL, iPhone 5/6/7/8/X, iPad and iPad Pro. In all these views the website is responsive and shows content properly.
* The website was also tested on the following devices: Samsung Galaxy A3, Asus laptop 15", Dell laptop 13.3", a 24" monitor. On all of this devices the website is responsive and shows content properly. 
* On mobiles and tablets the navbar collapses into a 'hamburger menu' and can be expanded to reveal the items by clicking/touching it, on desktop it contains the visisble list of all the items
* The pictures in the 'About' section are situated below/above the text description on mobile, while on bigger screens they are next to it.
* The cards in the 'Services' section are situated one under another for mobile view, for most of the tablets (medium size screens) they are displayed in rows of two, on bigger screens (bigger tablets and desktops) they show it 2 rows of 3 items. On desktop (very large screens) the cards become flipcards that have the cover with the category name and when hover over they flip and show the content.
* The subsections in 'What to expect' section are aligned one under another on mobile and on bigger screens they are next to each other.
* The files for download and their descriptions in the 'For GP surgries/companies' section are one under another on mobile view and to the left there is one big document icon, on bigger screens thy are next o wach other and on the left of each there is a document icon.
* The map in the 'Contact' section is situated below the address on mobile view and on bigger screens it is on the right side of the address and is also bigger.
* An additional 'reviews' item on the footer is hidden on the mobile view and appears on bigger screens.

#### Accessibility

* I downloaded an NVDA screen reader to check the accessibility for peope with impaired vision. As an unexperienced user I was unable to use the exact controls as everyday users do, however I managed to test how the screen reader behaves on the website on the basic level. Based on this I added additional aria-labels (there were some already existing) for the scroll down arrow buttons, expand arrow buttons in the pricing section and number and phone links. This was checked with English speaking reader on the English version. The Polish version was adjusted accordingly based on the changes to the English version. 
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

* The contrast between the background colours and the text colours should be sufficient for people with impaired ability to see colours

#### Peer code review

* It was pointed out to me that in the 'Why Us' subsection of Home the last icon reaches outside its container. This was not the case on my devices but after investigating using Chrom Dev Tools I noticed it happens when the height of the device is smaller. The bug was caused by setting the height to 100vh. Changing it to min-height: 100vh solved the problem. 
* Some reviewers noticed that the navigation bar on mobile mode wouldn't collapse when an item was selected. This wasn't the best user experience as they would have to touch the hamburger menu button again to be able to fully see the site. This was fixed using JavaScript code.
* It was suggested that I should compress my images for better performance which I did using [this tool](https://tinyjpg.com/).

### Known bugs/limitations

* Image upload

  Image upload is an ectra feature in this project, as it is beyond the scope of the module. However, adding images enhances user experience and therefore is fairly important functionality in this application. Ideally, the images would be saved externally, using another server, however for the scope of this project the solution of saving them in a folder within the project itself seemed sufficient. The biggest issue is that there is no size limit when uploading the image, which can cause an overload and break the app. To fix this, I tried to use Flask's MAX_CONTENT_LENGTH builtin configuration value, however this causd another issue. Whenevr a file was above the set limit, the application would crash and the connection was reset, and should return 403 error. However, writing an 403 error handler didn't work and the app would crash anyway. This seems to be a [known issue](https://github.com/pallets/flask/issues/2188?fbclid=IwAR3yls9p6gEIZcY-cF-RzQm4xmIYQ3OrvloA7asQYrdDRmWgPSMHkM2CTyg) and it is said that when deployed, that should no longer be a problem. However, after deploying it to Heroku, the issue persisted. The issue might occur because of the way modern browsers interact with Werkzeug WGSI. In search of solution for this problem I found [this code snipped](https://www.cocept.io/blog/development/flask-file-upload-connection-reset/?fbclid=IwAR1SSM7KVOc12CqCUpsKq4LwKkeLLDhBBG_p2yYwU5k5JPLPqI69uOV3xyA), however it also did not solve the problem. As this seems to be a quite complex issue, I decided not to investigate further, due to time constraints and not having enough experience with such issues. 

  Another issue is that saved images are not deleted when the recipe is deleted or the image is changed while editing the recipe. As mentioned before, image upload is beyond scope of the project, and therefore I decided to focus on the core functionalities more. However, it is worth noticing that this would become a problem if the project would scale up and would be user by many people. 


## Deployment
This project was developed using the [Visual Studio Code IDE](https://code.visualstudio.com/), committed to Git and pushed to GitHub. 

To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken:

1. Log into GitHub.
2. From the list of repositories on the screen, select Alicja-Malinowska/Milestone1.
3. From the menu items near the top of the page, select Settings.
4. Scroll down to the GitHub Pages section.
5. Under Source click the drop-down menu labelled None and select Master Branch
6. On selecting Master Branch the page is automatically refreshed, the website is now deployed.
7. Scroll back down to the GitHub Pages section to retrieve the link to the deployed website.

### How to run this project locally

To clone this project from GitHub:

1. Follow this link to the Project GitHub repository.
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.

  ```
  git clone https://github.com/Alicja-Malinowska/Milestone1.git
  ```
7. Press Enter. Your local clone will be created.

More about cloning can be found on this [GitHub Help page](https://help.github.com/en/articles/cloning-a-repository).


## Credits

### Content
The text was entirely written by me, both in Polish and English.

Psychotest was a real company that I used to run and it had a website built in WordPress. The website does not exist anymore and I do not have access to it either. I used texts in Polish that I had saved in word files when I had been preparing the content for the website. I changed some content and added some new content. I translated everything to English. The layout of the webiste is different than the WordPress website, although the sections are similar. I no longer have the access to the WordPress page and I do not have any images of the old website, I only rely on my memory of it and I was not attempting to recreate it in terms of layout and design.

### Tools used

* [CSS Gradient](https://cssgradient.io/) - background gradient created using this website
* [ColorSpace](https://mycolor.space/) - this tool was used to match the colors used on the webiste to the logo
* [Autoprefixer](https://autoprefixer.github.io/) - used to add prefixes for the code to work on different browsers
* [Tiny JPG](https://tinyjpg.com/) - used to compress the images to improve performance

### Media
* The flag images, truck hero image and cards images come from [Pixabay](https://pixabay.com/)
* The images from the 'About' section are mine
* The fonts were imported from [Google Fonts](https://fonts.google.com/)

### Acknowledgements

Thanks to my Mentor [Simen Daehlin](https://github.com/Eventyret) for suggesting to make it a one-page scrollable website and for giving me idea to display my contact form as a modal. Thanks to [Anthony O'Brien](https://github.com/auxfuse) for giving me a piece of JavaScript Code to provide better UX with the collapsable navigation bar on mobile devices. 
