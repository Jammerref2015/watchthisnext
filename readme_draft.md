


# Watch this next. -  Creating a movie database for the movies we love to watch!

![readme image](/assets/images/readme_image.jpg)

A live demo can be found [here](http://watchthisnext.herokuapp.com/)

'French is fun' is a simple word matching game inspired by a real-world word game **Kids 'French Kit by Magnetic Poetry** that uses double-sided magnets with the English word on one side, the French word on the other.
As someone learning the French language, I wanted to develop a fun word matching game aimed at people that are at the
early stages of learning French. The aim of the game is « Très facile! » Simply match the English word with the correct French word!
Try to match all the words before the time runs out!

## Contents ##
---
* UX
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
* Features
    * Features that have been developed
    * Features that will be implemented in the future
* Testing
* Bugs
* Deployment
* Credit


## UX

### Project Goals ###

The **goal** for this project was to make an easy to use word matching game that could help increase one's vocabulary. I have been learning French for a while now and I have used many language learning applications in the past, they inspired me when it came to creating 'French is fun'. I decided to keep the concept simple along with the execution. 'French is fun' needed to be super easy to use.

- Wireframes for this project are available in the Mockups folder.

### User Goals ###

* Provide users with a place to add movie reviews for movies they love.
* To provide a tool to help increase vocabulary.

### User Stories ###

* As a **user**, I want a **fun and interactive language learning application ** so I will be **educated and entertained**.
* As a **user**, I want to discover movies that i may have not seen.
* As a **user**, I want to be able to learn in a fun way by playing a game that will test my knowledge.

### Site Owner Goals ###

* As a **site owner**, I want to give users a place where can share ??????.
* As a **site owner**, I want to communicate my love for the French language by including images that highlight many French traditions.


### User Requirements and Expectations ###

**Requirements**
* Two word-groups presented.
* Display selected words in a specific place.
* Content displayed in a **visually appealing** manor.
* A visual cue that tells me when I achieve a successful word match.


**Expectations**
* Content is **visually satisfying** and presented.
* The features of the site are explained clearly and simply.
* Buttons are clear and easy to read.
* 


### Design Choices ###
---
**Fonts**
- I wanted the navbar to reference the movie 'Jaws'. In order to achive this i optained an open source font [amity_jack](https://www.dafont.com/amity-jack.font)
 - I then used a converter from fontsquirrel.com to Enable web embedding. (https://www.fontsquirrel.com/tools/webfont-generator)
 - The color for the fonts on the navbar was taken from the movie poster for Jaws.
 - This same font was also used for the placeholder image when a user does not submit an image. 
- I went with Google Fonts [Nunito](https://fonts.googleapis.com/css2?family=Nunito&display=swap). I felt that this font had a certain polishness to it.


**Colours**

- The color scheme was based on colors used in movie poster for 'Jaws' with colors eyedropped from the movie poster. 
- #384345 was used for the background
- #617478 was used for the navbar and footer
- Button colors for the search field were red for cancel and blue for submit. 
- Button color for the log in form is blue.
- Button color for delete review on review cards is #26a69a



## Wireframing ##
---
Balsamiq was used for wireframing. This produced some basic wireframes, which were used to get an overall feeling for what would go where and how things would look on different screen sizes.

These are available in the 'Mockups' folder. 


## Features ##
---
**Features** that have been **implemented:**

* Easy to use **navigation** on all screen sizes.
* Popup modals for starting the game, countdown running out, and completing the game.
* **Attractive** design aimed at ease of use of friendly images were used.
* Player can log in. Currently, the name is displayed next to the counter.

**Features** that will be **implemented** in the **future:**

* The ability to change the difficulty. Perhaps by adjusting the countdown time. For example, an easy difficulty level providing more time in which to complete the level.

* Turn the counter off. Learn without the pressure of the timer.

* Multiple levels. Increasing in difficulty as the player progresses utilizing including more difficult words. Counter continuing to countdown as they progress.

* Audio. Hear the word when a player clicks on a button. Also include some kind of sound on a successful match and/or successfully
completing a level.

* Include a different game style such as including a series of words alongside an image. The player selects the correct word to match the image.

* Allow the player to create a profile. This can include the ability to save scores/times.

* Enable player to have a word list showing the words that they have learned.

* Implement a dark mode feature.

* Allow the player to change UI colors by including some color schemes.




## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://www.javascript.com/)
- [Python 3.8.5](https://www.python.org/)

### Frameworks, Libraries and Programs Used
- Front-End
    - [Materialize v1.0.0](https://materializecss.com/) - Used for the responsive layout as well as the navigation, header, footer, forms, item cards and modals.
    - [Font Awesome](https://fontawesome.com/) - Font Awesome was used to add social media icons at the bottom of the page and icons throughout the pages.
    - [Google Fonts](https://fonts.google.com/) - Google Fonts was used to import 'Nunito' font in the style.css file.
    - [dafont](https://www.dafont.com/) - 'Amity Jack' Font for navbar optained from dafont.com
    - [fontsquirrel](https://www.fontsquirrel.com/tools/webfont-generator) - The genereator was used to convert 'Amity Jack' font for web use.
    - [jQuery 3.5.1](https://jquery.com/) - Used to initialize Materialize components.
- Back-End
    - [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/) - Web micro-framework written in Python and was used in building the web application. 
 
    - [Jinja 2.11.2](https://jinja.palletsprojects.com/en/2.11.x/) - Templating language used across all HTML pages
    - [Werkzeug 1.0.1](https://werkzeug.palletsprojects.com/en/1.0.x/) - Used in hashing and unhashing user passwords.
    - [MongoDB](https://www.mongodb.com/) - Non relational document-oriented database. Used to store all JSON-like documents and user, item, match, and category data.
    - [PyMongo 3.11.0](https://pymongo.readthedocs.io/en/stable/) - Used to connect Python to MongoDB Databse.
- General
    - [Git](https://git-scm.com/) - Git was used to allowing for tracking of any changes in the code and version control.
    - [Github](https://github.com/) - GitHub is used to host the project files.
    - [Balsamiq](https://balsamiq.com/) - Balsamiq was used to create mockups. 
    - [GitPod](https://www.gitpod.io/) - Web based IDE used to compile the code.
    - [TinyJPG](https://tinypng.com/) - Used to minify and compress images.
    - [Heroku](https://dashboard.heroku.com/apps) - A cloud platform used to deploy the web application.
    - [Canva](https://www.canva.com/) - Graphic Design Platform used in creating the logo and favicon.





* [Git](https://git-scm.com/)
* [Coolors](https://coolors.co)
* [Am I responsive](http://ami.responsivedesign.is/Responsive)
* [imagecompressor](https://imagecompressor.com/)

## Testing

- The application was tested manually using the following browsers. Testing involved going through the steps listed below as well as checking for responsiveness.  
  - Chrome.
  - Firefox.
  - Microsoft Edge.
  - Safari.

- Mark-up was validated via https://validator.w3.org/ - no errors were found.
- CSS was validated via http://jigsaw.w3.org/css-validator/ - no errors were found.
- JS was validated via https://jshint.com/ - no major issues were found.

- Page loading speed was tested using via chrome Developer tools -> Network.
  - Finish: 2.72 s
  - DOMContentLoaded: 2.01 s


* The following steps were followed on all major browsers.

    - On page load:
        - If new user('player') starts a game (name not in local storage) then a enter name modal appears.
        - If user('player') returns (name is in local storage) no modal appears and game counter starts counting down.

    - Change user button:
        - Clicked on the change user button, enter name modal appeared as intended.
        - Entered a new name which then appeared in on the main page. Entering a new name during a game results in a bug with the counter (see bugs section below).

    - Enter name modal:
        - Checked that the 'enter name' modal appeared on page load.
        - Clicked on the button to start the game without entering a name. Validation appeared as intended.
        - Clicked outside the modal to make sure that the player could not bypass the modal without entering a name. Also pressed Esc.
        - Checked to ensure that validation text appeared when the text field was left blank.   
        - Entered a name in the text field then click on the start button.

    - Change name button:
        - Clicked on the change name button to test if the enter name modal appeared.
        - Entered a different name to check that the name change occurred.

    - Reloading page.
        - Forced a page to reload. The counter appeared as intended and the current player name appeared. The page functioned as intended.
        - Changed player name during a game results in multiple countdowns. Reloading the page removes the countdown from the previous player.

    - Main game:
        - Checked to see that name entered in the text field matches that which appears on the screen.
        - Checked to see that counter was displayed and showed the correct timing.
        - Clicked on various buttons to make sure that the selected button changed color.
          - Grey when selected.
          - Restored to blue when a different button in the same language group was selected.
          - On a successful match checked that buttons changed to green, faded out, and became unselect-able.  
        - Let the timer run down to ensure that the timer expired modal appeared and the counter did not go into minus.
          - Clicked outside the modal to make sure that could not bypass modal. Also pressed Esc.
          - Checked that the restart button reloaded the page.
        - Matched all buttons to ensure that a 'Super' modal appears and counter stops.
          - Clicked outside the modal to make sure that the player could not bypass the modal. Also pressed Esc.
          - Checked that the restart button reloaded the page.

    - All of these actions were repeated with the console open. No errors were found.

    - The following bugs occurred during development

    - Counter issue:
      - The counter continued to run past zero even when the player completed the game. The countdown () function was updated to stop the clock when a player completes the game.
    - Randomize feature:
      - Adding the randomize feature caused buttons to randomize on click as opposed to on page load. This was corrected with changes made to the randomize function.
    - Rows too close to each other:
      - Setting margins and padding corrected this.
    - Enter name modal:
      - Player able to bypass enter name modal by clicking outside the modal. This was corrected by adding data-keyboard="false" data-backdrop="static".
      - Players were able to begin the game without entering a name. An if statement was added to check for a blank field.  
    - Timer expired modal:
      - The player able to bypass the timer expired modal by clicking outside the modal. This was corrected by adding data-keyboard="false" data-backdrop="static".
    - Player able to resize text-areas which affected the positioning of other elements.  
      - Styling was added to prevent this.
    - Modal images too large:
      - Added styling to the modals which fixed this.
    - Timer expired modal appearing on game completion:
      - Changes made to counter function to prevent this from happening.
    - Player needs to enter name when restarting:
      - implemented local storage to store player name and therefore remove the need to constantly re-enter name on page reload. Included a button to allow the player to change name.
    - Button sections styling issue.
      - Removing buttons resulted in rows getting smaller. Using a different technique to remove the buttons fixed this issue.
    - The Counter did not show if the player reloaded the page.
      - Updated main.js to run countdown if a player's name is in storage. Counter now appears.
    - Multiple counters running if the player's name changed during a game.
      - This bug needs to be corrected. The game should restart upon a name change.


    - The following bugs were discovered upon validation/testing

    - 'enter name' modal Firefox issue:
      - When clicking on the start button with a blank text field the validation text read 'Enter Nome'. Font not displaying correctly.
    - 'time out' modal Firefox issue:
      - Image is not displaying correctly.
    - The player name and counter were not visible when accessed on mobile without clicking on the accordion button:
      - Replaced navbar with a row with styling.

# Deployment

The website is hosted via [GitHub](https://github.com/), with the source code being available on [my repository](https://github.com/Jammerref2015/watchthisnext).

### Requirements

- **Python3** to run your application
- **PIP** to install all app requirements
- **IDE** of your choice - e.g Gitpod / Visual studio
- A **MongoDB Atlas** account for database development


### How To Access It
- In order to run this project locally you should follow these steps:

    1. Click the green *'clone or download'* button in the [GitHub repository](https://github.com/gaspar91/FeedMe) for the project.

    2. Copy the link provided by clicking the **clipboard button** to the right of the link.

    3. In your terminal, type ***git clone***, paste in the previously copied link, and hit return.

    4. Create a file called ".flaskenv" and add the following:
        - **FLASK_APP=run.py**
        - **FLASK_ENV=development**

    5. Install the required modules with the command **pip -r requirements.txt**.

    6. If you don't have it yet, create a free account on [MongoDB](https://mongodb.com/) and create a new Database called **Database3**.

    7. Then create the following collections in that Database:
        - **categories**
            - **_id:**< ObjectId >
            - **category_name:**< string >
            - **category_image:**< string >
        
        - **difficulty**
            - **_id:**< ObjectId >
            - **level:**< string >
        
        - **recipes**
            - **_id:**< ObjectId >
            - **category_name:**< string >
            - **recipe_name:**< string >
            - **recipe_description:**< string >
            - **recipe_ingredients:**< string >
            - **recipe_method:**< string >
            - **recipe_image:**< string >
            - **time:**< string >
            - **difficulty:**< string >
            - **created_by:**< string >
        
        - **difficulty**
            - **_id:**< ObjectId >
            - **tool_name:**< string >
            - **tool_description:**< string >
            - **tool_details:**< string >
            - **tool_image:**< string >
        
        - **users**
            - **_id:**< ObjectId >
            - **username:**< string >
            - **password:**< string >
            - **email:**< string >
    
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
        - **IP = 0.0.0.0**
        - **MONGO_DBNAME = [Name of MongoDB]**
        - **MONGO_URI = mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority**
        - **PORT = 5000**
        - **SECRET_KEY = [Secret key]**


   11. Go to the Deploy tab and **Deploy Branch**, ensuring that the master branch is selected.


## Credits

### Code 
- Front end components were coded using [Materialize v1.0.0](https://materializecss.com/)
- Select validation used code provided in Code Institute DataBase Mini Project video
- Return to top button uses CSS and JS obtained from [w3schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top)
- Star rating on forms uses adapted code orginally obtained from [codeconvey](https://codeconvey.com/css-star-rating-radio-buttons/)

### Media :clapper:
- 'Amity Jack' font used in navbar designed by AJ Paglia and available from [dafont](https://www.dafont.com/amity-jack.font)
- Images used on this site are hosted from various sources as users can upload their own images. 
- Orginal 'Doc Brown' image used in the image upload helper modal obtained from (https://media.fromthegrapevine.com/assets/images/2017/5/dr-emmett-brown.jpg.824x0_q71.jpg)

### Acknowledgements
- A big thank you to the great tutors at the Code Institute for helping save the hair i have left! 
- Thanks Caterina O'Brian for help in naming the site. 
- Thanks to my friends and family for endless testing.
- Big thanks to my mentor for putting up with my questions and giving me great insights.