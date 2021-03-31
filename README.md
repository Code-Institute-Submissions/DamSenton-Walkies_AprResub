# Walkies!

## Milestone Project 3

![Walkies, Responive Design](https://browser-fe9a12bc-f34c-4c3b-98e3-d6bb3c2e7b81.ws-eu03.gitpod.io/workspace/Walkies/static/img/Responsive-Walkies.JPG)

## Introduction

This is my thirdd Milestone Project. Having previously focussed on HTML5, CSS3 and JavaScript, this project afforded me the opportunity to use Python, Jinja, Flask and MongoDB to bring about not only a responsive website, but also a highly functional one that takes into account user needs and desires from a website such as this.

*Walkies!* is a fictional company based in Edinburgh, focussing on 5 main areas within, these being Haymarket, Leith, Morningside, New Town and Stockbridge. This website aims to bring walkers and owners together for the sake of dogs. 

I decided to go with this idea as my wife and I have previously used a website called Borrow My Doggy, which *Walkies!* takes inspiration from. We believe that no dog should go without proper exercise and stimulation but we also wanted something that focussed on our local area.

[Live view of my project](http://walkies-master.herokuapp.com/index)

<hr>

## **User Experience**

### Project aims

- To bring walkers and owners together to ensure those who cannot walk their dogs, are able request help, and also allows those who do not have a dog to spend time with one whilst getting out and active.

- Make a seamless experience for all users from start to finish by implementing responsive design principles such as a grid system and flexible page elements.

- Make use of MongoDB to store user data and to also provide live feedback to users e.g. when entering an incorrect username/password or by trying tosign up with a username that is already in use.

- Make use of APIs, such as Google Maps API to show users possible walk locations if they are new to an area.

<hr>

### User stories

### Stakeholders

- As the sole creator of this website, I want to see high amounts of user traffic as I feel strongly about the company's purposea and would personally use this frequently.

### New users

- When i first opened this website, I knew exactly how to navigate it, I liked how you canpress the logo to take you back home, and the layout of each page made sense and really fit in with the purpose of the website.

- I would use this regularly as I currently work from home during lockdown and would like to see my dog given the attention he deserves

### Returning users

- As a returning user, I like the fact that I am always matched with an owner who needs their dog walked, it gives me a good reason to get out of the house during lockdown and has really helped me during these times.

### Mobile user

- As a moble user, it is nice to see a website built with mobiles in mind, this website works well on all screen sizes, especially my small phone screen, and no feature is exclusive to a desktop which really ties the experience together.

<hr>

## Design Planes

- Strategy Plane: As stated above, I wanted to create a webpage that brought people together with one goal in mind, walking dogs. I also wanted to flex my newly found Python muscles and put my knowledge of MongoDB and Jinja to good use and integrate a system which is easy to use for all types of users.

- Scope Plane: I knew i wanted to give users the ability to sign up to this webpage, but I wanted two types of users, Walkers and Owners. With a new found skill in Jinja, I wanted to use this to have these users connect on the back-end by matching them based on age groups and location so that only certain users are exposed to data relevant to them.

- Structure Plane: Having decided on key features, I set to work on the overall structure of my web page, focussing heavily on mobile first, responsive design which used the incredible grid system and flex-box features which does a lot of heavy lifting with responsive design. 
I decided on a basic structure which uses a multi-page structure to allow for account registration, sign-in, user profiles and CRUD funtionality for owners to allow then to create, read, edit and delete new bespoke walks for theie dog(s).

- Skeleton Plane: As above, I knew i would be using the grid system and flex-box for this project, so the placement for my content was set to center-align to make this seamlessacross all screen sizes. My buttons we placed centrally also to make use of the afformentioned grid system. I wanted first time users to know exaclty how to use the webpage and how to navigate this, so my navbar is what I consider industry standard, and as per an above user story, this seems to have paid off.

- Surface Plane: With all of he above mapped out, I set to work on creating the surface of the webpage. Starting with [Figma](https://www.figma.com/file/fYDp7xJVwoSdtarTEg7e4n/Walkies-Design) I set out the structure I wanted to follow, and also made sure to cement a theme early on, which tied the whole website together.
I decided to use pastel colours as I wanted a playful and friendly website which would appeal to users of all ages. I also decided on a quirky font from Google Fonts and a background from [Harryarts @ www.freepik.com](https://www.freepik.com/vectors/background) which added more personaltiy to the web page.

<hr>

## Wireframes

- Desktop wireframe
![Desktop Design](https://browser-fe9a12bc-f34c-4c3b-98e3-d6bb3c2e7b81.ws-eu03.gitpod.io/workspace/Walkies/static/img/Desktop-wireframe.JPG)

- Mobile wireframe
![Mobile Design](https://browser-fe9a12bc-f34c-4c3b-98e3-d6bb3c2e7b81.ws-eu03.gitpod.io/workspace/Walkies/static/img/Mobile-wireframe.JPG)

- Tablet wireframe
![Tablet Design](https://browser-fe9a12bc-f34c-4c3b-98e3-d6bb3c2e7b81.ws-eu03.gitpod.io/workspace/Walkies/static/img/Tablet-wireframe.JPG)

[Full Wireframe](https://www.figma.com/file/fYDp7xJVwoSdtarTEg7e4n/Walkies-Design)
<hr>

## Technologies used

- For this website, I have utilised HTML5, CSS3, JavaScript, Python, Jinja, MongoDB, Materialize and JQuery

[HTML5](https://en.wikipedia.org/wiki/HTML5)

- This language is used to build the overall body of the page, from text, to page structures.

[CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)

- CSS3 is used to style the elements on the page. CSS3 is responsible for the colour scheme, and the layout of the page.

[JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- JavaScript is used to manipulate the logic of the page. I used this extensively for the Drink Matcher page.

[JQuery](https://jquery.com/)

- JQuery is a JavasCript library which allows users to use pre-written code to achieve a JavaScript goal.

[Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- Python is an interpreted, high-level and general-purpose programming language. I used this for the brains of the app, making use of app routes and app views to carry out complex functions out of sight of the user.

[Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine))
- Jinja is an incredible tool used to help developers keep consistency across all pages through the use of Jinja templates. I also used Jinja to pull in data from MongoDB to display to users based on certain criteria.

[MongoDB](https://www.mongodb.com/)
- MongoDB is an object-oriented database program used to store data.
- I sued MongoDB to store user data such as *Owners*, *Walkers* and *Walks*, thishc using Jinja templating, would be shown to users based on specific conditions.

[Materialize](https://materializecss.com/)
- Materialize is a powerful tool which gives developers multiple snippets of code to use in their projects, which can then be styled through CSS3 and JavaScript.

[Font Awesome](https://fontawesome.com/)

- Font Awesome is a tool used to provide icons which add to the overall aesthetic of the web page.

[Google Fonts](https://fonts.google.com/)

- Google Fonts provides the user with different options for fonts to be used in web pages, further adding to the personalization of each page.

[Google Maps API](https://developers.google.com/maps/documentation/javascript/overview)
- I used tne Google Maps API to display maps of certain areas, and specific areas within these to serve as inspiration to users for where to go on walks.

<hr>

## Features

With a multi page design, I deceided to make this easy for users. The home page has account registration buttons and sign in buttons. These buttons are only viewable in the user is not already signed in to avoid confusion and to avoid errors with multiple sign-ins.

tying the page together is a responsivenav bar which is set out in an indusry style fashion and features a variety of buttons depending on if the user is logged in or not.

Once you are signed up as an owner you are taken to your profile page, from here you are able to create bespoke walks for your dog. Once created, you can read, edit or delete these as you wish, these walks the display on your profile page.

Once you are signed up as a walker, you are shown to your profile page, on this page you are shown a list of collapsible lists which shows dogs available to walk, if you match the preferred age group and location specifications outlined by the owner. From here you can email the owner via a link ont he website which opnes your operating system's default email app with the owner's email address already inserted into the address bar.

On the index page, users are also able to view various maps of each of the 5 areas, these maps show different types of walks in each area and stand to serve as inspriation for new users, I opted not to use marker clusters for these maps as the maps are already centered on the locations stated above it, and this gives users to have a look around the surrounding area for their own inspiration.

## Desired Features

- I would have like to implement a feature that automatically emails users upon a successful account registration but due to time constraints from fixing other bugs, I was left unable to do this.

- The ability to upload an image to the website and use this as a user's profile picture would have really brought this all together, but after having asked multiple people about the possibility of this, I was put off the idea due to the constraints of MongoDB.
<hr>

## Testing

- User Feedback: My main goal with ny project is to have the pag elive as soon as possible so i can conduct thorough testing from the off. With Walkies I found this to be paramount in fixing any bugs quickly, and with the user experience in mind.

- When my page first went live, mobile users encountered whitespace at the bottom of the page due to my body element having the wrong height values, this was quickly fixed using mobile breakpoints and @media querys.

- Another piece of feedback I recieved was that when an *owner* would register, they would be presented with all of the walks in the database, and not just the ones they had created, this was due to my extremely new knowledge of Jinja, and this was fixed with the help of The Code Institute tutors.

- Similar to the above, my users found that if they registered as a *walker*, they were presented with ALL of the walks in the database, and not ones they were matched to based on certain conditions. This was also a Jinja error whihc was fixed by re-routing my flask aspp to draw data from one app view and not 3 at once. This not only saved the project purpose, but cemented my knowledge of Jinja template routing.

<hr>

## Code Validation

### HTML Validator (W3C):

All of my pages pass validation through the URL validator https://validator.w3.org/nu/, the only warnings present on each page is to do with code comments containing too many hyphons which does not affect the page in any way shape or form.

Here are screenshots of my code being passed through a URL validator.

 [HTML Code Validation](static/code-validation/html).

### CSS Validator (W3C):

All of my pages had the same errors in the CSS, however all of the errors were to do with imported styles from Materialize.min.css, clean-blog.css and overwritten styles due to my use of Chrome Dev Tools. As a result of this, these do not pass validation but also do not detract from the sie in any way.

My pages also had multiple warnings due to the validator not recognizing -webkit-, -o-, -ms-filter, and so on. As these are warnings, they do not affect the page in anyway and are simply there to make sure my CSS styling carrie sover to multiple web browsers.

Here is a screenshot of my CSS errors.

 [CSS Code Validation](static/code-validation/css).

### JavaScript Validator (JSHint)

- My Javascript all passed Validation except for my Maps.js, which didn't actually fail, but JSHint showed I had unused variables in my code. While this does not break the page, it would make readibility and editing harder.

[JavaScript Errors](static/code-validation/javascript).

### Python Validator (Extendsclass.com)

- Shockingly to me, my Python code had no errors. With this being my first time using this language, I am over the moon about this fact.

<hr>

## Responsiveness

This website's was tested using responsiveness was tested using Chrome Developer Tools exclusivley due to hardware limitations.

The onlytesting carried out on Safari was on my Iphone, but as stated in the above user story, this showed an issue with the body's background height.

### Chrome Developer Tools

- Chrome Developer Tools are extremely useful for testing a website's responsiveness due to the vast amount of layouts it provides.

Navigating my page on all screen sizes, and the 'responsive' function helped me to ensure a smooth UI across every page.

The in-browser styling also helped to quash any design flaws with the page, most recently, an issue with my walker-profile.html, which due to a misplaced end div tag, my footer was a part of the profile container.

Another issue I ran into with testing this way was an issue with my hero image on the landing page. On smalle rscreens, the image would become compressed and the contents would hide behing the body and the hero-image became scrollable to make up for this. Using the in-browser styling, I quickly made breakpoints for the hero-image and it's content, and this has now kept the hero image responsive.

<hr>

## Testing Links

- With a new way to re-route users, manual testing of all links on the page was of extremely high importance. 

- All of my links redirect users properly and to exaclty where they expect.

- My social media links all open in a new blank tab as to not take away from the UX.

- As mentiones in a user story, my page logo also acts as a home button.

- The back-to-top button works as intened on all pages with the body height to utilise it.

<hr>

## Database Entries / Data Retrieval

With the use of MongoDB, I had to make sure that every new entry into the database was easily readable and made sense as to what pieces of data were being entered.

With the data being entered in correctly, this led me to need to be able to retrieve this from my database using the @app.route function in Python.

The CRUD function for this project was the most difficult thing for me to pull off, it required me to give the *owners* the ability to create a *walk* which went into a new database collection, this collection could then be used to route into in order to edit or delete this *walk*. This also afforded me the chance to complete the below mentioned function.
 
After multiple hours, I have made it so when a *walker* and a *walk* share the same *location* and the *walker's* *age_group* matched the *Walk's* *preferred_age_group* in the database, the *walker* would be shown matched dogs to walk, and the owner's email address in order to contact them. 

<hr>

## Project Deployment

My project was created exclusivley in GitPod and using Git Version Control, I was able to periodically commit and push my code to GitHub.

This project is also hosted on Heroku, and using automatic deployments from GitHub, this is a mirror of my original code.

- To start this project, I had to create a GitHub profile, I then created a new repository using the on-screen instructions. When setting up my repository,

- I utilized the Code Institute template which provides basic boiler text.

- Once my code was written, and pushed to GitHub, I opened up my GitHub profile and navigated to the settings in my repository.

- From the settings, I scrolled down to the GitHub Pages section and selected the _Master Branch_ source.

- With these settings confirmed, the page is now live on GitHub Pages, and free to view by all in a web browser.

- I created a Heroku account by first navigating to [Heroku](https://dashboard.heroku.com/apps), and creating an account. From here, I selected create a new app, and this brought me to create an app name and select the region for it's hosting.
From here, I entered in my GitHub details and linked the account.
In the app settings, perhaps ne of the most important parts of this project, I entered in multiple variables into the section labelled 'config vars'. These config vars are hidden from any code pushed to GitHub and Heroku unless you are the owner of the repository. These config vars are essential to the connection between my app and MongoDB, utilizing my 'SECRET_KEY', 'MONGO_URI', 'MONGO_DBNAME', 'PORT' and 'IP' variables set up in my env.py file on GitPod.

- Once my repository was created on GitHub, I was able to link this to my Heroku profile.

- Any users wishing to view this code, or if they would like to use it for inspiration, they can do so on [My GitHub Page](https://github.com/DamSenton/Walkies)

<hr>

## Content

All content for this website is fictional, and was written by myself for creative and scholastic purposes.

The images for the website were taken from Google images using advanced search.

## Code

Most of the code for this project was written by myself, however, as stated in code comments in my style.css file, the back-to-top button was provided by [Heather Tovey](https://heathertovey.com/blog/floating-back-to-top-button).

For extra style accross the page, I opted to use a new blcok divider, this was free to use from [Codepen.Io](https://codepen.io/stg/pen/ZYYQMJ)

The code for my python functions was taken and refactored from the task-manager-flask-app Code Institute mini project.

I took inspiration from previous projects and used old code such as my nav-bar-hide.js code.

Some of the CSS has been provided by the 'Clean-Blog' template provided by [Start Bootstrap](https://startbootstrap.com/theme/clean-blog)

<hr>

## Special Thanks

A special thanks to my family and frineds for keeping me sane during this taxing project and a very weird time concerning lockdown.

A thank you to my wife for unlimited cups of tea and coffee to keep me going, and for putting up with my tantrums when things didn't go my way, but in doing, when does it ever??

And also to myself, for always pushing forwards thorugh the hard times and making websites that I am passionate about.
