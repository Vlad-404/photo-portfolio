As every project, this one had them too. Instead of making a long list in the readme, I moved bugs to a separate file:

### List of bugs found

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

[Back to top](#)

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

[Back to top](#)

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

[Back to top](#)

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
    * **How I found it:** While testing the site on Safari(iPad mini)
    * **What went wrong:** Wrong link was given to `cart.html` when pressing `Remove` button
    * **Resolution:** Fixed the template name from `button-back.html` to `cart/buttons-back.html`


[Backt to top](#)