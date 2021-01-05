# Photo portfolio

![Desktop Demo](https://res.cloudinary.com/drtxn8d5t/image/upload/v1609721113/photo-portfolio/display-images/mockup_aso6tx.png "Desktop Demo")

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
    * Content
    * Acknowledgments and thank you's
* [Disclaimer](#disclaimer)

# UX 

## Idea
The idea behind this project was to present the pictures I gathered over time and during my travels. I was always fascinated by the mutual relationships of different spaces, colours and how they all work together, especially in nature. This is why most of my pictures are about nature. My other interest is gaming where this fascination with space and colours didn't get ignored.

As my collection of pictures was increasing, I decided to use it and make a portfolio website where I can possibly profit out of a static resource which are images. That is why I set up a web site with portfolio of my work which can serve as an online shop.

As this is only for educational purposes, I will not be charging for the images or sending them out just yet, and if someone tries to buy something, Stripe payment system won't let them untill I activate my account.

The scope of this project will be localized on just the images I made. Making this site to be a platform where I can make my living of, is not in the scope of this project, but it's open to the possibility.

I chose to make this project because of the following:
* I love to travel
* I like making photos
* I can make some profit out of it
* I can see which of my pictures are more desirable so I can improve on my photography and editing skills
* it gives me exposure

[Back to top](#photo-portfolio)

## Research and preparations

Idea for this website came to me while I was talking to a fellow student and I saw this as a viable topic. When I saw his project, I liked it and started looking online for some inspirations to see how difficult will this be considering my skills and timeframe I had.

After going through photo portfolio pages, I found one which served as an inspiration for my project: [Nate Luebbe](https://www.nateluebbe.com/).

Going through all of these portfolio pages, I noticed that all of them some things in common:
* minimalistic design
* very few colours used which made photos stand out
* name of the owner on the initial page
* very little text, mostly for navigation
* some of the best effects I found on the internet in regards to presentation


[Back to top](#photo-portfolio)

### Wireframes

After the initial idea, I decided to make a couple of sketches and make wireframes for different platforms to have an idea of how the page will look like on different platforms. Software used for generating mockups was [Balsamiq](https://balsamiq.com/?gclid=EAIaIQobChMIzK-ozrWk6QIVF-vtCh1l-woMEAAYASAAEgJ_vvD_BwE). 
You can find all the wireframes in the [wireframes](https://github.com/Vlad-404/photo-portfolio/tree/master/wireframes) folder.

After finishing the project, some of the design and features were changed:
- I removed the ability for users to rate the images due to time constrains
- Image purchase is now available to everyone instead of just registered users
- Image upload app is now part of the `image_presentation` app
- `basket` has been renamed to `cart` for better assotiation with shopping
- Different image sizes were removed from purchasing a it took too much time to implement
- Removed the ability to purchase the same item from order history
- I added a separate page instead of full page modal where visitors and users can see an image accross the full page and decide about their purchase;
And some minor UI changes. If you want to know more, scroll down to *[Features Left to Implement](#features-left-to-implement)*.

## User stories

As a user:
1. As a new visitor to the page, I want to be able to find a nice landscape image to put in my living room
2. As a new visitor to the page, I want to be able to purchase images and get them delivered to my house
3. As a customer, I want to be able to chose different sizes for the images
4. As a recruiter, I want to see Vladimir's work and decide whether to hire him or not
---
5. I want to be able to display my work publicly
6. I want to be able to add, remove and edit the images
7. I want to be able to see the address where I should send the printed image if purchase has been made
8. I want to be able to see which images are most popular so I can make more similar ones

[Back to top](#photo-portfolio)

## Design Choices
Based on the research I made browsing through some other photo portfolio pages, I decided to continue my approach from previous projects and that is making it simple and easy to navigate.

From this, I decided on the following:
- minimalism with very few colours so images can stand out and be the focus of the site
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
* For amost of the site:
    - [Montserrat](https://fonts.google.com/specimen/Montserrat) for most of the page as it fits well with...
* For all of the form and smaller text:
    - [Open Sans](https://fonts.google.com/specimen/Open+Sans?query=open+sans) for forms, descriptions, sub-menu and small text


### Colours

Colours used:
Most of the colours are brought down to a [minimum](#design-choices). Grayish colours were used for navigation butons, navbars, footer while elements that have site wide impact used bootstrap colours(info, primary, danger,...)

| Colours       | Hex           | Bootstrap value  | Used in         |
| :------------- |:-------------:| :-----:| :-----:|
| gray      | #5a6268 | `element`-secondary | nav buttons, navbars, rules, message backgrounds|
| gray      | #5F5F5F90 | none | navbars, and everywhere I needed transparency|
| blue      | #0275d8 | `element`-primary | messages |
| teal       | #5bc0de | `element`-info |messages from cart, infos, free delivery info, edit and update buttons |
| yellow       | #fff3cd | `element`-warning | free delivery info |
| red       | #c82333 | `element`-danger | buttons for deleting, checkbox and text in image upload form, error messages in forms, messages |


### Icons

Icons were used from a [FontAwesome page](https://fontawesome.com/). 

[Back to top](#photo-portfolio)

# Features
As per the initial idea, UI has to have a uniform and appealing look, be easy and intuitive to navigate. For this reason, multi-page concept was implemented. Thanks to Django, I used apps to cut down on repetitive tasks like creating everything from ground up.

As per [research](#research-and-preparations) and [design choices](#design-choices), I decided on these the following features:
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

The following features were left for future implementaions:
* Different image sizes with respective prices - printing a small image is not the same as printing a large panorama image. Adding different price for different size required more coding and as a beginner with Django, I didn't had time to add relation between size and price while purchasing.
* Rating system - it took too long to implement
* Adding category and social links - it can be added through the admin console, but adding them through the site UI was left out
* Sorting within a selected category in image gallery - while it is an integral part of the page, it doesn't have a significant impact on page functionality, so it was left out untill future implementations. Current functionality only supports sorting of all images.

[Back to top](#photo-portfolio)

# Technologies Used

## Languages

* HTML5
* CSS3
* JavaScript
* JSON
* Python

## Tools, frameworks and librarys
- [Django](https://www.djangoproject.com)
- [Stripe](https://stripe.com)
- [JQuerry](https://jquery.com/)
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

[Back to top](#photo-portfolio)

# Testing

#### Browser and Device Testing on Heroku page
Other than some long initial loading times on deployed Heroku page on majority of devices, following platforms were tested:

| **Browser**      | **Device** | **Compatibility**                                            | **Version**            |
| :--------------- | :---------: | :-----------------------------------------------------------: | :--------------------- |
| Google Chrome    | PC         |         Excellent                                             | Version 87.0.4280.88 (Official Build) (64-bit) (x64)|
| Firefox          | PC         |          ???                                           | Version ??      | 
| Opera            | PC         | Excellent | Version 73.0.3856.284(x64)|
| Google Chrome | OnePlus 3t  |      ???                                               |      Version ??  |
| Opera Touch | OnePlus 3t  | Excellent                                                    | Version 2.8.4       |
| Safari           | iPad Mini   |        ???                                             | Version ??          |

#### Testing per device
( [x] = pass, x = failed)

| **Test**      | **Google Chrome(PC)** | **Opera(PC)** | **Firefox(PC)** | **Opera Touch(mobile)** | Safari(iPad mini) |
| :---------------------------- | :------: | :-----: | :--------------: | :--------------: | :--------------: |
| Test links to all pages    | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Try to access the user area without signing in    | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test search    | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test messages   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test filtering    | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test link to contact form outside home page    | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test photo info page    | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test hide sidebar   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test adjusting the quantity for purchase in image view   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test adding to cart   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test update cart quantity   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test remove from cart   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test adding to cart   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test purchase form   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Purchase form - wrong form field entry   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Purchase form - wrong payment details   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Purchase form - save info for future purchases   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Purchase form - webhooks by monitoring Stripe dashboard   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Purchase form - interrupted payment process   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test update default delivery info saving   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test account registration   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test email registration   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test login   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test logout   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test add new image   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test modify image   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test delete image   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test edit/remove image buttons displaying for different types of accounts  | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test reject access to admin pages if user is not admin   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test filling the contact form on home page | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test sending contact request mails   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |
| Test sending purchase confirmation email   | [x]         |   [x]       | [x]|       [x]  |  [x] |   [x] |

During testing, these errors were found and corrected:
- Removing an item from cart manually resulted in 500 error. 

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
    * **Bug ID:** #001
    * **How I found it:** after adding a class of ``align-items-center`` text wouldn't align 
    * **What went wrong:** ``row`` class didn't have the same height as the parent ``container``
    * **Resolution:** added class of ``.mheight-3-5`` to the ``row`` container which equalized both containers in height

* **Description:** Carousel on the home page sometimes just stops changing the images
    * **Bug ID:** #002
    * **How I found it:** While editing code on the home page
    * **What went wrong:** Bootstrap code(?)
    * **Resolution:** Lowered the time needed for images to change. It still occurs occasinally, but it has no consistent pattern. Because of this and low impact on the site, it was left unresolved

* **Description:** While trying to migrate `images` model, django refused and threw an error
    * **Bug ID:** #003
    * **How I found it:** While trying to `makemigrations` with images model, _"You are trying to add a non-nullable field 'category' to images without a default"_ error, and wouldn't make any migrations
    * **What went wrong:** Probable cause was editing already existing model
    * **Resolution:** Added `deafult=None` to every field that django required and hasn't got `default` value

* **Description:** Couldn't migrate changes to `Images` model after adding a foreign key for `categories`
    * **Bug ID:** #004
    * **How I found it:** I got `django.db.utils.IntegrityError` while trying to apply migrations to `Image` model
    * **What went wrong:** I didn't relate `categories` model with `Images` model before I loaded fixtures. This resulted in mismatch in key values of ID in `categories` model and raised an error
    * **Resolution:** I deleted all of the objects in `Image` model and added them through fixtures

* **Description:** No categories were showing in categories section of `index.html`
    * **Bug ID:** #005
    * **How I found it:** After fixing the bug with integrity error (see above)
    * **What went wrong:** `for loop` in `index.html` template had `categories` as a reference instead of `category` (i.e. `categories.name` instead of `category.name`)
    * **Resolution:** Changed `categories` to `category` in `for` loop

* **Description:** If search query is empty, no results were displayed(expected behaviour) and no message was displayed after page loaded
    * **Bug ID:** #006
    * **How I found it:** When initiating search in search form while form is empty
    * **What went wrong:** 
    * **Resolution:**

* **Description:** Issue with tooltips showing
    * **Bug ID:** #007
    * **How I found it:** After hovering over tooltiped item( i.e. icon to show/hide sidebar in image details page), tooltip didn't show
    * **What went wrong:** Bootstrap issue?
    * **Resolution:** I left it unresolved as there is no consistency to track it down and it wasn't a critical error

* **Description:** Couldn't start server in Gitpod
    * **Bug ID:** #008
    * **How I found it:** By typing `python3 manage.py runserver` in terminal
    * **What went wrong:** After moving environmental variables to a separate file (`env.py`), syntax for database link in `settings.py` was incorrect
    * **Resolution:** Changed `env.get` to `os.getenv`

* **Description:** Deployed page gave 500 error when adding to cart
    * **Bug ID:** #009
    * **How I found it:** While testing the functionality on Heroku's deployed page
    * **What went wrong:** In `image-view` template, wrong variable was passed on
    * **Resolution:** Changed passing variable from `image_id` to `image.id` in `image-view.html`

* **Description:** Quantity for items in cart would not update after adjusting and clicking/tapping on *Update*
    * **Bug ID:** #010
    * **How I found it:** While trying to modify the quantity in cart
    * **What went wrong:** JavaScript didn't initialize the `adjust_cart` function
    * **Resolution:** Moved `anchor` link inside the form and converted it to `button` with `type="submit"`

* **Description:** No payment intent was sent to Stripe after filling in delivery details
    * **Bug ID:** #011 in relation to #010
    * **How I found it:** While submiting a payment intent and monitoring events and logs on Stripe side
    * **What went wrong:** Forms that were submiting the payment intent were using environmental variables stored in Gitpod settings(from previous project) instead of `env.py` file. This also affected any other form submission as `SECRET_KEY` was invalid(related to BID#010)
    * **Resolution:** Deleted environmental varibles in Gitpod settings

* **Description:** Could not upload an image through template
    * **Bug ID:** #012
    * **How I found it:** While trying to add image through `gallery/add_image.html` template in `image_presentation` app
    * **What went wrong:** Missing `%` in href for form in `add_image.html` template resulted in browser not properly encoding the page and throwing 400 error
    * **Resolution:** Added `%` to `action="{% url 'add_image' }"` for the form that submits the new image entry

* **Description:** No image was shown in cart nor in toast success after adding image to the cart
    * **Bug ID:** #013
    * **How I found it:** By adding image to the cart
    * **What went wrong:** Wrong variables used in `if` statements
    * **Resolution:** Changed `{% if images.imgurl == None %}` to `{% if item.images.imgurl == None %}`. Error occured during Cloudinary implementation where I had to add this `if` statement because images prior to that were not uploaded through this site. Instead, only url was used.

* **Description:** Messages are not showing in any template other than cart
    * **Bug ID:** #014 in relation to #006
    * **How I found it:** Anytime message was supposed to be displayed(error, info, success,...)
    * **What went wrong:** Jquery that shows toast was not loading. It was present as `block postloadjs` in cart app which explains why it was displaying messages only there
    * **Resolution:** Moved `<script src="{% static 'js/script.js' %}"></script>` from `<head>` to bottom of the body

* **Description:** Removing image from cart sometimes took multiple times to succeed
    * **Bug ID:** #015
    * **How I found it:** While testing the functionality for mobile screens
    * **What went wrong:** Javascript was causing the issue
    * **Resolution:** Removed the Javascript at the bottom of the `cart.html` template

* **Description:** No message after search couldn't find the search term
    * **Bug ID:** #016
    * **How I found it:** By testing search for mobile devices. Discovered that there was the same issue for any other screen size.
    * **What went wrong:** There was no handler that handled situations where there was no result from the search term
    * **Resolution:** Added `if` statement in `image_presentation.views.all_images` under "`if 'search' in request.GET:`"

* **Description:** 500 error on Heroku(deployed) page
    * **Bug ID:** #017
    * **How I found it:** While testing the deplyed page on Heroku, I tried accessing all images and got 500 error
    * **What went wrong:** Config vars on Heroku didn't had the same name as in Gitpod
    * **Resolution:** Changed the names of config vars on Heroku to match ones in Gitpod

* **Description:** Noticable white space on image view page under image container
    * **Bug ID:** #018
    * **How I found it:** While refactoring the code for mobile screen sizes
    * **What went wrong:** `#full-size-image-container` had minimum width of 768px while parent container didn't had any overflow so the whole page was scaling with this
    * **Resolution:** Added `overflow-x: auto;` to image parent container `view-image-container`

* **Description:** Removing item from cart resulted in 500 error
    * **Bug ID:** #019
    * **How I found it:** While testing the site on Safari(iPad min)
    * **What went wrong:** Wrong link was given to `cart.html` when pressing `Remove` button
    * **Resolution:** Fixed the template name from `button-back.html` to `cart/buttons-back.html`

* **Description:** 
    * **Bug ID:** #020
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
| SECRET_KEY        | Session Variables        | This is a unique secret used for cookie encryption,  you can use any random string for this |





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

## Acknowledgments and Thank You's

- Big thanks to Nate Luebbe whos page served as an inspiration to my project. You can find his page here: [Nate Luebbe](https://www.nateluebbe.com/)
- Sidenav for mobile devices used from w3schools: https://www.w3schools.com/howto/howto_js_sidenav.asp
- Display for image cards in gallery was used from [bootstrapious.com](https://bootstrapious.com/p/bootstrap-photo-gallery) as free resource.
- Code from `quantity_input_script.html` for `+` and `-` buttons in image preview used from [Chris Zielinski](https://github.com/ckz8780) from [Code Institute](https://codeinstitute.net/) and most of the checkout app
- YouTube user [Majin Dev](https://www.youtube.com/channel/UCu7jaqMRRr8xpljmT7urxYA) and his [video](https://www.youtube.com/watch?v=m5O4sSVbzjw) on instructions how to set up Cloudinary in Django

[Backt to top](#photo-portfolio)

# Disclaimer

This page was built for educational purposes and all resources were used under fair usage and/or under free licence! If you find any content that violates the copyrights, please contact me on vmijat21@gmail.com

Thank you for visiting my page and I hope you'll have fun browsing through my images as I did making them.

[Backt to top](#photo-portfolio)