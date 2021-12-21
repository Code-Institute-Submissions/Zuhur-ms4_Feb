# JO<s>G</s>Y<s>M</s>

**Milestone 4 project for Code institute Software Development Programme.**
[Live site](https://milestone-four.herokuapp.com/)

## Table of contents
-   [User Experience](#user-experience)
-   [Design](#design)
    *   [Wireframes](#wireframes)
    *   [Database Schema](#database-schema)
    *   [Colours](#colours)
    *   [Fonts](#fonts)
-   [Features](#features)
    *   [Existing Features](#existing-features) 
-   [Technologies](#technologies)   
-   [Testing](#testing)
-   [Deployment](#deployment)


## User Experience
JOGYM is website for an alternate gym, providing all fundamentals required for a regular gym, but also offers a host of various physical activities such as indoor paintballing, rock climbing etc. to allow members to experience some joy in the gym when working out becomes repetitive or a plateau stagnates the workout. The gym offers monthly and annual subscriptions as well as an ecommerce section to provide merchandise to all users. This app is a Full Stack website created using the Django framework with a backend of PostgresSQL. <br>

Follow [this](/readme_files/ms4-user-stories.png) link to see a detailed view of the user stories.


## Design
### Wireframes
The wireframes were designed using the balsamiq tool for different sections and screen sizes. These can be found [here](/readme_files/ms4-wireframes.pdf).

### Database Schema
The database schema was designed using diagrams.net and can be found [here](/readme_files/ms4-schema.jpg)

### Colours
The colour palette was selected using Coolors website and can be found [here](/readme_files/ms4-palette.png)

### Fonts
Google fonts: Unica One

## Features

### Existing Features
Navigation bar: Responsive nav bar is present on all pages. If a user is logged in links to join/login are no longer present, and if the user is the admin they have a access to a product management link (yet to be developed).

Home page: Contains images of the gym showing various activities, scrolling down presents users with a concise about 'our gym' section. Any further questions invites user to contact us form for further information.

Products page: There is a search bar which allows terms found in title or description of an item. Users can filter by gender and further more by price. Navigation to further product detail is also provided through clicking image or the item name.

Item detail: Merchandise-detail page displays individual item information and allows user to add items to cart which increments/decrements everytime an item is added/removed to the cart. Furthermore they can choose to continue shopping or click the cart to navigate to the checkout page.

Checkout page: User is prompted to fill in the form to process payment. With successful registration, they are redirected to a confirmations page and provided with an order summary. Should the user want to delete all orders, text is shown that their bag is empty and a link to take them back to continue shopping.

Join/login: These pages are designed with help of django-allauth and handles user registration, login and logout details.

## Technologies

-	HTML5: For the structure of the site.
-	CSS3: For styling of the site.
-	Bootsrap5: For fast development of the site and its responsiveness.
-	Fontawesome: For visual icons.
-	Github: For remote access of the project.
-	Git: For version-control.
-	Visual Studio Code: A development environment as an upgrade to gitpod.
-	SQLite3: As the database for storing users data during development.
- PostgresSQL: As the database for storing users data during production.
- Python/Django: Used for the backend and for communication with mongodb.
- Heroku: Deployment of project.
- AWS S3 Bucket: As remote storage for static and media files.

## Testing
1. [PEP8](http://pep8online.com/) was used to check python file, until file was pep8 compliant. <br>
2. The HTML validator used was [https://validator.w3.org/](https://validator.w3.org/). Several errors caught due to jinja the other errors were corrected until no errors shown. <br>
3. The CSS validator used was [https://jigsaw.w3.org/css-validator/validator]( https://jigsaw.w3.org/css-validator/validator). <br>
Google devtools was used to make sure the site is responsive to different devices and screen sizes. <br>

### Manual Testing
#### Testing of user stories
Testing was carried out based on if the requirements for the user stories where met and can be found [here](/readme_files/ms4-testing.png). Due to the size of this project it was not possible to meet the requirements of all the user stories. More will be discussed in future implementations.

#### Future Features
The main feature required to be developed is the membership aspect of the website. Manual and annual subscriptions with automatic withdrawal of payment is the next step. Although users can filter products, filtering the price based on the categories rather than entire products list will also be implemented.

#### Bugs
Although static files are rendered somehow the images for the carousel stored within media are not rendering. Further testing is required to fix this bug.


## Deployment

### To clone repository
- Open [this](https://github.com/Zuhur/ms4) repository
- Select code in the following and clone using HTTPS or SSH
- Select the working directory you would like the repo to be cloned
- Type ‘git clone’ followed by URL decided above
- Create an env.py file as shown below, while replacing values with password and the name of the database <br/>
`import os` <br/>
`  os.environ.setdefault("DEVELOPMENT", "True")` <br/>
`  os.environ.setdefault("STRIPE_PUBLIC_KEY", <PUBLICKEY>)` <br/>
`  os.environ.setdefault("STRIPE_SECRET_KEY", <SECRETKEY>)` <br/>
`  os.environ.setdefault("STRIPE_WH_SECRET", <SECRET-WH-KEY>)` <br/>
- Install all the required requirements `pip3 install -r requirements.txt`
- Load data from db.json file
- Create superuser and run the application with `python3 manage.py runserver`

### To Heroku

- Login / sign up to Heroku
- Create a new app
- Select unique app-name
- Choose appropriate region
- Make sure there is a requirements.txt and Procfile since Heroku requires these.
- Heroku cannot read env.py files therefore the contents need to be manually input into config vars (via settings) 
- Enter values in env.py into config vars
- Push all code to GitHub
- Enable automatic deployment to allow automatic update when code pushed to GitHub

## Credits

### Images
From Pexels, picabay and unsplash <br>
Carousel images
  1. https://www.pexels.com/photo/bright-close-up-color-colorful-221247/
  2. https://cdn.pixabay.com/photo/2018/08/22/14/31/paintball-3623794_960_720.jpg
  3. https://unsplash.com/photos/20jX9b35r_M
Product images
  1. https://cdn.pixabay.com/photo/2017/07/02/19/24/dumbbells-2465478_960_720.jpg
  2. https://images.unsplash.com/photo-1602143407151-7111542de6e8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8d2F0ZXIlMjBib3R0bGV8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60
  3. https://cdn.pixabay.com/photo/2020/05/15/10/20/sweatpants-5173125_960_720.jpg
  4. https://images.unsplash.com/photo-1618354691373-d851c5c3a990?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8YmxhY2slMjB0c2hpcnR8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60
  5. https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80
