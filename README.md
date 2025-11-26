# My Assistance Website
#### Video Demo:  <https://youtu.be/2TwIT-8YfTQ>
#### Description:

In every single of html files, I use bootstrap for design.
in My project folder I have another two folder(Static and Templates)

Static: that include 2 images one for login page and one for background.
one js file: index.js
one css file: style.css

Templates: that include 6 files.

1. Layout.html file:
It’s a main layout file and base html file for frontend view. it include bootstrap link and script and google fonts.
I use bootstrap and google font for UI and use Jinja for substitution.
I define two jinja block in this file one for title and another for main block to change everything I want in different html file between body tags.
I use two if statements one for change the link in navigation bar when user logged in and another for flash messages that appear between navigation bar and main body.

2. login.html file:
this file extends the layout file to reduce redundancy and I just change the body of layout.
this is the first page users can see to log in to the website.
I use a form tag and two input one for username and another for password and one button to get users inputs and submit them through POST method.
Also I put a register link on the navbar to register.

3. register.html file:
this page also extends from layout file.
here I use a form with four inputs for username, password,
Password conformation and city and also one button to submit user's inputs whit POST method.

4. index.html file:
this file extends the layout file.
the first page user can see is this file and it include 3 columns that created with bootstrap feature.

First column for weather that shows user city, icon of weather condition, weather degree in Celsius and brief description for weather condition. here I use jinja to bring in front-end name of the city, temperature, weather description and id code that I use in image tag to change icon depend on each weather.

Second column for adding new task to user to-do list that include one form with one input and one button that submit user's task through POST method.

Third column for list of to-do list tasks. That I use for loop with Jinja that make a div tag include label and check box in it.
every time user add a new task, it will appear in this column.

5. profile.html file:
this file extends the layout file.
this file is for change password or change the city of user.
it include 4 inputs and one button that submit users input through POST method.
here through jinja I bring to front-end the name that user use for username.
this page include 2 column.
First for some tips and second for users inputs.

6. done.html file:
this file extends the layout file.
this file is for delete your tasks (done tasks). it has a select tag that with Jinja I use a for loop
for show every task in this group list and user can choose a task and click delete to delete it that uses POST method.


7. style.css file:
This file is for styling html files.
Here I use tags, classes and IDs. In body I change the font-family
Background image, size position, attachment and repeat.
Give one rem margin from top for every buttons and 20 rem margin for log-in form from top,
And 10 pixel border radius for login image and its div.
Also define a class for making checkbox checked and become gray.

8. index.js file:
This file includes JavaScript codes.
First code block is for showing real-time time and date.
Second code block is for draw a line on tasks that marked checked.

9. todo.db file:
It’s my database file that include two tables one for users and one for tasks.

10. app.py file:
This is our backend file that uses Flask framework.
Here I use lots of functions for every single of website pages such as
Index () function,
That is the function when user logged-in in website called to show index.html file and get open weather API,
To show weather of each city user entered or add new task to job table.
Register function is for get users inputs and post it in users table it also make users password hash.
Login function is for get user inputs (username and password) and compare it with user database to check if user already
Registered (the username and password already exist) allow to user enter or log-in.
When user logged in I equal session module that I import from Flask library to the ID of user table (ID column is auto-generated).
So website remember user anytime he/she log-in and don’t show to him/her log-in page again, unless user click on the logout
On the navigation bar that called Logout function, this function clear the session and back to login page.
Profile function is for change password and city of user. That gonna compare users old password and if it exist
In users table it gonna replace new password with old one. And also gonna replace old city with new one.
Done function get what user chooses and delete it from job table and return to index file.


