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

## Features

With a multi page design, I deceided to make this easy for users. The home page has account registration buttons and sign in buttons. These buttons are only viewable in the user is not already signed in to avoid confusion and to avoid errors with multiple sign-ins.

tying the page together is a responsivenav bar which is set out in an indusry style fashion and features a variety of buttons depending on if the user is logged in or not.

Once you are signed up as an owner you are taken to your profile page, from here you are able to create bespoke walks for your dog. Once created, you can read, edit or delete these as you wish, these walks the display on your profile page.

Once you are signed up as a walker, you are shown to your profile page, on this page you are shown a list of collapsible lists which shows dogs available to walk, if you match the preferred age group and location specifications outlined by the owner. From here you can email the owner via a link ont he website which opnes your operating system's default email app with the owner's email address already inserted into the address bar.

On the index page, users are also able to view various maps of each of the 5 areas, these maps show different types of walks in each area and stand to serve as inspriation for new users, I opted not to use marker clusters for these maps as the maps are already centered on the locations stated above it, and this gives users to have a look around the surrounding area for their own inspiration.

## Desired Features

- I would have like to implement a feature that automatically emails users upon a successful account registration but due to time constraints from fixing other bugs, I was left unable to do this.

- The ability to upload an image to the website and use this as a user's profile picture would have really brought this all together, but after having asked multiple people about the possibility of this, I was put off the idea due to the constraints of MongoDB.


