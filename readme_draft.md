
  

# Watch this next. - Creating a movie database for the movies we love to watch!

  

  

![readme image](/assets/images/readme_image.jpg)

  

  

A live demo can be found [here](http://watchthisnext.herokuapp.com/)

  

  

'Watch this next' is a app that allows users to curate movie reviews which are referred to as 'movies'.

  

As a lover of films, I wanted to create something that involved movies. The aim was to create a site where movie buffs could add reviews of a film they would recommend. 

## Contents ##
#### UX

* Project Goals

* User Goals

* User Stories

* Site Owner Goals

* User Requirements and Expectations

* Design Choices

* Fonts

* Icons

* Colours

* Technologies

#### Features

* Features that have been developed

 * Features that will be implemented in the future
 
* Testing

* Bugs

* Deployment

* Credit

## UX

### Project Goals ###

The **goal** for this project was to make an easy to use site that would allow a user to create a film review that they could share with other film buffs. A user could use the site to search for a list of comedies and possibly find a movie that they are interested in watching. Information about a particular movie is available including the platform that the movie was viewed. This would let  the vistor to the the site know how they could access the movie.

-  **Wireframes** for this project are available in the Mockups folder.

### User Goals ###

* Provide users with a place to add reviews for movies they have seen recently.

- Provide users with an ever growing list of movies that may inspire them when searching for a movie to watch.


### User Stories ###

* As a **user**, I want a **fun and interactive application that will allow me to share movie reviews** so I will **discover new movies**.

* As a **user**, I want to discover movies that i may not have seen.

As a **user**, I want to be able to search for a movie or maybe search for a genre of movies. 

  
### Site Owner Goals ###

* As a **site owner**, I want to give users a place where users can add movie reviews.

* As a **site owner**, I want to give users the abilty to search a database of movie reviews

* As a **site owner**, I want to give users a place where they can share movie reviews. (Currently only possible by emailing/messaging link to the movie).

  
### User Requirements and Expectations ###

**Requirements**

* Content displayed in a **visually appealing** manner.

* A visual cue that tells me when I have completed an action such as adding a movie.

* Functions of the site clearly labelled and easy to access.

**Expectations**

* Content is **visually satisfying** and presented.

* The features of the site are explained clearly and simply.

* Buttons are clear and easy to read.

- Forms are clear and easy to understand.

  
### Design Choices ###

**Fonts**

- I wanted the navbar to reference the movie 'Jaws'. In order to achive this i obtained an open source font [amity_jack].(https://www.dafont.com/amity-jack.font)

- I then used a converter from fontsquirrel.com to enable web embedding. (https://www.fontsquirrel.com/tools/webfont-generator)

- The color for the fonts on the navbar was taken from the movie poster for Jaws.

- For the main content and footer I decided on Google Fonts [Nunito](https://fonts.googleapis.com/css2?family=Nunito&display=swap). I felt that this font had a certain aesthetic to it that fitted into the site.

  

**Colours**

- The colour scheme was based on colours used in a movie poster for 'Jaws' with colours eyedropped from the movie poster.

- #384345 was used for the main background. [#384345](https://www.color-hex.com/color/384345)

- #617478 was used for the navbar and footer. [#617478](https://www.color-hex.com/color/617478)

- Button colours for the search field were red for cancel and blue for submit. These colors were the standard materializecss colors. 

- Button colour for the log-in form is blue. Standard materializecss color. 

- Button color for 'delete movie' on the movie review cards is[#26a69a](https://www.color-hex.com/color/26a69a).

  
**Images**


- The majority of the images on the site are user submitted and therefore vary in many different ways.

- The background for the 'helper' modal on the add movie form features a still image from 'Back To The Future' which was converted to black and white with the text being white which allowed it to stand out more.

- A placeholder image was created in the case that a user did not submit an image or user submitted image was no longer available at the address given.

  

## Wireframing ##

 
Balsamiq was used for wireframing. This produced some basic wireframes, which were used to get an overall feeling for what would go where and how things would look on different screen sizes. Wireframes were created for mobile views firstly with the desktop views following.

**Mockup's are available in the 'Mockups' folder.**

  
## Features ##

**Features** that have been **implemented:**

* Easy to use **navigation** on all screen sizes.

* Popup modals are used if a logged in user wishes to delete a 'movie' as well as a 'helper' modal on the add/edit movie form instructing users on how to get a URL for an image.

*  **Attractive** design aimed at ease of use.

- Non logged in users have full read capability. They can scroll through and also search for movie(s).

- Logged-in users can create and edit 'movies'.

**Features** that will be **implemented** in the **future:**

##### Incorporate social media

* The ability to share a 'movie' via social media by incorporating social media platforms. For example, this would allow a user to post to instagram. Sharing this way would help increase the popularity of the site.

##### Option to add a youtube link to a movie trailer/clip

* The abilty to embed a movie trailer / clip into a movie card. This could be done by implimenting a youtube API and would be incorporated into the dedicated movie page.

##### Option to add comment section to movie cards

- Give users the abilty to leave comments on a particular movie. Controls would be put in place that would give the creator (or admin) of the review the option of enabling, deleting or flagging comments as well as allowing only friends to comment. etc

##### User profile

- Create a user profile. A user could provide basic information about themselves as well as being able to create lists e.g users top ten movies. User could also provide a profile image or select from a number of movie inspired images.

##### Rate other movies

- Rate other movies. The ratings that would then appear on a given movie will be based on a computation.

##### Curated top ten lists

* Feature top ten lists based on a season or an event, for example, Top ten Christmas movies around the holiday season or top ten Steven Spielberg movies on his birthday. These would be curated by the site owner.

##### Lost username/password support

- Provide support system for lost username / password.

##### Image optimisation

- Incorporate system for managing images that are uploaded by users that would enable them to be dynamically resized to specified size on load as well as compression. This would ensure that images are optimised for the site improving preformace.


##### Home page optimisation

- Currently the home page is one single page. As users add review cards the page grows in size. Two possible options to improve this are available.

  - Pagination. Limit the amount of cards to a particular page for example 4 per page.

  - Only load a set number of cards and as the user scrolls load another set of cards and so on.

  

## Technologies Used

### Languages Used

-  [HTML5](https://en.wikipedia.org/wiki/HTML5)

-  [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

-  [JavaScript](https://www.javascript.com/)

-  [Python 3.8.5](https://www.python.org/)

 
### Frameworks, Libraries and Programs Used

#### Front-End

-  [Materialize v1.0.0](https://materializecss.com/) - Used for the responsive layout as well as the navigation, header, footer, forms, item cards and modals.

-  [Font Awesome](https://fontawesome.com/) - Font Awesome was used to add social media icons at the bottom of the page and icons throughout the pages.

-  [Google Fonts](https://fonts.google.com/) - Google Fonts was used to import 'Nunito' font in the style.css file.

-  [dafont](https://www.dafont.com/) - 'Amity Jack' Font for navbar optained from dafont.com

-  [fontsquirrel](https://www.fontsquirrel.com/tools/webfont-generator) - The genereator was used to convert 'Amity Jack' font for web use.

-  [jQuery 3.5.1](https://jquery.com/) - Used to initialize Materialize components.

#### Back-End
-  [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/) - Web micro-framework written in Python and was used in building the web application.

-  [Jinja 2.11.2](https://jinja.palletsprojects.com/en/2.11.x/) - Templating language used across all HTML pages.

-  [Werkzeug 1.0.1](https://werkzeug.palletsprojects.com/en/1.0.x/) - Used in hashing and unhashing user passwords.

-  [MongoDB](https://www.mongodb.com/) - Non relational document-oriented database. Used to store all JSON-like documents and user, item, match, and category data.

-  [PyMongo 3.11.0](https://pymongo.readthedocs.io/en/stable/) - Used to connect Python to MongoDB Databse.

#### General
-  [Git](https://git-scm.com/) - Git was used to allowing for tracking of any changes in the code and version control.

-  [Github](https://github.com/) - GitHub is used to host the project files.

-  [Balsamiq](https://balsamiq.com/) - Balsamiq was used to create mockups.

-  [GitPod](https://www.gitpod.io/) - Web based IDE used to compile the code.

-  [TinyJPG](https://tinypng.com/) - Used to minify and compress images.

-  [Heroku](https://dashboard.heroku.com/apps) - A cloud platform used to deploy the web application.

-  [imagecompressor](https://imagecompressor.com/) - Used to compress placeholder image.

-  [StackEdit](https://stackedit.io/) - Markdown editor used to create the readme and testing markdown.

-  [Git](https://git-scm.com/)

## Testing

#### Full testing documentation is available in testing.md

  
# Deployment

The website is hosted via [GitHub](https://github.com/), with the source code being available on [my repository](https://github.com/Jammerref2015/watchthisnext).

### Requirements
-  **Python3** to run your application

-  **PIP** to install all app requirements

-  **IDE** of your choice - e.g Gitpod / Visual studio

- A **MongoDB Atlas** account for database development

### How To Access It

- In order to run this project locally you should follow these steps:

1. Click the green *'clone or download'* button in the [GitHub repository](https://github.com/Jammerref2015/watchthisnext) for the project.

2. Copy the link provided by clicking the **clipboard button** to the right of the link.
  
3. In your terminal, type ***git clone***, paste in the previously copied link, and hit return.
  
4. Create a file called ".flaskenv" and add the following:

-  **FLASK_APP=run.py**
-  **FLASK_ENV=development**
  
5. Install the required modules with the command **pip -r requirements.txt**.
  
6. If you don't have it yet, create a free account on [MongoDB](https://mongodb.com/) and create a new Database called **Database3**.
  
7. Then create the following collections in that Database:
-  **movies**

   -  **_id:**< ObjectId >
   -  **title:**< string >
   -  **synopsis:**< string >
   -  **genre:**< string >
    -  **platform:**< string >
    -  **rating:**< string >
    -  **release_year:**< string >
    -  **age_rating:**< string >
    -  **movie_image:**< string >
    -  **created_by:**< string >

-  **users**
    -  **_id:**< ObjectId >
   - **username:**< string >
   -  **password:**< string >

  8. You should now be able to run this application locally by typing **flask run**.
  
### Deployment to Heroku

1. Create a **requirements.txt** file by typing **pip3 freeze --local > requirements.txt** into the terminal line.

2. Create a Procfile by typing **echo web: python app.py > Procfile**.

3. Add, commit and push these changes to Github.

4. Navigate to the [Heroku](https://heroku.com/).

5. Create new app and give it a unique name.

6. Choose the region that is closest to you.

7. Go to the **Deploy** tab and choose **Github**.

8. Search for the correct repository and connect.

9. Go to Heroku **Settings** and navigate to **Config Vars**.

10. Set the following:

-  **IP = 0.0.0.0**
-  **MONGO_DBNAME = [Name of MongoDB]**
-  **MONGO_URI = mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority**
-  **PORT = 5000**
-  **SECRET_KEY = [Secret key]**

11. Go to the Deploy tab and **Deploy Branch**, ensuring that the master branch is selected.

## Credits

### Code

- Front end components were coded using [Materialize v1.0.0](https://materializecss.com/)

- Select validation used code provided in Code Institute DataBase Mini Project video

- Return to top button uses CSS and JS obtained from [w3schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top)

- Star rating on forms uses adapted code orginally obtained from [codeconvey](https://codeconvey.com/css-star-rating-radio-buttons/)

 
### Media 
- 'Amity Jack' font used in navbar designed by AJ Paglia and available from [dafont](https://www.dafont.com/amity-jack.font)

- Images used on this site are hosted from various sources as users can upload their own images.

- Orginal 'Doc Brown' image used in the image upload helper modal obtained from (https://media.fromthegrapevine.com/assets/images/2017/5/dr-emmett-brown.jpg.824x0_q71.jpg)

- Orginal royalty free placeholder image from vectorstock.com juice and popcorn for movie night poster vector 20220730

### Acknowledgements

- A big thank you to the great tutors at the Code Institute for helping save the hair i have left!

- Thanks Caterina O'Brian for help in naming the site.

- Thanks to my friends and family for endless testing.

- Big thanks to my mentor for putting up with my questions and giving me great insights.

> Written with [StackEdit](https://stackedit.io/).