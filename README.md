# Wildlifers
(Developer: Ewart Hestick)

![Mockup image](docs/feature/amiresponsive.JPG)

[Live webpage](https://wildlifers.herokuapp.com/)


## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing of user stories](#manual-testing-of-user-stories)
    - [Automated testing](#automated-testing)
    - [Performing tests on various devices](#performing-tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Configuration](#configuration)
    - [Google emails](#google-emails)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)


## About
- Wildlifers are a group dedicated to saving and aiding wild life.  We save and help native animals who are close to extinction or similar.  
 

### User Goals
- Learn more about wild life 
- Use site features to help prevent wildlife distinction
- Sign up for to be a memeber of site
- Enroll in site programs
- Contact the Organisation
- Write and comment on blog posts

### Site Owner Goals
- Make people aware of wild life distinction
- Offer programs that contribute to this
- Offer a blog for conversation and interaction amongst targeted audiences
- Get feedback form targeted audience

## User Experience

### Target Audience
- Wildlifers Targets animal lovers
- Enviroment activists
- Everyday working people who wants to but do not know how to contribute to the enviroment
- Everyday working people who wants to but do not know how to contribute to distinct animals
- 

### User Reqirements and Expectaions

- Accessible site
- Navigations that are simple and easy to use
- Site contact information
- Social media links
- Fully responsiveness

### User Stories

#### User 
1. As a site user I awnt to see a wild life scheme to site
2. As a user I want to have easy navigation to the site features 
3. As a site user have access to a list of animals of which I can register and help
4. As a site user I want to know how I can contribute
5. As a site user I want to be able to paginate through the list easily
6. As a site user I should have the option of enrolling in a program when I am reading about an 
  animal I like
7. As a site user I want to be able to register an account so I can enroll in a program
8. As a site user I want to be able to view a list of my current enrollments so I can plan for them
9. As a site user I want to be able to updade and change my enrollments
10. As a site user I want to be able to cancel any of my enrollments
11. As a site user I want to see messages when I enter, update or delete data entries  
15. As a site user I want o see a blog list
16. As a site user to want to read blog details
17. As a site user I want to have blog commenting options 
 
#### Returning User
 
 19. As  a return user I want the site to remember me

#### Site Owner 
12. As a site owner I want the user to be able to send us messages/emails through a contact form
13. I want site to be fully responsive  
14. I want user to see data entry vaildation when registering
18. As a owner I want to control commnets posted


### Kanban, Epics & User Stories
- GitHub Kanban was used to track all open user stories
- Epic was created using the milestones feature
- Mistaken all issues were load into one epic instead of seperate page Epics

<details><summary>Epic</summary>

![Epic](docs/testing/epic.JPG)

</details>
<details><summary>User Story</summary>

![User Story](docs/testing/user-story.JPG)

</details>
<details><summary>Kanban</summary>

![Kanban](docs/testing/kanban.JPG)

</details>

## Design


### Colour
 The color of the site was chosen to support the theme which is wild life, trees and animals. The dark navbar and footer helps to contrast the brightness of the colors.

### Fonts
The font was chosen from Google Font but I mostly used simple stanard font 

## Structure

### Website pages
This website was structured with the animal logo which give a wild life characteristic but also with the regular easy to use nav bar, a body of information and the regular footer which give the final characteristics of a funtional webpage.

The site Navbar is a black with a logo to to the lefzt which navigate to te home, links to the site pages on the right witha drop style nav which have links for registration, login and booking. At the bottom of the page there is the footer which contains office location informtion and social links.

- The site is consist of these pages:
 - Home page that contains information and images to share about wild life with 2 nav buttons to register and enroll in program.
 - The program page which display a paginated list of animals the programs represent, the status and option to read more about them 
 - A page to read more about the selected animal with a button to return to the aniaml list and a button to booking form
 - My bookings page if user is looged in shows a paginated list of that users enrollment programs with option buttons to edit or cancel the enrollment 
 - The contact us page display the contact form on which user can send us a message and also contain a map location of our Stockholm office
 - The blog page show a list of site blog post wth the option to view the blog
 - The blog page view show blog post details craeted date and comments, if the suer is logged in a comment for is present to allow suer to leave a comment on the post
 - The registration page displays the registration form for user to access and use site features
 - The login page displays a form to give return user an easier was to log in to sue site features
 - The Enroll page displays a for for users to make a booking with choices or date, time, animal, Jobs,etc. 

### Database

-The backend consists of Python built with the Django framework with a database of a Postgres for the deployed version

<details><summary>Show diagram</summary>
<img src="/docs/testing/database.JPG">
</details>

#### Usermodel
- This contains user information and was config by Django Allauth biult in library

#### Programsmodel
- animal_name(Foriegnkey)
- animal_category(Foriegnkey)
- country
- image
- description

#### Animalmodel
- name

#### Survivalcategorymodel
- category

#### Enrollmodel
- create_date
- start_date
- user
- name
- email
- volunteer_job
- work_time
- animal_name

#### Commentmodel
- post(Foriegnkey)
- name
- email
- body
- created_on
- approved

#### Postlistmodel
- title
- slug
- author(Foriegnkey)
- updated_on
- content
- feature_image
- excerpt
- created_on
- status

### Wireframes


<details><summary>Home</summary>
<img src="/docs/wireframe/browser-wireframe-home.png">
<img src="/docs/wireframe/tablet-wireframe-home.png">
<img src="docs/wireframe/mobile-wireframe-home.png">
</details>
<details><summary>Program</summary>
<img src="/docs/wireframe/browser-wireframe-program.png">
<img src="/docs/wireframe/tablet-wireframe-program.png">
<img src="/docs/wireframe/mobile-wireframe-program.png">
</details>
<details><summary>Program Read</summary>
<img src="/docs/wireframe/browser-wireframe-program-read.png">
<img src="/docs/wireframe/tablet-wireframe-program-read.png">
<img src="/docs/wireframe/mobile-wireframe-program-read.png">
</details>
<details><summary>My Bookings</summary>
<img src="docs/wireframe/browser-wireframe-mybookings.png">
<img src="docs/wireframe/tablet-wireframe.mybooking.png">
<img src="docs/wireframe/mobile-wireframe-mybookings.png">
</details>
<details><summary>Booking Edit</summary>
<img src="docs/wireframe/browser-wireframe-enroll-editing.png">
<img src="docs/wireframe/tablet-wireframe-enroll-editing.png">
<img src="docs/wireframe/mobile-wireframe-enroll-editing.png">
</details>
<details><summary>Contact</summary>
<img src="docs/wireframe/browser-wireframe-contact.png">
<img src="docs/wireframe/tablet-wireframe-contact.png">
<img src="docs/wireframe/mobile-wireframe-contact.png">
</details>
<details><summary>Blog</summary>
<img src="docs/wireframe/browser-wireframe-blog.png">
<img src="docs/wireframe/tablet-wireframe-blog.png">
<img src="docs/wireframe/mobile-wireframe-blog.png">
</details>
<details><summary>Blog Details</summary>
<img src="docs/wireframe/browser-wireframe-blog-display.png">
<img src="docs/wireframe/tablet-wireframe-blog-display.png">
<img src="docs/wireframe/mobile-wireframe-blog-display.png">
</details>
<details><summary>Register</summary>
<img src="docs/wireframe/browser-wireframe-register.png">
<img src="docs/wireframe/tablet-wireframe-register.png">
<img src="docs/wireframe/mobile-wireframe-register.png">
</details>
<details><summary>Login</summary>
<img src="docs/wireframe/browser-wireframe-login.png">
<img src="docs/wireframe/tablet-wireframe-login.png">
<img src="docs/wireframe/mobile-wireframe-login.png">
</details>
<details><summary>Logout</summary>
<img src="docs/wireframe/browser-wireframe-logout.png">
<img src="docs/wireframe/tablet-wireframe.logout.png">
<img src="docs/wireframe/mobile-wireframe-logout.png">
</details>
<details><summary>Enroll</summary>
<img src="docs/wireframe/browser-wireframe-enroll.png">
<img src="docs/wireframe/tablet-wireframe-enroll.png">
<img src="docs/wireframe/mobile-wireframe-enroll.png">
</details>


## Technologies Used

### Languages

- HTML
- CSS
- Javascript
- Python
- Django

### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [Pycodestyle(PEP8)](https://pypi.org/project/pycodestyle/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)


## Features

### Logo and Navigation Bar
- Site Logo supports the wild life theme of the site and navigates to home page 
- The navbar is consist of the logo and the links to all the site feature
- The navbar is present on all pages
- The navbar also have a drop down features login, register and booking

<details><summary>See feature images</summary>

![logo-and-nav](docs/feature/feature-navbar.JPG)
![logo-and-nav](docs/feature/feature-nav-dropdown.JPG)

</details>

### Home page
- The home page is consist og images and descriptions relating to wildlife 
- The home page is also consist of a button to navigate to register and a button enroll

<details><summary>See feature images</summary>

![home](docs/feature/feature-home-page.png) 

</details>

### Footer
- The footer is consist of social media link
- The footer also have office location and contact information 
- the footer is displayed at the bottom of the page

<details><summary>See feature images</summary>

![footer](docs/feature/feature-footer.JPG)
</details>

### Sign up/Register
- The registration page is consist of a form to enter user details
- It prupose is for new users to access more site features
- The form also instructions on how to register


<details><summary>See feature images</summary>

![signup/register](docs/feature/feature-registration.png)
</details>

### Login
- Easy for return users to get in
- Fields are mandatory

<details><summary>See feature images</summary>

![login](docs/feature/feature-login-required.JPG)
</details>

### Logout
- User can log out before leaving the site

<details><summary>See feature images</summary>

![logout](docs/feature/feature-logout.JPG)

</details>

### Program
- Information on what the program stands for
- Aniaml cards of feature animals with images aand animal status
- paginated for easy navogation
- Read button to get more details on the animal
- Programs can be added, edited and deleted by the staff/organization
- Fully responsive

<details><summary>See feature images</summary>

![program](docs/feature/feature-program-page.JPG)
</details>


### Read program
- Here you find a more detailed information about the animal chosen
- There is a list on what you vcan do to help this animal
- There is a button to return to the list
- There is a button to go to enroolment form

<details><summary>See feature images</summary>

![read-program](docs/feature/feature-animal-details.png)

</details>

### User enrollment list
- Must be registered or logged in to see 
- Paginated list of user enrollment
- Each card are consist of a edit and cancel button

<details><summary>See feature images</summary>

![enrollment-list](docs/feature/feature-mybookings.png)
</details>

### Enrollment editing
- Here is the enrollment form displaying the fields fill with the current booking and ready to be changed
- Submit and update message will be seen  

<details><summary>See feature images</summary>

![enrollment-editing](docs/feature/feature-edit-enrollment.png)

</details>

### Cancel enrollment
- Here the canceling confirmation card is diaplayed
- The card have a button to return if user change their minds and a button tp cancel
- A confirmation message will be dispalyed when the canalation is completed

<details><summary>See feature images</summary>

![cancel-enrollment](docs/feature/feature-cancel-enrollment.JPG)

</details>

### Contact page
- User can contact us by filling out this form
- User must enter their names and email and the message in the text field
- Message will display when the form is submitted
- Google map address is present for our office location

<details><summary>See feature images</summary>

![contact-page](docs/feature/feature-contact-us.png)
</details>

### Blog
- Fully responsive
- Display blog posts made by staff/organisation
- Blog post are paginated
- Click on the post to read the post details

<details><summary>See feature images</summary>

![blog](docs/feature/feature-blog-page.JPG)
</details>


### Blog details
- Blog details show more detials about the blog
- The featured image is displayed

<details><summary>See feature images</summary>

![blog-details](docs/feature/feature-blog-detailse.png)
</details>

### Blog commenting
- only registered or logged in User get the option to leave comment
- Comment cand be done in the text field but needs to be approved
- When commented are made the submitted the comment awiting approval message is displayed 
- Comments are approved by staff/organisation for monitering purposes

<details><summary>See feature images</summary>

![program](docs/feature/feature-blog-detailse.png)
</details>


### Booking
- Here the is the bookig form to enter your name and the aniaml, job. time and date User want to do their program
- Only registered or looged on user are allow to enroll in a program
- The form is made easier by displaying the list of Jobs, work times, animals and date picker
- There are also a descriptive list of the offered Jobs

<details><summary>See feature images</summary>

![program](docs/feature/feature-booking-form.png)
</details>


## Validation

### HTML Validation
- The W3C Markup Validation Service was used to validate the HTML of the website.

<details><summary>Home</summary>
<img src="/docs/validation/html-home-page.JPG">
</details>
<details><summary>Program</summary>
<img src="/docs/validation/html-program-page-validation.JPG">
</details>
<details><summary>Program details</summary>
<img src="/docs/validation/html-program-view-page-validation.JPG">
</details>
<details><summary>My Booking</summary>
<img src="/docs/validation/html-mybooking-page-validation.JPG">
</details>
<details><summary>Booking Edit</summary>
<img src="/docs/validation/html-booking-edit-page-validation.JPG">
</details>
</details>
<details><summary>Contact Us</summary>
<img src="/docs/validation/html-contact-page-validation.JPG">
</details>
<details><summary>Blog</summary>
<img src="/docs/validation/html-blog-page-validation.JPG">
</details>
<details><summary>Blog details</summary>
<img src="docs/validation/html-blog-detail-page-validation.JPG">
</details>
<details><summary>Register</summary>
<img src="docs/validation/html-register-page-validation.JPG">
</details>
<details><summary>Login</summary>
<img src="docs/validation/html-login-page-validation.JPG">
</details>
<details><summary>Logout</summary>
<img src="docs/validation/html-logout-page-validation.JPG">
</details>
<details><summary>Enroll</summary>
<img src="docs/validation/html-enroll-validation.JPG">
</details>
<details><summary>403, 404, 500</summary>
<img src="">
</details>

### CSS Validation
- The W3C Jigsaw service was used for CSS Validation. 

<details><summary>style.css</summary>
<img src="/docs/validation/css-validation.JPG">
</details>

### JavaSript Validation

- The JSHint JS Validation Service was used to validate the Javascript.

<details><summary>script.js</summary>
<img src="/docs/validation/javascript-validation.JPG">
</details>

### Pep8 Validation

- PEP8 Validation Service was used to check the code for PEP8 requirements. 

#### Homeapp

<details><summary>tests.py</summary>
<img src="">
</details>
<details><summary>urls.py</summary>
<img src="/docs/validation/pyth-home-url-validation.JPG">
</details>
<details><summary>view.py</summary>
<img src="/docs/validation/pyth-home-view-validation.JPG">
</details>

#### Programsapp

<details><summary>admin.py</summary>
<img src="/docs/validation/pyth-program-admin-validation.JPG">
</details>
<details><summary>forms.py</summary>
<img src="">
</details>
<details><summary>models.py</summary>
<img src="/docs/features/wireframes/validations/signuphtml-validation.JPG">
</details>
<details><summary>tests.py</summary>
<img src="">
</details>
<details><summary>urls.py</summary>
<img src="/docs/validation/pyth-program-url-validation.JPG">
</details>
<details><summary>view.py</summary>
<img src="/docs/validation/pyth-program-view-validation.JPG">
</details>

#### Bookingapp

<details><summary>admin.py</summary>
<img src="/docs/validation/pyth-booking-admin-validation.JPG">
</details>
<details><summary>forms.py</summary>
<img src="/docs/validation/pyth-booking-form-validation.JPG">
</details>
<details><summary>models.py</summary>
<img src="/docs/validation/pyth-booking-model-validation.JPG">
</details>
<details><summary>tests.py</summary>
<img src="">
</details>
<details><summary>urls.py</summary>
<img src="/docs/validation/pyth-booking-url-validation.JPG">
</details>
<details><summary>view.py</summary>
<img src="/docs/validation/pyth-booking-view-validation.JPG">
</details>

#### Blog app

<details><summary>admin.py</summary>
<img src="/docs/validation/pyth-blog-admin-validation.JPG">
</details>
<details><summary>forms.py</summary>
<img src="/docs/validation/pyth-blog-form-validation.JPG">
</details>
<details><summary>models.py</summary>
<img src="/docs/validation/pyth-blog-model-validation.JPG">
</details>
<details><summary>tests.py</summary>
<img src="">
</details>
<details><summary>urls.py</summary>
<img src="/docs/validation/pyth-blog-url-validation.JPG">
</details>
<details><summary>view.py</summary>
<img src="/docs/validation/pyth-blog-view-validation.JPG">
</details>

### Chrome ligthouse tool

- Lighthouse was used to test the performance, accessibility, best practice and SEO of the site.

#### Mobile
<details><summary>View results</summary>

Page  | Performance (%) | Accessibility (%) | Best Practices (%) | SEO (%)
------------  | ------------ | ------------- | ------------- | -------------
home/templates/home/index.html | 91 | 100 | 92 | 100 |
home/templates/home/contact.html | 93 | 97 | 100 | 100 |
programs/templates/programs/programs.html | 98 | 100 | 100 | 100 |
programs/templates/programs/programs_list.html | 92 | 97 | 92 | 100 |
booking/templates/booking/bookings.html | 94 | 97 | 100 | 100 |
booking/templates/booking/enrollment_list.html | 97 | 98 | 100 | 100 |
booking/templates/booking/enrollment_editing.html | 94 | 98 | 92 | 100 |
booking/templates/booking/enrollment_delete.html | 98 | 93 | 100 | 100 |
blog/templates/blog/blog_list.html | 87 | 98 | 83 | 100 |
blog/templates/blog/blog_story.html | 87 | 98 | 83 | 100 |
templates/account/login.html | 98 | 100 | 92 | 100 |
templates/account/logout.html | 99 | 100 | 92 | 100 |
templates/account/signup.html | 99 | 100 | 92 | 100 |

</details>

#### Desktop
<details><summary>View results</summary>

Page  | Performance (%) | Accessibility (%) | Best Practices (%) | SEO (%)
------------  | ------------ | ------------- | ------------- | -------------
home/templates/home/index.html | 99 | 100 | 92 | 100 |
home/templates/home/contact.html | 100 | 100 | 92 | 100 |
programs/templates/programs/programs.html | 100 | 100 | 92 | 100 |
programs/templates/programs/programs_list.html | 99 | 96 | 92 | 100 |
booking/templates/booking/bookings.html | 100 | 100 | 92 | 100 |
booking/templates/booking/enrollment_list.html | 100 | 93 | 92 | 100 |
booking/templates/booking/enrollment_editing.html | 100 | 93 | 92 | 100 |
booking/templates/booking/enrollment_delete.html | 100 | 93 | 92 | 100 |
blog/templates/blog/blog_list.html | 87 | 98 | 83 | 100 |
blog/templates/blog/blog_story.html |  | 98 | 92 | 100 |
templates/account/login.html | 100 | 100 | 92 | 90 |
templates/account/logout.html | 100 | 100 | 92 | 100 |
templates/account/signup.html | 100 | 100 | 92 | 100 |
</details>


### Waves
- The WAVE WebAIM web accessibility evaluation tool was used to test the websites accessibility.
- Wave accessibilty issues with heroku connection cause some page not to be tested
#### Desktop

<details><summary>Home</summary>
<img src="docs/validation/wave-home-validation.JPG">
</details>
<details><summary>Program</summary>
<img src="docs/validation/waves-program-page-validation.JPG">
</details>
<details><summary>Contact Us</summary>
<img src="docs/validation/waves-contact-page-validation.JPG">
</details>
<details><summary>Blog</summary>
<img src="docs/validation/wave-blog-page-validation.JPG">
</details>
<details><summary>Blog details</summary>
<img src="">
</details>
<details><summary>Register</summary>
<img src="docs/validation/wave-register-page-validation.JPG">
</details>
<details><summary>Login</summary>
<img src="docs/validation/wave-logout-page-validation.JPG">
</details>
<details><summary>Logout</summary>
<img src="docs/validation/wave-logout-page-validation.JPG">
</details>
<details><summary>Enroll</summary>
<img src="docs/validation/wave-enroll-page-validation.JPG">
</details>


### Performing tests on various devices 

- HP EllitBook
- Amazon fire table 7
- Samsung galaxy 20

### Browser compatability

- Tested on Goole Chrome
- Tested Micrsoft Edge
- Tested on Morzilla Firefox

## Testing

- The was done as follows:
1. Mannual testing
2. Automative testing

1. As a site user I awnt to see a wild life scheme to site

   | **Step** | **Expected result** | **Actual Result** |
   |-------------|------------|---------------------|
   | Visit page:https://wildlifers.herokuapp.com/| Home page tells about the wht the site represent with photos to match | Work as Expected | 

   <details><summary>Screenshots</summary>
   <img src="docs/feature/feature-home-page.png">
   </details>

2. As a user I want to have easy navigation to the site features 

   | **Step** | **Expected result** | **Actual Result** |
   |-------------|------------|---------------------|
   | Click on 'Home' on navigation bar | Home page will load | Work as expected |
   | Click on 'Programs' on navigation bar | Programs page will load |  Work as expected |
   | Click on 'Enroll' on navigation bar | Enroll page/login will load if logged in |  Work as expected |
   | Click on 'Blog' on navigation bar | Blog page will load |  Work as expected |
   | Click on 'Get Registered' on navigation bar select 'Register' | Register page will load |  Work as expected |
   | Click on 'Get Registered' on navigation bar select 'Contact'| Contact page will load |  Work as expected |
   | Click on 'Get Registered' on navigation bar select 'My Bookings' | 'Must be logged in message'/Enrollment list will load  |  Work as expected |
   | Click on 'Logout' on navigation bar | Logout page will load |  Work as expected | 

     <details><summary>Screenshots</summary>
     <img src="docs/testing/test-navbar-home-page.JPG">
     <img src="docs/testing/test-navbar-program-page.JPG">
     <img src="docs/testing/test-navbar-enroll-page.JPG">
     <img src="docs/testing/test-navbar-blog-page.JPG">
     <img src="docs/testing/test-navbar-register.JPG">
     <img src="docs/testing/test-navbar-contact-page.JPG">
     <img src="docs/testing/tets-mybookings-page.JPG">
     <img src="docs/testing/test-navbar-logout-page.JPG">
     </details>

3. As a site user have access to a list of animals of which I can register and help

   | **Step** | **Expected Result** | **Actual Result** |
   |------------|---------------------|-------------------|
   | Navigate to program page  | List of imaged animal cards are visible  | Works as expected |
   | Go through paginated list | Cards are paginated by 4 on different pages | Works as expected |
   | Click read on card | aniaml detail will display with option to enroll or go back to list | Works as expected |
  
    <details><summary>Screenshots</summary>
    <img src="docs/testing/test-navbar-program-page.JPG">
    <img src="docs/testing/test-story-animal-list.JPG">
    <img src="docs/testing/test-story-animal-detail.JPG">
    </details>

4.  As a site user I want to know how I can contribute 

   | **Step** | **Expected Result** | **Actual Result** |
   |------------|---------------------|-------------------|
   | Go to profram page | Description on how to contribute is visible | Works as expected |

    <details><summary>Screenshots</summary>
    <img src="docs/testing/test-story-program-text.jpg">
    <img src="docs/testing/test-story-job-list.png">
    </details>

5. As a site user I want to be able to paginate through the list easily
   | **Step** | **Expected Result** | **Actual Result** |
   |------------|---------------------|-------------------|
   | Go to the bottom of any list | pagaination nav present | Works as expected |
   | Clic on arrow | the next page of list will display | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/testing/test-story-pagination.png">
    <img src="docs/testing/test-story-pagination1.png">
    <img src="docs/testing/test-story-pagination2.png">
    </details>

6. As a site user I should have the option of enrolling in a program when I am reading about an 
    animal I like   
    
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-----------------|
    | Select animal card | animal description page present with an enroll button to the bottom | 
    Works as expected |
    | Select Enroll on Navbar | Enroll page will be present | Works as expected |
     
    <details><summary>Screenshots</summary>
      <img src="docs/testing/test-story-animal-detail.JPG">
    </details>

7. As a site user I want to be able to register an account so I can enroll in a program

   | **Step** | **Expected Result** | **Actual Result** |
   |------------|---------------------|-------------------|
   | Go to Get registered click register | Registration page will be displayed | Works as expected |

  <details><summary>Screenshots</summary>
     <img src="docs/testing/test-navbar-register.JPG">
     <img src="docs/testing/test-navbar-enroll-page.JPG">
  </details>

8.  As a site user I want to be able to view a list of my current enrollments so I can plan for 
    them 

   | **Step** | **Expected Result** | **Actual Result** |
   |------------|---------------------|-------------------|
   | Got to 'Get Registered' click on 'My Bookings' | A list of User'e booking will display | Works as expected |
  <details><summary>Screenshots</summary>
    <img src="docs/feature/feature-mybookings.png">
     <img src="docs/feature/feature-mybookings.png">
   </details>


9. As a site user I want to be able to update and change my enrollments

   | **Step** | **Expected Result** | **Actual Result** |
   |------------|---------------------|-------------------|
   | Got to 'Get Registered' click on 'My Bookings' | A list of User'e booking will display, Bookings in list will have editing button | Works as expected |
   | Click 'Edit button' | Edit form will display with this enrollment information ready to be changed | Works as expected |
   | Click submit | Enrollment wil be updated with upkdate confirmation message present | Works as expected |
  <details><summary>Screenshots</summary>
    <img src="docs/testing/test-story-enrollment-editing.png">
    <img src="docs/testing/test-edit-enrollment1.png">
    <img src="docs/testing/test-story-edit-message1.jpg">
  </details>

10. As a site user I want to be able to cancel any of my enrollments

    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-------------------|
    | Got to 'Get Registered' click on 'My Bookings' | A list of User'e booking will display, Bookings in list will have editing button | Works as expected |
    | Click 'Delete button' | delete confirmation modal will display | Works as expected |
    | Click Delete | Enrollment will delete and a enrollment delete message will display | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/testing/test-navbar-register.JPG">
    <img src="docs/testing/tets-mybookings-page.JPG">
    <img src="docs/testing/test-story-enrollment-delete.png">
    <img src="docs/feature/feature-cancel-enrollment.JPG">
    <img src="docs/testing/test-story-delete-message.jpg">
    </details>

11.  As a site user I want to get messages when I enter, update or delete data entries

   | **Step** | **Expected Result** | **Actual Result** |
   |------------|---------------------|-------------------|
   | Submit Loginform | Logged in message will display | Works as expected |
   | Submit update form | Updated message will display | Works as expected |
   | Sumit logout| Logged out message will display | Works as expected |
   | Submit delete Enrollment | Deleted message will display | Works as expected |
   | Submit Enrollmet | Enrolled message will display | Works as expected |

  <details><summary>Screenshots</summary>
    <img src="docs/testing/test-story-login-message.JPG">
    <img src="docs/testing/test-story-logout-message.JPG">
    <img src="docs/testing/test-story-edit-message1.jpg">
    <img src="docs/testing/test-story-delete-message.jpg">
    <img src="docs/testing/test-story-enrollment-message.JPG">
  </details>

12.  As a site owner I want the user to be able to send us messages/emails through a contact form
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-----------------|
    |  Got to 'Get Registered' click on 'Contact' | Contact form will be displayed with message field | Works as expected |
    
    <details><summary>Screenshots</summary>
    <img src="docs/testing/test-navbar-contact-page.JPG">
    </details>

13. I want my site to be fully responsive

    |**Step** | **Expected Result** | **Actual Result**
    |------------ | ------------ | ------------ |
    |Change device screen size using chrome dev tools | The web functionality remains the same on various screen sizes | Works as expected |

    <details><summary>Screenshot</summary>
    <img src="docs/testing/test-story-response-tablet.png">
    <img src="docs/testing/test-story-responsive-mobile.png">
    </details>


14. As a site owner want user to see data entry vaildation when registering
    |**Step** | **Expected Result** | **Actual Result**
    |------------ | ------------ | ------------ |
    |Click on the 'Log in' on the nav bar and 'Register' from the drop-down menu | Displays Registration page | Works as expected |
    |Input username shorter than 4 characters (eg. xyz) | Prevents registration. Shows warning message to lenghten username text  | Works as expected |
    |Input username which has already been taken (eg. Admin) | Prevents registration. Displays 'A user with that username already exists.' message | Works as expected |
    |Input incorrect format of email | Shows warning message to include '@' in the email. Prevents registration | Works as expected |
    |Input 'newuser12' password |  Prevents registration. Displays 'The password is too similar to the username' message | Works as expected |
    |Input '12345678' as a password | Prevents registration. Displays 'This password is entirely numeric' message | Works as expected |
    |Input 'testing' as a password | Prevents registration. Displays 'This password is too short. It must contain at least 8 characters' message | Works as expected |
    |Input two different values in 'Password' and 'Password (again)' fields | Prevents registration. Displays 'You must type the same password each time.' message | Works as expected |

    <details><summary>Screenshots</summary>
    <img src="docs/testing/test-story-common-pass.png">
    <img src="docs/testing/test-story-register-email.png">
    <img src="docs/testing/test-story-register-pass-characters.png">
    <img src="docs/testing/test-story-register-pass-sim.png">
    <img src="docs/testing/test-story-register-same-pass.png">
    <img src="docs/testing/test-story-registration-input validation.png">
    <img src="docs/testing/test-story-user-exist.png">
    </details>

15. As a site user I want to see a blog list
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-------------------|
    | Go to blog on navbar | A list of blog post will display | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/testing/test-story-pagination2.png">
    </details>

16. As a site user to want to read blog details
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-------------------|
    | Click on a blog image in blog list | Blog details will display | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/feature/feature-blog-detailse.png">
    </details>

17. As a site user I want to have blog commenting options 
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-------------------|
    | Login, click on blog post | Comment form will display for commenting | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/feature/feature-login-required.JPG">
    <img src="docs/testing/test-story-login-message.JPG">
    <img src="docs/testing/test-story- blog commenting.png">
    </details>

18. As a owner I want to control commnets posted
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-------------------|
    | User submit Comment  | Comment waiting approval message is displayed | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/testing/test-story-blog-commenting-approve.jpg">
    </details>

19. As  a return user I want the site to remember me 
    | **Step** | **Expected Result** | **Actual Result** |
    |------------|---------------------|-------------------|
    | Comment  | 2 | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/feature/feature-login-required.JPG">
    <img src="docs/testing/test-story-login-message.JPG">
    </details>

## Design



## Bugs
  List of bugs found and fixes used ti mitigate them.

- Bug: the data in the database no longer fit the new schema due to model changes
  Fix: performed data dump reset datebase in SQL app, restored data and run migrations
- Bug: Django collectstatic -input, static file was not updating causing deployment fail error
  Fix: performed python manage.py collectstatic in terminal which resolve issue
- Bug: blog post slug:slug url path was missingthe end '/' causing program page and admin pages 
    404 error
    Fix: Correct typo and confirm this issue was mitgated
- Bug: html validation for index.hmtl warnings for lack of heading h1-h6 in section tags
  Fix: removed unneccesary section tags
- Bug: Some stary divs were found during html validation
   Fix: removed div and confirm alidatio to be good
- Bug: Wave error for color contrast on site buttons 
  Fix: change to a darker green  to mitigate issue.
- Bug: Wave error for color conflicting contrast with commenting text-mute on the blog page
  Fix: Remove text-mute
- Bug: loading performance on the form page was low due to background image loading time
  Fix: removed background image


## Configuration

### Google emails

To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required:

1. Create an email account at google.com, login, click you user icon and then on 'Manage Your Google Account'
2. Click on the Security tab
3. Turn on 2-step verification and follow the steps to enable
4. Click on App passwords, click on Select app and choose Other
5. Give your app a name and click on 'Generate'
  <br>![App password]()
6. A 16 digit password will be generated, note the password down
7. Set the below variables within the settings.py file to successfully send emails
  <br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
  <br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
  <br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
  <br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')</code>
  <br><code>EMAIL_PORT = '587'</code>
  <br><code>EMAIL_USE_TLS = True</code>
8. Set up the variables EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in your Render application Config vars


## Deployment

### Heroku
This application has been deployed from GitHub to Heroku by following the steps:

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
   
### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

[Back to Table Of Contents](#table-of-content)


### Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
    <details>
    <img src="docs/heroku/heroku-create-app.JPG">
    </details>

2. Create an app, give it a name similar to project name, and select a region
  <details>
  <img src="docs/heroku/heroku-overview.JPG">
  </details>

3. Under resources search for postgres, and add a Postgres database to the app


4. Create and ElephantSqul account and set up a plan with in your region
   <details>
   <img src="docs/heroku/sql.JPG">
   </details>

5. Copy Url database instance from Sql account and store it in the env.py enviroment variable (os.environ["DATABASE_URL"]="<copiedURL>")

6. Add a your secret key to env.py enviroment variable os.environ["SECRET_KEY"]="my_super^secret@key"

7. Import env.py to settings.py  add Data base and sercert key variable to settings.py file

8. Add localhost, and wildlifers.herokuapp.com to the ALLOWED_HOSTS variable in settings.py
    <details>
    <img src="docs/heroku/debug-false.JPG">
    </details>
9. Migrate change to manage.py

10. Add Secret key and Database url to Heroku Config vars

11. Add PORT 8000 to config vars to avoid deployment failure

12. Set DEBUG value to False
   <details>
   <img src="docs/heroku/debug-false.JPG">
   </details>

13. Set X_FRAME_OPTION ='SAMEORIGIN'

14.  Run pip3 freeze > requirements.txt so that file are updated before deployment

15. Run "python3 manage.py showmigrations" to check the status of the migrations

16. Run "python3 manage.py migrate" to migrate the database

17. Check config vars for DISABLE_COLLECTSTATIC=1 is removed

18. Go to deploy in the Heroku app
    <details>
    <img src="docs/heroku/heroku-deploy.JPG">
    </details>

19. Clik Deploy 

20. View build logs for error
     <details>
     <img src="docs/heroku/heroku-build-log.JPG">
     </details>

21. Click app to view website


## Credits

### Media

Media images were referenced from <a href="https://www.pexels.com/">Pexels</a> , <a href="https://unsplash.com/">Upsplash</a> and <a href="http://www.freepik.com/">Freepik</a>. 

- [404-background](assets/images/404er.jpeg): <a href=" https://www.pexels.com/photo/an-apple-and-a-dumbbell-on-a-clipboard-8154260/" >Pexels</a>
  Photo by:  <a href="https://www.pexels.com/@alesiakozik/">Alesia Kozik</a>
- [signup-page-background](assets/images/signupimage.jpeg): <a href="https://www.pexels.com/photo/          personal-male-trainer-with-overweight-female-client-in-fitness-center-6455927/">Pexels</a>
  Photo by:  <a href="https://www.pexels.com/@julia-larson/">Julian Larson</a>
- [hero-image](assets/images/heroimage.jpg): <a href="https://www.freepik.com/premium-photo/sport-couple-doing-plank-exercise-workout-fitness-centrum-man-woman-practicing-plank-gym_17801349.htm">Freepik</a>
  Photo by: <a href= "https://www.freepik.com/author/weyo">Weyo</a>
- [crossfit-image](assets/images/crossfitsmall.jpg): <a href="https://unsplash.com/photos/h3D-RRvxfqE">Unsplash</a>
  Photo by: <a href="https://unsplash.com/@bastien_plu">Bastien Plu</a>
- [trainer-image](assets/images/trainer.jpeg): <a href="https://www.pexels.com/photo/ethnic-woman-exercising-with-battling-ropes-near-male-trainer-6455771/">Pexels</a>
  photo by: <a href= "https://www.pexels.com/@julia-larson/">Julian Larson</a>


### Code
 


## Acknowledgements
- Tanks and acknowlegement goes to my mentor Mo Shami great guidance.
- Acknowledge my brother Addan Mc Collin for support form a user's veiw
- Thanks to my girlfriend Hiba Salem for support and input on a user veiw
- Thankful to the Slack team for tips