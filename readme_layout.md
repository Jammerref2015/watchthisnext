# Never Judge a Book
## Welcome! Please click the below image, I hope you enjoy it.

[![Book Image](static/images/flickedBook.jpg)](https://never-judge-book.herokuapp.com/)

## Table of content
* [Overview](#Overview)
* [UX](#UX)
* [Wireframes](#Wireframes)
* [Features](#Features)
* [Technologies Used](#Technologies-Used)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credits](#Credits)
## Overview

This is a mobile-first site that is designed for users to easily view book reviews from other users and also add a review themselves. It is aesthetically pleasing due to the user's ability to easily add an image to their reviews by simply copying a link for their image and pasting it into the write review form. It is also an easy site to navigate around due to its simplicity, which should keep the user's attention. For book lovers, of all ages, this site is perfect as it is not complicated by unnecessary details and gives the user the essential information.



## UX

### Ideal Users
People who are passionate about movies. 

### User Stories

## Wireframes 


## Features
### Existing Features

### Login/Register 

#### Register
#### Login
#### Login/Register page content

### Book Review 


### Write Review

### Profile

### Features left to implement

## Technologies Used



* [BSON](https://www.mongodb.com/json-and-bson)
  * BSON is the binary encoding of JSON-like documents that MongoDB uses when storing documents in collections



## Database Used

## Testing
Testing can be accessed [here](TESTING.md)

## Deployment
### Deploying Online 
View live page: https://never-judge-book.herokuapp.com/

To deploy this project online (online IDE - like gitpod) follow the following steps:

1. Clone this repository and initialize your repository - open the repository
2. Creat an env.py file where you created your variables (IP, PORT, MONGO_URI, MONGO_DBNAME, and a secret key for flashed messages)
3. Used the CLI to install all of the frameworks and collect them inside the requirements.txt file
    * You can do this by typing "pip3 install -r requirements.txt" in your command-line interface
4. Create a Procfile for Heroku stating that it should run app.py as a web app and use Python as the language
5.  Create your MongoDB database and collections, populated it with data, and connected to it by following the steps in MongoDB
6. Sign up to Heroku and go to https://dashboard.heroku.com/apps and created your new app
7. Connect to your GitHub repository via Heroku
8. Go to settings and in Config Vars, click Reveal Config Vars :
    * IP = 0.0.0.0
    * PORT = 5000
    * MONGO_DBNAME is book_review
    * MONGO_URI is mongodb+srv://<username>:<password>@myfirstclust.tmrem.mongodb.net/<database-name>?retryWrites=true&w=majority
    * SECRET_KEY is a password chosen by you
9. Connect to a branch you want to deploy from and the project will be deployed to the Heroku
10. Click on the 'view' button to view the live deployed project

### Local Deployment
To deploy this project locally I followed the following steps:

You will need to install the following to run this locally:

* An IDE such as Microsoft Visual Studio Code
* Python3 to run the application
* PIP to install all app requirements
* MongoDB to develop your database either locally or remotely on MongoDB Atlas.
* GIT for cloning and version control

When deploying locally, you will need to follow the below steps:

* Clone this GitHub repository by either clicking the green Clone or download button and downloading the project as a zip-file (remember to unzip it first), or by entering the following into the Git CLI terminal:
    * git clone https://github.com/Richiefinegan11/bookReview.git
* Navigate to the correct file location after unpacking the files
    * cd <path to folder>
* Create a .env file with your credentials. (The same as deploying the project online)
* Install all requirements from the requirements.txt file using this command:
    * sudo -H pip3 -r requirements.txt
* Sign up for a free account on MongoDB and create a new Database called food The Collections in that database should be as stated in the interaction design
* You should now be able to launch your app using the following command in your terminal:
    * flask run
* The app should now be running on localhost on an address similar to http://127.0.0.1:5000. Simply copy/paste this into the browser of your choice!

## Credits 

### Content 
  * The content for this site was taken from the project idea section, suggested by the code institute.
  * All text used for this is my own

### Media 

### Acknowledgements



### Disclaimer
The content of this Website is for educational purposes only