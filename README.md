# Photo portfolio

Welcome to my photos portfolio page! Here you will be able to see some of my work I gathered over time and during my travels. I welcome you to make your self comfortable, enjoy the images and if you like some of them, why not consider purchasing them?

Contents:
* UX (user experience)
  * [Idea](#idea)
  * [Research and preparations](#research-and-preparations)
  * [Wireframes](#wireframes)
  * [User stories](#user-stories)
  * [Design choices](#design-choices)
    * [Fonts](#fonts)
    * [Colours](#colours)
    * [Icons](#icons)
* [Features](#features)
* [Features left to implement](#features-left-to-implement)
* [Technologies used](#technologies-used)
* [Testing](#testing)
    * [Bugs during development](#bugs-during-development)
    * [User stories Testing](#user-stories-testing)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Content](#content)
    * [Acknowledgments and thank you's](#acknowledgments-and-thank-you's)
* [Disclaimer](#disclaimer)

# UX 

## Idea
The idea behind this project was to present the pictures I gathered over time and during my travels. I was always fascinated by the mutual relationships of different spaces, colours and how they all work together, especially in nature. This why most of my pictures are about nature. My other interest is gaming where this fascination with space and colours didn't get ignored. Even if games are property of their publishers/ developers, I decided to include some of them, as pictures here are a result of my own effort.

As my collection of pictures was increasing, I decided to use it and make a portfolio website where I can possibly profit out of a static resource which are images. That is why I set up a web site with portfolio of my work which can serve as an online shop.

As this is only for educational purposes, I will not be charging for the images or sending them out just yet, and if someone tries to buy something, there wilL be a notification not to use their real bank card.

The scope of this project will be localized on just the images I made, and potential customers will be able to select the size of the image they order. Making this site to be a platform where I can make my living of, is not in the scope of this project, but it's open to the possibility.

I chose to make this project because of the following:
* I love to travel
* I like making photos
* I can make some profit out of it
* I can see which of my pictures are more desirable so I can improve on my photography and editing skills
* it gives me exposure

[Backt to top](#photo-portfolio)

## Research and preparations

Idea for this website came to me while I was talking to a fellow student and I saw this as a viable topic. When I saw his project, I liked it and started looking online for some inspirations to see how difficult will this be considering my skills and timeframe I had.

After going through photo portfolio pages, I found one which served as an inspiration for my project.

Going through all of these portfolio pages, I noticed that all of them some things in common:
* minimalistic design
* very few colours used which made photos stand out
* name of the owner on the initial page
* very little text, mostly for navigation
* some of the best effects I found on the internet in regards to presentation


[Backt to top](#photo-portfolio)

### Wireframes

After the initial idea, I decided to make a couple of sketches and make wireframes for different platforms to have an idea of how the page will look like on different platforms. Software used for generating mockups was [Balsamiq](https://balsamiq.com/?gclid=EAIaIQobChMIzK-ozrWk6QIVF-vtCh1l-woMEAAYASAAEgJ_vvD_BwE). 
You can find all the wireframes in the [wireframes](#) folder.

After finishing the project, some of the design and features were changed:
- ...

## User stories

As a user:
1. As a new visitor to the page, I want to be able to find a nice landscape image to put in my living room
2. As a new visitor to the page, I want to be able to purchase images and get them delivered to my house
3. As a customer, I want to be able to chose different sizes for the images
4. As a recruiter, I want to see Vladimir's work and decide whether to hire him or not

As an owner:
1. I want to be able to display my work publicly
2. I want to be able to add, remove and edit the images
3. I want to be able to see the address where I should send the printed image if purchase has been made
4. I want to be able to see which images are most popular so I can make more similar ones

[Backt to top](#photo-portfolio)

## Design Choices
Based on the research I made browsing through some other photo portfolio pages, I decided to continue my approach from previous projects and that is making it simple and easy to navigate. I used Nate Leuebbe' page as an inspiration. You can find the link below in [Credits](#credits) section.

From this, I decided on the following:
- minimalism with very few colours so images can stand out and be in the focus
- the UI needs to be easy to navigate; each part of the page has to be easily acessible.
- uniform and appealing look
- put more focus on design - css transitions and JS effects are much more represented than on previous projects
- grayish font colours instead of solid black (or more pronounced shadow effects if black colour used)
- as image heavy page, I will be using Cloudinary API and their widget for more image controll instead of simple upload

For styling the page Bootstrap library was used.

### Fonts

The following fonts were chosen:
* For page name:
    - [Black Ops One](https://fonts.google.com/specimen/Black+Ops+One?selection.family=Black+Ops+One&category=Display&preview.text_type=custom&sidebar.open=true) goes with Open Sans and Roboto
* For accents:
    - [Montserrat](https://fonts.google.com/specimen/Montserrat) for titles and accents
* For all of the text:
    - [Open Sans](https://fonts.google.com/specimen/Open+Sans?query=open+sans) for regular text


### Colours

Colours used:

| Colours       | Hex           | Bootstrap value  | Used in         |
| :------------- |:-------------:| :-----:| :-----:|
| color1      | #ff7043 | deep-orange lighten-1 | titles, neutral buttons|
| color2      | #424242 | grey darken-3 |navbar, header and footer background|
| color3      | #00e676 | green accent-3 |for floating Icon and some buttons|



### Icons

Icons were used from a [FontAwesome page](https://fontawesome.com/). 

[Backt to top](#photo-portfolio)

# Features
As per the initial idea, UI has to have a uniform and appealing look, be easy to navigate, and be quick to get anywhere on the page within 3 clicks. For this reason, multi-page concept was implemented. Thanks to Django, I used apps to cut down on repetitive tasks like creating everything from ground up.
as per [research](#research-and-preparations) and [design choices](#design-choices), I decided on these the following features:
* minimalistic design
* initial page with transparent header for navigation. Scrolling down reveals cards that stretch accross the screen and lead to a respective category
* search bar
* ability to sort the images by category, price and rating
* page dedicated to a single photo where people can read about it in more detail
* CRUD functionality: owner can Create, Read, Update and Delete content he created; users can see history of their purchases and rate the images
* super user account and one admin account which will be dedicated to me (for security reasons)
* Users can create and delete their account
* Image hosting will be handled by a third-party provider - [Cloudinary](https://cloudinary.com) as current storage capacities aren't adequate for a large number of images. 

## Features Left to Implement
...

[Backt to top](#photo-portfolio)

# Technologies Used

## Languages

* HTML5
* CSS3
* JavaScript
* JSON
* Python

## Others
- [Django](https://www.djangoproject.com)
- [Stripe](https://stripe.com)
- [JQuerry](https://jquery.com/)
- [Flask 1.1.2](https://palletsprojects.com/p/flask/)
- [Jinja2 2.11.2](https://pypi.org/project/Jinja2/)
- [Cloudinary 1.21.0](https://cloudinary.com/)
- [Git](https://git-scm.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Google fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
- [Heroku](https://www.heroku.com/)
- [GitHub](https://github.com/)
- [Balsamiq](https://balsamiq.com/) 
- [VS Code](https://code.visualstudio.com/) 
- [W3C Markup](https://validator.w3.org/)
- [W3C CSS](https://jigsaw.w3.org/css-validator/)
- [jshint](https://jshint.com/) 

for more details and dependencies, please refer to [requirements.txt](#) file

[Backt to top](#photo-portfolio)

# Testing

#### Browser and Device Testing on Heroku page

| **Browser**      | **Device** | **Compatibility**                                            | **Version**            |
| :--------------- | :---------: | :-----------------------------------------------------------: | :--------------------- |
| Google Chrome    | PC         |         ???                                             | Version ?? (x64)|
| Firefox          | PC         |          ???                                           | Version ??      | 
| Opera            | PC         | ??? | Version  ??|
| Google Chrome | OnePlus 3t  |      ???                                               |      Version ??  |
| Opera Touch | OnePlus 3t  | ???                                                    | Version ??       |
| Safari           | iPad Mini   |        ???                                             | Version ??          |

- [ ] Test links to all pages
- [ ] Try to access the user area without signing in
- [ ] Test filtering dropdowns
- [ ] Test searching
- [ ] Test photo info page
- [ ] Test errors by typing in random page redirects
- [ ] Test account registration
- [ ] Test log out 
- [ ] Test sign in
- [ ] Test admin page
- [ ] Test add new image
- [ ] Test add / del image
- [ ] Test update image
- [ ] Purchasing test
- [ ] Test basket
- [ ] Test purchasing
    - [ ] Test if all required fields are filled
    - [ ] Test redirects after purchasing
    - [ ] Test going back after purchase has been made

## User Stories Testing

As a user:
1. As a new visitor to the page, I want to be able to find a nice landscape image to put in my living room
    - any new visitor to the page is greeted with an image that stretches accross the whole screen. From there, visitor can either use the nav bar on the top, click on the arrow on the botom or just scroll.
2. As a new visitor to the page, I want to be able to purchase images and get them delivered to my house.
    - during each purchase, user is asked to fill in a form with his full address so the image can be delivered to him.
3. As a customer, I want to be able to chose different sizes for the images
    - as above, during the purchase, user can select which size he wants: S, M or L. Each size has dimensions in mm so the user has an idea of how big a delivered image will be.
4. As a recruiter, I want to see Vladimir's work and decide whether to hire him or not
    - All of the best images are displayed on this web page, and everyone can sort them by category, panorama or not, colour or black/white, name, rating, price and top rated.  This will make the recruiter's job much easier.

As the owner:
1. I want to be able to display my work publicly
    - all images will be hosted on Heroku where they will have exposure to everyone on the internet, accessible 24 hours a day - every day.
2. I want to be able to add, remove and edit the images
    - thanks to forms and Cloudinary, images can be easily uploaded, manipulated and deleted.
3. I want to be able to see the address where I should send the printed image if purchase has been made
    - users won't be able to complete their purchase if the address is missing. This is where the image should be sent.
4. I want to be able to see which images are most popular so I can make more similar ones
    - thanks to rating system, it will be possible to see which images are more popular.

[Backt to top](#photo-portfolio)

### Bugs During Development

**List of bugs found:**

* **Description:** text in the top navbar wouldn't align to the midle of the container horizontally
    * **How I found it:** after adding a class of ``align-items-center`` text wouldn't align 
    * **What went wrong:** ``row`` class didn't have the same height as the parent ``container``
    * **Resolution:** added class of ``.mheight-3-5`` to the ``row`` container which equalized both containers in height

* **Description:** 
    * **How I found it:** 
    * **What went wrong:** 
    * **Resolution:**

[Backt to top](#photo-portfolio)

# Deployment
The repository for this project is hosted on [GitHub](https://github.com/) and uses [Heroku](https://www.heroku.com/) to serve the site to the world wide web. If you would like to contribute to this project you would need to first have some sort of online code editor like [Gitpod](https://www.gitpod.io/) or local such as [VS Code](https://code.visualstudio.com/). Also you will need some version control software like [Git](https://git-scm.com/). For Git, you will also need a GitHub account.

#### Prerequisites

In order to contribute to this repository, you will need to have the following installed:

- Python 3.8.3 or higher
- Git version control
- Code editor - [Gitpod](https://www.gitpod.io/) or [VS Code](https://code.visualstudio.com/) are recommended

#### Development

There are a number of steps required to deploy a local version of this project. 

##### Local copy

- At the top of the repository click on the **Code** button and select *Download zip*
- Copy the path to the repo "https://github.com/Vlad-404/#"
- Navigate to the folder where you would like to make a copy of this repository - *"C:\WorkFolder\MyRepo\..."* and save.
- Start VS Code and click on *"File -> Open Folder..."*
- Navigate to the downloaded files *"C:\WorkFolder\MyRepo\..."* and click on "Select Folder"
- If you don't have your environment set up, please refer to the VS Code documentation
- Install all the dependencies by typing in the terminal: ``pip3 install -r requirements.txt``
- If you add or update any new packages to the project use ``pip freeze --local > requirements.txt`` to update the [requirements.txt](requirements.txt) file with the new dependencies.

##### Environment Variables

You will need to setup the following environment variables on your system.

| Variable name         | Used for                 | Notes                                                        |
| --------------------- | ------------------------ | ------------------------------------------------------------ |
| CLOUDINARY_CLOUD_NAME | Cloudinary Image package | Found in your Cloudinary account dashboard                    |
| CLOUDINARY_API_KEY    | Cloudinary Image package | Found in your Clouinary account dashboard                    |
| CLOUDINARY_API_SECRET | Cloudinary Image package | Found in your Clouinary account dashboard                    |
| MONGO_DBNAME       | Mongo DB                 | This is the name of your database collection e.g.: "photo-portfolio" |
| MONGO_URI          | Mongo DB                 | Found in the connect button on the database cluster          |
| SECRET_KEY        | Session Variables        | This is a unique secret used for cookie encryption,  you can use any random string for this |
| IP                    | Flask                    | You can use `0.0.0.0` here to indicate a local IP address    |
| PORT                  | Flask                    | You can use the default port `5000`                          |



> Note: you will need to add these environment variable to your GitHub repo in "env.py" and Heroku  in "settings -> config vars"

[Backt to top](#photo-portfolio)

##### Deployment

The easiest way to deploy the project to Heroku is to set your connect method to GitHub and link the repository master branch. If you set the project up for automatic deploys, it will deploy once the master branch is updated.

My photo portfolio site was developed on GitPod and VS code, using GitHub and Heroku to host the repository. As GitHub pages cannot host dynamic pages, for this purpose I used Heroku.

When deploying photo portfolio using Heroku, the following steps were taken:

Linking the Heroku and GitHub:
* Log in to [Heroku](https://www.heroku.com/) and [GitHub](github.com)
* Make sure you have admin privileges on GitHub
* Go to Heroku and select photo-portfolio app
* Click on Deploy and in Deployment method, select GitHub(Connect to GitHub)
* Select repository to connect to
* Enter repo name in the empty field and click on search. Be sure your repo exists on GitHub and that you typed it in correctly.
* When repo shows click on "Connect"
* Your Heroku app will be synchronised each time you "git push"
* Website is now live on Heroku. To run the site, click on "Open App" at the top

If GitHub asks you to authorize the Heroku app in any of the steps above, do so, and you will be able to do an automated deployment from GitHub to Heroku.



# Credits

## Content
All of the images were made by me. I used various cameras to capture the images. Even if I was carefull not to include any logos, business names or faces, if you find anything related to yourself, and you don't want it contained in my photos, please contact me on vmijat21@gmail.com and explain the situation. I will be glad to answer and correct if there are any issues you find with my photos.

## Acknowledgments and Thank-Yous

- Big thanks to Nate Luebbe whos page served as an inspiration to my project. You can find his page here: [Nate Luebbe](https://www.nateluebbe.com/)
- Sidenav for mobile devices used from w3schools: https://www.w3schools.com/howto/howto_js_sidenav.asp

[Backt to top](#photo-portfolio)

# Disclaimer

This page was built for educational purposes and all resources were used under fair usage and/or under free licence! If you find any content that violates the copyrights, please contact me on vmijat21@gmail.com

Thank you for visiting my page and I hope you'll have fun browsing through my images as I did making them.

[Backt to top](#photo-portfolio)