This document explains how the project was tested. Please see full [README.md file](https://github.com/Alicja-Malinowska/Meal_Planner/tree/master/README.md).

# Automated testing

* [W3 HTML validator](https://validator.w3.org/) was used on all the html files. There were some errors displayed but it seems they all were connected to the usage of the templating language, which the validator does not seem to recognise. There was one misplaced closing tag in home.html and one h5 tag that was supposed to be a closing tag but it was an opening tag - these two were fixed. 

* [W3 CSS validator](https://jigsaw.w3.org/css-validator/) was used to check the CSS file. No errors were found. 

# Manual testing 

Different testing accounts were created to test all the features and make sure the data persists between logins for the same account, however the data added on one account is not available in the other. 

## Features testing

* **Fixed navbar**

  **Tests*
  - Click all the links on the navbar and verify if they work as intended
  - Use Google Chrome Dev Tools to check how the navbar looks on different screen sizes and devices
  - Click hamburger menu on mobile view
  - Check if navbar is present on every possible view
  - Scroll up and down the page to see if the navbar stays fixed


  **Results*
  - All the links in the navbar work properly and take a user where it was intended
  - The navbar is collapsed on mobile devices and the side bar shows when the hamburger menu is clicked
  - When scrolling down the navbar is visible for user all the time
  

* **Pages with 'login required'**

  **Tests*

  - Click pages on navbar that require user to be logged in (Recipes and Planner) when no user is logged in
  - Copy links to pages that are not visible on the home page (e.g. recipe view, add recipe form etc) and paste them in the url bar when no user is logged in


 **Results*

  - When Planner or Recipes are clicked on the navbar and a user is not logged in, they are redirected to the login page, and after successful login, back to the selected page

  - When an existing address is typed or pasted (e.g. for a particular recipe) while user is not logged in, they are also redirected to login page and then back to the selected page

* **User-specific content**

  **Tests*

  - Switch between two user accounts with saved and scheduled recipes to see what is displayed for each user on Recipes page, Home page and Planner page
  - Copy one user's recipe address and paste it after logging it as another user

  **Results*

  - On Recipes page only recipes that belong the logged in user are displayed
  - On Home page only recipes planned for the particular day by the logged in user are displayed
  - If a user tries to use a url of another user's recipe, a 404 page is displayed
  - On Planner page a user can only see their recipes scheduled  

### Home page - no login


* **'Register' and 'Login' links**

  **Tests*

  - Click links to see if they work as intended

  **Results*

  - The links work properly and take user to Register and Login pages respectively 

### Register and Login forms

* **Link to sign in in register form and link to register in sign in form**

  **Tests*

  - Click link on Register page to see if it takes user to Login page
  - Click link on Login page to see if it takes user to Register page

  **Results*

  - Both links work properly and take user where they are intended to 

* **Field validation**

  **Tests*

  - Try to submit empty form
  - Try to submit form with only one required field filled, two etc.
  - Try to type an invalid email address
  - Try to type not matching passwords in Registration Form
  - Try to use email address that already was used for registration in Registration Form
  - Try to type incorrect password for registered email address
  - Try to login with an email address that was not registered
  - Try to submit when everything completed correctly
  
  **Results*

  - If required fields are not filled in and user attempts to submt form, the form is not submitted and an error message is displayed informing what user should do

  - If, for whatever reason, the email address is not valid, an error message appears and the form is not submitted

  - If passwords do not match in registration form, an error message appears and the form is not submitted

  - If a user tries to register with an email address that has already been used to register, a message informing about it appears and the for is not submitted

  - If register form validates properly, an account is created and user is able to login with given email address and password

  - If in login form user enters an email address and a password that are not a part of the same user docuement, a message informing that the password or username are wrong appears

  - If there password matched the email address, user is logged in and is redirected to the home page or a page they tried to access before login


* **Automatic login**

  **Tests*

  - Submit a valid registration form to see what happens after

  **Results*

  - After successful registration a user is automatically logged in and taken to the home page

### Home page - logged in user

* **Today recipes**

  **Tests*

  - Schedule recipes for current day, go to the home page and planner to see if they are displayed
  - Logout and log back in to see if this persists 

  **Results*

  - Recipes scheduled for current day are displayed
  - If a user schedules a new recipe fot the current day and goes back to home page, it is displayed in addition to other, earlier scheduled recipes, if any

* **Additional actions when nothing is scheduled**

  **Tests*

  - Register and check if the actions are displayed for a brand new user
  - Log in to a user account with nothing planned for current day and check homepage

  **Results*

  - Links are displayed when nothing is scheduled only
  - Links work and take user where they are intended to
   

### Planner

* **Week view**

  **Tests*

  - Open planner and see if the first day in the table (desktop)/schedule (mobile devices) is the current day and if the following days are the next 6 consecutive days
  - Check if week days match dates

  **Results*

  - Planner shows a view of the current week, with current day as first day
  - Planner displayed as table for desktop and as a schedule, one day under another on mobile view

* **Scheduled recipes**

  **Tests*

  - Schedule a recipe and see if it is displayed in the planner under the correct date and daytime and only there
  - Click the recipe name to see if it takes you to the correct recipe page
  - Click x to see if the recipe, and only it, is removed from the planner
  - Check the database if the date was removed

  **Results*
  
  - If any recipes were scheduled by user, they appear under correct day and daytime in the planner
  - When recipe name is clicked in the planner, user is taken to that recipe page
  - When x icon is clicked next to the scheduled recipe, the recipe is removed from the schedule

* **Next and Previous arrows**

  **Tests*

  - Click the next arrow to see if it takes to the next week, and previous arrow - to the previous week
  - Click next/previous arrow multiple times to see if works as expected
  - Click next/previous arrow multiple times and then click the opposite one (next for previous and vicer versa) to see if it shows correct week
  - Choose a custom date and then use arrows to see of they work properly in this case

  **Results*

  - When 'next' arrow clicked, the planner view changes to the next seven days from current view
  - When 'previous' arrow clicked, the planner view changes to the previous seven days from current view

* **'Current week' button**

  **Tests*

  - Click the button from different views (e.g. when next arrow was used, when custom date was selected, when no action was performed)

  **Results*

  - When 'Current week' button clicked, the planner view goes back to the current week, regardless what view was displayed previously

* **'Custom date' field**

  **Tests*

  - Click on the field to see if datepicker pops up
  - Choose a date on datepicker
  - Choose 'today' on datepicker

  **Results*

  - When clicked a datepicker appears
  - When 'Custom date' selected, the view changes to the week with the selected date as the first day

* **Link to Recipes**

  **Tests*

  - Click the link to see if it works as intended

  **Results*

  - The link works and takes user to the recipes view

### Recipes page

* **Add new recipe button**

  **Tests*

  - Click the button to see if it works as intended

  **Results*

  - The button works and takes a user to 'add recipe' form

* **Search by name**

  **Tests*

  - Try to search without inputting anything
  - Try to search for a string that includes characters other than letter and spaces
  - Try to search for existing recipe name in full
  - Try to search for a part of existing recipe name
  - Try to search for existing recipe name typed using different cases
  - Try to search for existing recipe name adding spaces in the beginning and/or the end
  - Try to search for non-existing recipe name

  **Results*

  - The search returns all the recipes that incude searched string
  - The search is case insensitive and ignores trailing spaces
  - If there are no results matching the searched string, a message informing about it is displayed
  - If a search string cosists of other characters than spaces or letters, an error message is displayed
  - If search button is clicked without any input, a user is prompted that the field cannot be empty and the form is not submitted


* **Search by tag**

  **Tests*

  - Check if all tags for logged in user are displayed in the drop down
  - Check if drop down opens properly and submits on select
  - Check if tags are sorted alphabetically
  - Check if all tags are lower case
  - Select a tag and see if the results are displayed correctly

  **Results*

  - All the user's tags are displayed as select options (lower case) in the drop down, and ordered alphabetically
  - When tag is selected from the drop down, all the recipes that include it as a tag are displayed in a list
    

* **'Back to all recipes' button**

  **Tests*

  - Check if the button is visible when no search was performed
  - Check if the button is visible when a searches for name, and then tag, were performed
  - Click the button to see if all recipes are displayed

  **Results*

  - The button is only visible when a search was performed 
  - When clicked, all the recipes are displayed correctly in a list

* **Recipes collection**

  **Tests*

  - Switch between different accounts with different recipes or none recipes and see if for each they are displayed correctly

  **Results*

  - All the recipes are displayed correctly for the user

* **'Add to planner' button**

  **Tests*

  - Click on the button to see if modal is triggered
  - Try to submit form without any picks
  - Try to submit for with only date or only daytime picked
  - Try to schedule the recipe and check if displayed in planner

  **Results*

  - Modal is triggered when the button is clicked
  - If 'schedule' is clicked and either date or datetime (or both) are not selected, the form is not submitted and the user is informed why
  - When correctly added, a message is displayed that this was added
  - After addition, the recipe is immediately visible in the planner under chosen date and daytime

* **'Edit' button**

  **Tests*

  - Click the button to see if it works as intended

  **Results*

  - The button works correctly and takes user to the edit page

* **'Delete' button**

  **Tests*

  - Click the button to see if modal is triggered
  - Click 'close' on the modal
  - Click 'confirm' on the modal and check if the recipe is still displayed in the recipe list
  - Try to search for the recipe name
  - Try to enter the recipe page using its link
  - Check if the recipe documents exists in the database

   **Results*

  - When clicked, a modal asking for confirmation is triggered
  - When 'Close' clicked within modal, the modal disappears and recipe remains visible
  - When 'Confirm' clicked within modal, the modal disappears and recipe is deleted from database, so it does not display on recipe page, it is also deleted from planner if it was scheduled
  - If a user tries to view the recipe using its link, a 404 page will be displayed

### Add recipe page and Edit recipe page

* **Field validation**

  **Tests*

  - Try to submit empty form
  - Try to submit form without name field filled in
  - Try to use characters other than letters and spaces in the name
  - Try to submit form with empty tag field
  - Try to submit form with tag field filled in without any semicilons present
  - Try to upload a file that is not an image
  - Try to submit valid form 
  - View the recipe to see if it was added/edited and if all the content is displayed properly

  **Results*

  - If name is not provided the form won't submit
  - If a name includes characters other than letters and spaces the form won't submit
  - If there are tag entered but there is no semicolon, the form won't submit and a message will display asking user to make sure they used semicolons to separate their tags
  - If a file is not in png or jpg format, the form is not submitted and an error message appears
  - When the above requirements are satisfied, the form validates succesfully and is submited, user is redirected to the Recipes page and a message appears that the recipe was added
  - The added/edited content is displayed properly



* **Image upload**

  **Tests*

  - Upload a file and see if your image is displayed on Recipes page, on the added/edited recipe page and in the edit form
  - Do not upload a file and see if the default image is displayed instead 

  **Results*

  - If a file is not uploaded, a filename is saved as default.png so that a default image would be added when the recipe is displayed 

## Browser support

* The website was tested and works properly on: Chrome v77, Chrome v77 on Android, Opera v63, Firefox and Edge
* There was an issue on IE11 - all the elements that used JavaScript or jQuery did not work (e.g. modal would not be triggered, drop down didn't show options, collapsed navbar would not show etc.). In the console there was a syntax error in one of the functions. It used arrow functions so I changed it to regular functions, however another error came up: "Object doesn't support property or method 'forEach'". I googled it and found a solution on [GitHub](https://github.com/miguelcobain/ember-paper/issues/1058), where people were reporting issues. I used a polyfill that adds forEach to the node list and the issue was resolved. The application works properly on IE11 now.
* There is a small issue on Safari - the date picker in the modal need to be scrolled because in appeard to be in the modal not on top of it, like it is in other browsers. This problem occured in Chrome while developing but was solverd by setting 'transform: none !important;' for the modal. However, this doesn't seem to have effect in Safari. Unfortunately, I did not have possibility to investigate further as I do not own a device with Safari on it. The issue does not prevent a user to fully utilise the app, but it creats a slightly worse user experience of scheduling a recipe. 

## Responsive design

* The website was tested using Google Chrome Developer Tools to check how it looks like in case of different width and height by choosing 'Responsive' option and resizing the window. Using Chrom Dev Tools, it was also tested how the website looks on: Galaxy S5, Pixel 2, Pixel 2XL, iPhone 5/6/7/8/X, iPad and iPad Pro. In all these views the website is responsive and shows content properly.
* The website was also tested on the following devices: Samsung Galaxy A3, Asus laptop 15", Dell laptop 13.3", a 24" monitor. On all of this devices the website is responsive and shows content properly. 
* On mobiles and tablets the navbar collapses into a 'hamburger menu' and can be expanded to reveal the items by clicking/touching it, on desktop it contains the visisble list of all the items
* The images on the home page before login are displayed in a row on desktop but one under another on mobile devices
* Today recipes are displayed 3 in a row in desktop view, two in a row on tablets and 1 in a row on mobile phones
* Planner is displayed as a table on desktop view and as schedule (one day under another) on mobile devices


# Known bugs/limitations

* **Image upload**

  Image upload is an ectra feature in this project, as it is beyond the scope of the module. However, adding images enhances user experience and therefore is fairly important functionality in this application. Ideally, the images would be saved externally, using another server, however for the scope of this project the solution of saving them in a folder within the project itself seemed sufficient. The biggest issue is that there is no size limit when uploading the image, which can cause an overload and break the app. To fix this, I tried to use Flask's MAX_CONTENT_LENGTH builtin configuration value, however this causd another issue. Whenevr a file was above the set limit, the application would crash and the connection was reset, and should return 403 error. However, writing an 403 error handler didn't work and the app would crash anyway. This seems to be a [known issue](https://github.com/pallets/flask/issues/2188?fbclid=IwAR3yls9p6gEIZcY-cF-RzQm4xmIYQ3OrvloA7asQYrdDRmWgPSMHkM2CTyg) and it is said that when deployed, that should no longer be a problem. However, after deploying it to Heroku, the issue persisted. The issue might occur because of the way modern browsers interact with Werkzeug WGSI. In search of solution for this problem I found [this code snipped](https://www.cocept.io/blog/development/flask-file-upload-connection-reset/?fbclid=IwAR1SSM7KVOc12CqCUpsKq4LwKkeLLDhBBG_p2yYwU5k5JPLPqI69uOV3xyA), however it also did not solve the problem. As this seems to be a quite complex issue, I decided not to investigate further, due to time constraints and not having enough experience with such issues. 

  Another issue is that saved images are not deleted when the recipe is deleted or the image is changed while editing the recipe. As mentioned before, image upload is beyond scope of the project, and therefore I decided to focus on the core functionalities more. However, it is worth noticing that this would become a problem if the project would scale up and would be user by many people. 
