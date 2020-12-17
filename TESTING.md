


## Table of Contents
1.  [Functionality](#functionality)

2.  [Validators](#validators)
	-  [HTML5](#html5)
	-  [CSS](#css)
	-  [JavaScript](#javascript)
	-  [Python](#python)

4.  [Compatibility](#compatibility)
5.  [Performance](#performance)
6.  [User Stories](#user-stories)
 
7.  [Bugs](#bugs)
	-  [Identified Bugs](#identified-bugs)
	-  [Existing Bugs](#existing-bugs)
  
1.  [Future Testing](#future-testing)

## Functionality

#### Navigation Bar

- Logo is placed to the left of the nav-bar on desktop, it is placed in the centre of the nav-bar on a tablet/mobile.

 - When  the logo is clicked/tapped, it brings the user to the Home Page or reloads it if they are already on the home page. This has been tested from all pages rendered on desktop, tablet, and mobile platforms.

- The navigation bar stays at the top of the page on all screen sizes.

- Font sizes adjust as intended on mobile/tablet devices to avoid overflow.

- All links in the nav-bar are working as intended and have been tested on multiple devices.

#### The following links are available depending on whether a user is logged in or not.

##### User is NOT signed in/registered:

-  **Home** -> Reload home page if already there. Return to home page if elsewhere.

-  **Log in** -> Log in page

-  **Register** -> Register page

##### User is signed in/registered:

-  **Home** -> Reload home page if already there. Return to home page if elsewhere.

-  **Add review** -> Add review page.

-  **Log out** -> User is logged out and rerouted to log in page.

#### The 'hamburger' menu appears on the right side of the nav-bar on screen sizes smaller than 992px.
- When clicked/tapped, it expands to reveal page links. These have been tested and are working as expected.

#### The following links are available depending on whether a user is logged in or not.

##### User is NOT signed in/registered:

-  **Home** -> Reload home page if already there. Return to home page if elsewhere.

-  **Log in** -> Log in page

-  **Register** -> Register page

##### User is signed in/registered:

-  **Home** -> Reload home page if already there. Return to home page if elsewhere.

-  **Add review** -> Add review page

  
-  **Log out** -> User is logged out and rerouted to log in page.

#### Footer

- Footer remains at the bottom of the screen on all devices.
- When the social media links are clicked, they open the relevant social media page in a new tab.

## Manual Testing

### The following steps were followed on all popular browsers with the console opened to error check and closed to check for display issues.

- On page load (user not logged in): Movie review cards appeared. Scrolled through the page. **Worked as intended**.

#### Home page (user not signed in/registered):

- On scrolling down a small red button appeared in the bottom right corner which allows the user to return to the top of the current page. Scrolled on page then clicked on button. **Worked as intended**

 - Clicking on a card brings the user to an individual movie page with more information. Clicked on random cards, each time resulted in the correct page loading. **Worked as intended**

 - Clicked on log in link located above search field. Log in page loaded. **Worked as intended**

 - Clicked on register in link located below the search field. Registration page loaded. **Worked as intended**
  
#### Home page (user signed in):

  - On scrolling down a small red button appeared in the bottom right corner which allows the user to return to the top of the current page. Scrolled on page then clicked on button. **Worked as intended**

  - Clicking on a card brings the user to an individual movie page with more information. Clicked on random cards, each time resulted in the correct page loading. **Worked as intended**

- Clicked on add movie link located below the search field. Add movie page loaded. **Worked as intended**

### Home page search function:
  
- User can search with any of the following categories:

"title"
"synopsis"
"release year"
"genre"
"platform"
"rating"
"age rating"
"created by"

#### When a user searches using any of these categories and clicks the blue 'enter' button or types enter key. The following occurs:

- If the category search finds a match, the page reloads with the relevant card(s). Clicking/tapping the red 'reset' button reloads the page with all the cards. When searching for a movie that exists, the Movie card appears. **Worked as intended.**
 
- If the category search does NOT find a match a **'review not found'** notice appears with a link to sign up and add a review. Clicking the link loads the registration page. Searching for a movie that does not exist. **Worked as intended.**

- Clicking the red reset button at any point reloads the page. **Worked as intended.**

 - A max length of 20 characters was set for the input. User cannot enter more than 20 characters. Typed random text, once it reached 20 characters, was not able to type any further. **Worked as intended.**

  - A min length of 4 characters was set for the input. Typed less than 4 characters and hit enter. A notice appeared 'Please lengthen this to 4 characters or more you are currently using 1,2,3 characters. **Worked as intended.**

### Home page 'movie cards'

#### User not registered/logged in:

- Cards appeared on home page for individual movies. Clicking on the image of a card brought you to a dedicated page for that movie with more information. Clicked on random cards resulted in dedicated movie page loading. **Worked as intended.**

- Links to 'edit movie' and 'delete movie' did not appear on individual cards. **Worked as intended.**

#### User logged in:
  
- Cards appeared on home page for individual movies. Clicking on the image of a card brought you to a dedicated page for that movie with more information. Clicked on random cards resulted in dedicated movie page loading. **Worked as intended.**

- Links to 'edit movie' and 'delete movie' were available on individual cards **ONLY** for movies added by that user. I logged in and inks to edit/delete movies were only available on cards that I had created. **Worked as intended.**

- Clicked on 'edit movie' resulted in the 'edit movie' page loading for a particular movie. **Worked as intended.**

- Clicked on 'delete movie' resulted in 'delete movie' modal pop-up appearing. **Worked as intended.**

#### 'admin' logged in.

- Cards appeared on home page for individual movies. Clicking on the image of a card brought you to a dedicated page for that movie with more information. Clicked on random cards resulted in dedicated movie page loading. **Worked as intended.**

- Links to 'edit movie' and 'delete movie' were available on **ALL** individual cards. **Worked as intended.**

- Clicked on 'edit movie' resulted in the 'edit movie' page loading for a particular movie. **Worked as intended.**

- Clicked on 'delete movie' resulted in 'delete movie' modal pop-up appearing. **Worked as intended.**

#### Home page 'delete movie' modal pop-up.

- If the creator of the movie review(s) or admin is logged in a 'delete movie' button was available on movie cards for which the user created. Clicking on this resulted in a modal appearing. Clicked on 'delete movie' on cards. Modal appeared. **Worked as intended.**

##### The text read 'are you sure you want to delete?' With two options:

- Clicked 'no' resulted in the modal closing. **Worked as intended.**

- Clicked 'yes' resulted the home page reloading with a flash message to state that i had successfully deleted my movie. Scrolled down the page to check that card had been deleted. The movie was no longer on the home page. **Worked as intended.**

### Register page:

- Register page has **three fields**: Email, username and password:

##### email:

- User must enter a legitimate email address. This is a required field. 

- Email address field was empty, clicking on submit resulted in a 'Please fill out this field' message appearing, the field turned red to alert. **Worked as intended.**

- Random text was entered. Upon clicking the submit button a message appeared. Line was red to alert. An alert with the text 'Please include a @ in the email address' appeared. **Worked as intended.**

- An Email address was entered. Line was green to illustrate that this was ok. **Worked as intended.**

##### Username:

- Username field was empty, clicking on submit resulted in a 'Please fill out this field' message appearing, the field turned red to alert. **Worked as intended.**

- A minlength of 5 characters was set. A 'Please match the requested format' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 15 characters was set. Typed random characters. Once 15 characters was reached it was not possible to type any more. **Worked as intended.**

##### Password:

- Password field was empty, clicking on submit resulted in a 'Please fill out this field' message appearing, the field turned red to alert. **Worked as intended.**

- A minlength of 5 characters was set. A 'Please match the requested format' noticed popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 15 characters was set. Typed random characters. Once 15 characters was reached it was not possible to type any more. **Worked as intended.**

#### If user existed:

- Entered a username and password for a registered user resulted in an **'Username already exists'**. The register page reloaded. **Worked as intended.**

#### If user does not exist. (I.e new user)

- Entered a unique email, username and password. This resulted in being routed to the home page with a flash message **'registration successful'**. **Worked as intended.**

### Log in page:

- Log in page has **two fields**: Username and password:

##### Username:

- Left the username field blank (password field was not blank) and clicked 'Log in'. A 'please fill out this field' notice appeared. **Worked as intended.**

- A minlength of 5 characters was set. Typed less than 5 characters. A 'Please match the requested format' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 15 characters was set. Typed random characters. Once 15 characters was reached it was not possible to type any more. **Worked as intended.**

##### Password:

- Left the password field blank (username field was not blank) and clicked 'Log in'. A 'please fill out this field' notice appeared. **Worked as intended.**

- A minlength of 5 characters was set. A 'Please match the requested format' noticed popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 15 characters was set. Typed random characters. Once 15 characters was reached it was not possible to type any more. **Worked as intended.**

#### If user existed:

- Entered a username and password for a registered user. Home page loaded with 'Welcome user' notice. Worked as intended.

#### If user did not exist.

- Entered correct username, incorrect password. This resulted in a flash message 'Incorrect Username and/or Password' appearing. Remained on the log in page. **Worked as intended.**

- Entered correct password incorrect username. This resulted in a flash message 'Incorrect Username and/or Password'. Remained on the log in page. **Worked as intended.**
  
### Add movie page. (only available to logged in users)

- Add movie page loaded with a form. **Worked as intended.**

- The following categories were available:

##### "title":

- Left field blank. Clicked on 'Submit movie'. 'Please fill out this field' text appeared.**Worked as intended.**

- A minlength of 2 characters was set. A 'Please lengthen text to 2 characters or more' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 40 characters was set. Typed random characters. Once 40 characters was reached it was not possible to type any more. **Worked as intended.**

##### synopsis:

- Left field blank. Text was entered in 'title' field. Clicked on 'Submit movie'. 'Please fill out this field' text appeared. **Worked as intended.**

- A minlength of 20 characters was set. A 'Please lengthen text to 20 characters or more' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 240 characters was set. Typed random characters. Once 240 characters was reached it was not possible to type any more. **Worked as intended.**

##### genre:

- Left field blank. Text was entered in previous fields. Clicked on 'Submit movie'. 'Please fill out this field' text appeared. **Worked as intended.**

- A minlength of 5 characters was set. A 'Please lengthen text to 5 characters or more' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 20 characters was set. Typed random characters. Once 20 characters was reached it was not possible to type any more. **Worked as intended.**

##### platform:

- Left field blank. Text was entered in previous fields. Clicked on 'Submit movie'. 'Please fill out this field' text appeared. **Worked as intended.**

- A minlength of 3 characters was set. A 'Please lengthen text to 3 characters or more' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 10 characters was set. Typed random characters. Once 10 characters was reached it was not possible to type any more. **Worked as intended.**

##### rating:

-  **On hover:** Stars increased in size. **Worked as intended.**

-  **On click/tap:** Stars changed colour to indicate that they've been selected. **Worked as intended.**

- Star rating is **not** a required field.

##### release year:

- Left field blank. Text was entered in previous fields. Clicked on 'Submit movie'. 'Please fill out this field' text appeared. **Worked as intended.**

- A minlength of 2 characters was set. A 'Please lengthen text to 2 characters or more' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 4 characters was set. Typed random characters. Once 4 characters was reached it was not possible to type any more. **Worked as intended.**

##### age rating:
- Left field blank. Text was entered in previous fields. Clicked on 'Submit movie'. 'Please fill out this field' text appeared. **Worked as intended.**

- A minlength of 2 characters was set. A 'Please lengthen text to 2 characters or more' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 4 characters was set. Typed random characters. Once 4 characters was reached it was not possible to type any more. **Worked as intended.**

##### movie poster URL:
This field is optional. The following possible actions can occur:

##### user leaves the field blank:
- Left the field blank. All other fields were completed. Clicked on submit movie. Movie was added. **Placeholder image was implemented**. **Worked as intended.**

##### user enters random text (i.e not a url to an image file):
- Added random text. All other fields were completed. Clicked on submit movie. Movie was added. **Placeholder image was implemented**. **Worked as intended.**
 
##### user enters a URL for an image but the image is not found (404):
- Entered a URL for an image that was not found (404). Clicked on submit movie. Movie was added. **Placeholder image was implemented**. **Worked as intended.**

##### user enters a URL for an image which is available:
- Entered a URL for an image. Clicked on submit movie. Movie was added. **User image was applied**. **Worked as intended.**

#### 'Need help' button.

- Clicked on 'need help' button. Modal appeared. Clicked 'close' caused it to close. **Worked as intended.**

- Clicked on 'need help' button. Modal appeared. Clicked outside the modal caused it to close. **Worked as intended.**

#### 'Add movie' button.

##### Clicked on submit movie button with all text fields correctly filled. Two actions were possible:

- If the movie already existed a message stating this appeared. Remained on add movie page. **Worked as intended.**

- If the movie did not existed it was added to the database. Remained on add movie page. **Worked as intended.**


### Edit movie page. (only available to logged in users who created the movie and admin user.)

- Edit movie page loaded with a form. All fields were prefilled except Movie Poster URL and star rating as intended. Prefilled text was deleted to test validation.

The following categories were available:

##### "title":
- Left field blank. Clicked on 'Submit movie'. 'Please fill out this field' text appeared.**Worked as intended.**

- A minlength of 2 characters was set. A 'Please lengthen text to 2 characters or more' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 40 characters was set. Typed random characters. Once 40 characters was reached it was not possible to type any more. **Worked as intended.**

##### synopsis:
- Left field blank. Text was entered in 'title' field. Clicked on 'Submit movie'. 'Please fill out this field' text appeared. **Worked as intended.**

- A minlength of 20 characters was set. A 'Please lengthen text to 20 characters or more' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 240 characters was set. Typed random characters. Once 240 characters was reached it was not possible to type any more. **Worked as intended.**

##### genre:
- Left field blank. Text was entered in previous fields. Clicked on 'Submit movie'. 'Please fill out this field' text appeared. **Worked as intended.**

- A minlength of 5 characters was set. A 'Please lengthen text to 5 characters or more' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 20 characters was set. Typed random characters. Once 20 characters was reached it was not possible to type any more. **Worked as intended.**

##### platform:
- Left field blank. Text was entered in previous fields. Clicked on 'Submit movie'. 'Please fill out this field' text appeared. **Worked as intended.**

- A minlength of 3 characters was set. A 'Please lengthen text to 3 characters or more' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 10 characters was set. Typed random characters. Once 10 characters was reached it was not possible to type any more. **Worked as intended.**

##### rating:
- **On hover:** Stars increased in size. **Worked as intended.**

-  **On click/tap:** Stars changed colour to indicate that they've been selected. **Worked as intended.**

- Star rating is **not** a required field.

##### release year:
- Left field blank. Text was entered in previous fields. Clicked on 'Submit movie'. 'Please fill out this field' text appeared. **Worked as intended.**

- A minlength of 2 characters was set. A 'Please lengthen text to 2 characters or more' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 4 characters was set. Typed random characters. Once 4 characters was reached it was not possible to type any more. **Worked as intended.**

##### age rating:
- Left field blank. Text was entered in previous fields. Clicked on 'Submit movie'. 'Please fill out this field' text appeared. **Worked as intended.**

- A minlength of 2 characters was set. A 'Please lengthen text to 2 characters or more' notice popped up if the minlength was not satisfied. Line went red to alert. **Worked as intended.**

- A maxlength of 4 characters was set. Typed random characters. Once 4 characters was reached it was not possible to type any more. **Worked as intended.**
  
##### movie poster URL:
This field is optional. The following possible actions can occur:

##### user leaves the field blank:
- Left the field blank. All other fields were completed. Clicked on submit movie. Movie was added. **Placeholder image was implemented**. **Worked as intended.**

##### user enters random text (i.e not a url to an image file):
- Added random text. All other fields were completed. Clicked on submit movie. Movie was added. **Placeholder image was implemented**. **Worked as intended.**

##### user enters a URL for an image but the image is not found (404):
- Entered a URL for an image that was not found (404). Clicked on submit movie. Movie was added. **Placeholder image was implemented**. **Worked as intended.**

##### user enters a URL for an image which is available:
- Entered a URL for an image. Clicked on submit movie. Movie was added. **User image was applied**. **Worked as intended.**

#### 'cancel' button:
- Clicked on 'cancel' button. Returned to home page. **Worked as intended.**

#### 'Submit' button:
- Clicked on submit movie button with all text fields correctly filled. Movie was updated. **Worked as intended.**


### Individual movie page.
- Clicked on random movie cards on home page resulted in an individual page loading for that particular movie. **Worked as intended.**

- Clicked on the 'home link' at the top of the page. Directed to home page. **Worked as intended.**

- Clicked on image. Card action loaded. Movie details were present. **Worked as intended.**

- Clicked on the 'X' located on the top right. Movie details closed, image reappeared. **Worked as intended.**

##### If the user is logged in and is the creator of the review (or admin):

- Edit movie link and delete movie buttons were at the bottom of the card. **Worked as intended.**

- Clicked on edit movie resulted in the edit movie page loading with the correct prefilled fields. **Worked as intended.**

- Clicked on delete movie. Modal appeared asking for confirmation on deletion. **Worked as intended.**

##### If the user is NOT logged in:

- Bottom of card was blank. **Worked as intended.**

### Log out

- Clicked log out link. Redirected to log in page. A message alerting user has successfully logged out. Worked as intended.**Worked as intended.**


## Buttons

  - A return to top button appears when a user scrolls. When clicked/touched on each page and works as intended. **Worked as intended.**

  - All buttons have been tested and function as intended.

   ## Modals

  - A modal appears when a user clicks delete review. Works as intended. Movie review is deleted if desired. Modal disappears if user decides not to delete movie.

  - The add review page features a modal which is activated when a user clicks on 'Need Help'. The intention is to provide a user with instructions on retreving an image URL. **Worked as intended.**

  - Clicking outside the modal closes it as well as clicking the 'close' button.**Worked as intended.**

## Redirects

- When a new user completes registration he/she is redirected to the home page. **Worked as intended.**

- When an existing user logs in, they are redirected to the home page. **Worked as intended.**

- When an existing user logs out, they are redirected to the 'Log in' page. **Worked as intended.**

- When a user adds a new review they are redirected to the home page. **Worked as intended.**

- When a user clicks on submit movie in edit movie they are redirected to the home page. **Worked as intended.**

- When a user deletes a review on the home page the card is removed from the home page. **Worked as intended.**

- When a user deletes a review on the dedicated movie they are redirected to the home page. **Worked as intended.**

## External links

- All external links were tested to make sure they open up the correct pages in new tabs

- All social links in the footer bring the user to the relevant social pages that open in a new tab.

## Internal links

- All internal links were tested to make sure that all pages are correctly connected

- Navigation links bring the user to the relevant pages.

- Logo located in the navigation bar always brings the user to the home page.

- Links connecting the 'Register' page to the 'Log In' page and vice versa work and have been tested.

  
## Bugs

### Identified bugs

#### Movie cards not displaying correctly on the home page:

- A bug occurred that resulted in movie cards not displaying correctly on the home page. Each card was being generated inside a column which in turn caused the next card to be generated within that column. With each card gradually getting smaller and smaller.

- This was caused by a misplaced jinga 'for loop'  as well as a missing closing div tag.

- This was fixed by placing the div col within the for loop. Now each card is generated with its own column. The missing closing div tag was also added.

#### Fixed an error which allowed a non registered user to add a review:

- When a user searched for a movie that did not exist. Text appeared to alert the user that the movie did not exist. A link to add a review was present. Clicking this link brought the user to the add movie page.

- This was fixed by putting controls in place via a jinga 'if statement'. If a user is logged in then the link to the add movie form is present. If the user is not logged in a link to register is present.

#### Fixed an error which allowed non logged in / registered users to edit movie / delete movie:

- The ability to edit / delete movie's were available to users not signed in. This was caused by an error in an if statement {% if session.user == "admin" %}.

- Changing the line to {% if session.user == "admin"|lower %} fixed the error.

  
### Existing Bugs

- When a user edits a movie it is currently possible to rename a movie to one which may already exist. This could lead to duplicate movies being created. Attempts were made at putting a check in place to see if a movie already existed in the database when a user/admin edits a movie. Such attempts were unsuccessful however.

- As the site currently allows users to upload an image of their chosen movie this will result in images of varying sizes which result in styling issues in the cards, particularly on mobile devices.

- Star ratings are not currently saved when a user edits a movie they have to re-rate the movie. Text was added above the buttons 'Dont forget your rating!'. A tooltip was also included on the submit button but that is only visable via hover on desktops.

- In recent days there has been an issue regarding a lack of security due to no SSL certificate being attached to the page. This resulted in the following browser warning:  **The information you’re about to submit is not secure. Because the site is using a connection that’s not completely secure, your information will be visible to others.** SSL is only available on a paid Heroku plan. Switching to such a plan would eliminate this issue. Steps have been taken to ensure that confidental elements such as the MONGO_URI string for example are not available to the public (via github). Passwords are also secured using password hashing. 

- Delete modal on desktop currently adds the links to edit and delete reviews to the modal itself. This does not occur on mobile or tablets. 

- On the day of submitting the project a bug was discovered when signed in as 'admin', the button for 'delete movie' was not activating when clicked. A work around solution was to replace the button to open the 'delete movie' modal with a link. Clicking the link resulted in a movie being deleted. Further testing revealed that the last movie to be added does have a delete movie button that opens the modal and deletes the movie if the yes option is seleected. 

## Validators

### HTML5

- 5 validator - Fail

- HTML validator returned multiple errors as it does not recognize Jinja
 

### CSS3

- validator - Pass

- No Errors

- 1 warning 'Imported style sheets are not checked in direct input and file upload modes'

- Validation by URI resulted in many errors and warnings concerning imported CSS libraries

### JavaScript

- JSHint - script.js - pass

- Only known warnings for using `$` (jQuery)

- It refers to an unused variable on line 43 for 'topFunction' which is used in an onclick function in the HTML markup

### Python

- PEP8 (using pep8online) - app.py - pass ('All right')

## Usability

- To test the ease of navigation, this website was shared with friends and family of different ages.

- The site was accessed on a variety of devices, android phones and tablets, iOS phones and tablets and OSX/Windows/Linux systems

- Feedback resulted in some features being added such as the helper text on the movie pages explaining that clicking on the image allows you to access more information.

- There were no issues identified regarding the simplicity of navigating the website. No instructions were given as i needed to ensure that the aim of the site was straight forward and didn't need instruction.

- The testers also verified that all functionality aspects were working as explained above and as expected.

- Testers expressed that the design was easy to understand and navigate.

- 'Dummy' user accounts were also created and multiple movies were added.

- These accounts were used to interact with the site to test all the functionality explained.

## Compatibility

- Browser Compatibility

| Screen size\Browser | Safari | Opera | Microsoft Edge | Chrome | Firefox | Internet Explorer |

| --------------------|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:-----------------:|

| Mobile |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Not Tested |

| Tablet |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Not Tested |

| Laptop |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Not Tested |

| Desktop |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Not Tested |

- The website was exhaustively tested for responsiveness using [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)


### Performance Testing

##### Preformace testing was achived using pingdom.com. on 15/12/20. Due to the fact that users can upload images these results may change. 

- Preformance grade: B/86
- Page size 732.0 KB. 
- Load time: 678 ms
- Requests: 17

##### A detailed report is available here. [pingdom.com](https://tools.pingdom.com/#5d9a0d2168c00000)

  ### User Stories

  #### Common user stories:
 

#### I want to intuitively navigate through the site to browse the content.

- The landing page displays the latest 'movies' to be added to the site. The cards are displayed in pairs on desktops and singlarly on devices smaller than desktops.
  
- The footer and the header remain the same throughout the site which provides consistency for the user to easily understand how the site works.

  - The header and the footer are kept in line with conventional styles which lets the user access the navigation without thinking.

  - The 'logo' is placed on the left side of the navbar on desktop and is centered on mobile devices. Clicking it brings the user home. A dedicated 'home' link is also available.

 - The header is always visible at the top of the page and the user can find each page easily at any time.

   - All pages are displayed in the navigation bar as well as throughout the pages to provide the user with multiple points of navigation.

  - The style is kept the same throughout the page to allow the user to intuitively understand how to navigate the page.

#### I want the experience of using this site to be interactive.

  - Flash messaging feedback is provided to the user. To help boost the movie fan theme of the site, random qoutes from movies are implemented on log-in.

  - Delete movie confirmation is displayed as a modal pop-up.

  - Image URL help modal appears with a background image from a classic movie.

 #### I want to be able to view all 'movie' reviews.

  - User can view all movies on the home page. A sroll to top button enables user to quickly return to the top of the page to access the search feature.

- If the user has searched for a movie , they can once again view all movies by clicking the 'reset' button.

  #### I want to search by different categories.

- The search bar on the home page allows you to search by different categories, for example if one just wanted to see action movies. Typing 'action' will display movies in the 'action' category.

  - Search bar is clear, simple and easy to find and use.

  - Users can search by either pressing the 'Enter' key or clicking on the search button.

- Users can reset a search by clicking the 'reset' button.

 #### I want to access more information about a particular movie.

  - Clicking on a movie in the home page brings me to a dedicated page for that movie. A visually appling 'wave-effect' occurs on tap/click.

  - Clicking the image brings up more information on the movie. Clicking the 'X' closes the info pane.

  - A link to return to home is placed above the card eliminating the need to open the hamburger menu on mobiles. 

  #### I want to be able to understand the purpose of the site.

 - The home page has a short description keeping it simple.

  #### I want to be able to contact the owner of the site.

- Footer contains social media links that can be used to contact the creator.

####  I want the page to be responsive on all screen sizes.
- Page has been extensively tested to ensure it is responsive and works on all screen sizes.

 #### I want to be able to navigate to the top of the page quickly, particularly in the mobile view.

- A 'Go to top' button appears on page scroll which a user can click to bring them to the top of the page.
  
### As a first time visitor

#### I want to be able to find the 'Register' page easily.

- The 'Register' page link is located and clearly labeled in the navigation bar as well as above the search area.

- If the user clicks on the 'Log In' page instead, they can find a 'Register' page link under the login form.

- A link to register is also located below the search area. 
 

#### I want to be able to register easily

- The form on the 'Register' page is responsive and easy to use.

- Only two fields are required which allows the user to register quickly. **Email is not currently 'required'**.

- Real-time feedback is provided to the user in form of the color around the input field. This saves time for the user as they can see if the value entered is correct/incorrect before submitting the form.

 ### As a returning user

#### I want to be able to navigate to the 'Login' page easily.

- The 'Log In' page is located and clearly labeled in the navigation bar.

- A link to log-in is also located below the search area. 

- If the user clicks on the 'Register' page instead, they can find the 'Log In' page link under the login form.

- The call-to-action button on the landing page redirects the user to the 'Register' page which has the 'Log In' page link.

- If the user Logs Out, they are redirected to the login page in case they want to Log in again.

#### I want to be able to Log In quickly.

- The login form only contains 2 fields.

#### I want to add new movies easily.

- The 'Add movie' page link is located in the navigation bar and clearly labelled. It is also available at the start of the page. 

- A link to 'Add movie' is also located below the search area. 

- Real-time feedback is provided to the user in form of the color around the input field. This saves time for the user as they can see if the value entered is correct/incorrect before submitting the form.

- The form can be easily reset by clicking on the 'Reset' button.

- The form is responsive and easy to use.

#### I want to be able to edit and delete my movies.

- Each movie card displays an edit button to the creator of the movie review which brings the user to the 'Edit movie' page.
  
- Movie details are pre-filled in the form to allow the user to quickly change the relevant fields.

- Users can cancel editing a movie by clicking the 'Cancel' button.

- Each movie displays a delete button available to the creator of the movie review.

- When the delete button is clicked, the user is prompted with a confirmation. This prevents the user from accidentally deleting a movie (especially relevant on mobile sizes as it is easier to click/tap on the wrong button)

#### I want to be able to Log out.

- The 'Log Out' button is located in the navigation bar and labelled clearly.

### As an admin

#### I want to be able to delete an item if it contains inappropriate content

- Admin has the additional functionality to delete and edit all movies. 

  
> Written with [StackEdit](https://stackedit.io/).