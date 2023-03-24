# Good Life Gym
(Developer: Ewart Hestick)

![Mockup image]()

[Live webpage]()


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
4. As a site user I want to read about these animals and their status of extinction
5. As a site user I want to be able to paginate through the list easily
6. As a site user I should have the option of enrolling in a program when I am reading about an 
  animal I like
7. As a site user I want to be able to register an account so I can enroll in a program
8. As a site user I want my registration information t be saved so that I only need to log in when I return
9. As a site user I want to be able to view a list of my current enrollments so I can plan for them
10. As a site user I want to be able to upade and change my enrollments
11. As a site user I want to be able to cancel any of my enrollments
12. As a site user I want to see messages when I enter, update or delete data entries   
 
#### Returning User
 
 5. As  a return user I want the site to remember me

#### Site Owner 
13. As a site owner I want the user to be able to send us messages/emails through a contact form
14. As a site owner I want user to get messages when register, login , logout, enroll  
  in a program, edit enrollment, delete enroolment or send us messages through the contact form.
15. As a site owner I want user to have confirmantion action before canceling enrollments
16. T want user to see data entry vaildation when registering
17. I want site to be fully responsive  

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

-

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
<img src="">
<img src="">
<img src="">
</details>
<details><summary>Program</summary>
<img src="">
<img src="/docs/features/wireframes/wireframeaboutuspagepad.png">
<img src="">
</details>
<details><summary>Program Read</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>My Bookings</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>Booking Edit</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>Booking Cancel</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>Contact</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>Blog</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>Blog Details</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>Register</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>Login</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>Logout</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>Enroll</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>403</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>500</summary>
<img src="">
<img src="">
<img src="">
</details>
<details><summary>404 page</summary>
<img src="docs/features/wireframes/wireframe404.png">
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
- The navbar switch to hamburger menu when use on smaller screens
- Fully responsive

![logo-and-nav]()

### Home page
- The home page is consist og images and descriptions relating to wildlife 
- The home page is also consist of a button to navigate to register and a button enroll
- Fully responsive


![heros](docs/features/heros.PNG) 

### Footer
- The footer is consist of social media link
- The footer also have office location and contact information 
- the footer is displayed at the bottom of the page
- Fully responsive

![gym-features](docs/features/feature.PNG)

### Sign up/Register
- The registration page is consist of a form to enter user details
- It prupose is for new users to access more site features
- The form also instructions on how to register
- registered message will be seen
- Fully responsive
![easy-nav](docs/features/easynav.PNG)

### Login
- Easy for return users to get in
- Fields are mandatory
- Logged in messsage will be seen
- Fully responsive

![opem-times](docs/features/opentimes.PNG)

### Logout
- User can log out before leaving the site
- Logged out message will be seen
- Fully responsive

![interior-teaser](docs/features/teaser.PNG)

### Program
- Information on what the program stands for
- Aniaml cards of feature animals with images aand animal status
- paginated for easy navogation
- Read button to get more details on the animal
- Programs can be added, edited and deleted by the staff/organization
- Fully responsive

![map](docs/features/map4.PNG)

### Read program
- Here you find a more detailed information about the animal chosen
- There is a list on what you vcan do to help this animal
- There is a button to return to the list
- There is a button to go to enroolment form
- Fully responsive


![footer](docs/features/footer.PNG)

### User enrollment list
- Must be registered or logged in to see 
- Paginated list of user enrollment
- Each card are consist of a edit and cancel button
- Fully responsive

![about-us](docs/features/aboutus.PNG)

### Enrollment editing
- Here is the enrollment form displaying the fields fill with the current booking and ready to be changed
- Submit and update message will be seen  
- Fully responsive

![membership-cards](docs/features/membership.PNG)

### Cancel enrollment
- Here the canceling confirmation card is diaplayed
- The card have a button to return if user change their minds and a button tp cancel
- A confirmation message will be dispalyed when the canalation is completed
- Fully responsive

![signup-form](docs/features/signupform.PNG)

### Contact page
- User can contact us by filling out this form
- User must enter their names and email and the message in the text field
- Message will display when the form is submitted
- Google map address is present for our office location
- Fully responsive

![404-page](docs/features/test-user-story/404page.PNG)

### Blog
- Fully responsive
- Display blog posts made by staff/organisation
- Blog post are paginated
- Click on the post to read the post details

### Blog details
- Blog details show more detials about the blog
- The featured image is displayed
- Fully responsive

### Blog commenting
- only registered or logged in User get the option to leave comment
- Comment cand be done in the text field but needs to be approved
- When commented are made the submitted the comment awiting approval message is displayed 
- Comments are approved by staff/organisation for monitering purposes
- Fully responsive 

### Booking
- Here the is the bookig form to enter your name and the aniaml, job. time and date User want to do their program
- Only registered or looged on user are allow to enroll in a program
- The form is made easier by displaying the list of Jobs, work times, animals and date picker
- There are also a descriptive list of the offered Jobs
- A con firmation messagge will display after for is submited
- Only registered or logged in User get the option to leave comment
- Comment cand be done in the text field but needs to be approved
- Fully responsive 


## Validation

### HTML Validation
- The W3C Markup Validation Service was used to validate the HTML of the website.

<details><summary>Home</summary>
<img src="">
</details>
<details><summary>Program</summary>
<img src="">
</details>
<details><summary>Program details</summary>
<img src="/docs/features/wireframes/validations/signuphtml-validation.JPG">
</details>
<details><summary>My Booking</summary>
<img src="">
</details>
<details><summary>Booking Edit</summary>
<img src="">
</details>
<details><summary>Booking Cancel</summary>
<img src="">
</details>
<details><summary>Contact Us</summary>
<img src="">
</details>
<details><summary>Blog</summary>
<img src="">
</details>
<details><summary>Blog details</summary>
<img src="">
</details>
<details><summary>Register</summary>
<img src="">
</details>
<details><summary>Login</summary>
<img src="">
</details>
<details><summary>Logout</summary>
<img src="">
</details>
<details><summary>Enroll</summary>
<img src="">
</details>
<details><summary>403, 404, 500</summary>
<img src="">
</details>

### CSS Validation
- The W3C Jigsaw service was used for CSS Validation. 

<details><summary>style.css</summary>
<img src="">
</details>

### JavaSript Validation

- The JSHint JS Validation Service was used to validate the Javascript.

<details><summary>script.js</summary>
<img src="">
</details>

### Pep8 Validation

- PEP8 Validation Service was used to check the code for PEP8 requirements. 

#### Homeapp

<details><summary>admin.py</summary>
<img src="">
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
<img src="">
</details>
<details><summary>view.py</summary>
<img src="">
</details>

#### Programsapp

<details><summary>admin.py</summary>
<img src="">
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
<img src="">
</details>
<details><summary>view.py</summary>
<img src="">
</details>

#### Bookingapp

<details><summary>admin.py</summary>
<img src="">
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
<img src="">
</details>
<details><summary>view.py</summary>
<img src="">
</details>

#### Blogapp

<details><summary>admin.py</summary>
<img src="">
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
<img src="">
</details>
<details><summary>view.py</summary>
<img src="">
</details>

### Chrome ligthouse tool

- Lighthouse was used to test the performance, accessibility, best practice and SEO of the site.

<details><summary>Home</summary>
<img src="">
</details>
<details><summary>Program</summary>
<img src="">
</details>
<details><summary>Program details</summary>
<img src="/docs/features/wireframes/validations/signuphtml-validation.JPG">
</details>
<details><summary>My Booking</summary>
<img src="">
</details>
<details><summary>Booking Edit</summary>
<img src="">
</details>
<details><summary>Booking Cancel</summary>
<img src="">
</details>
<details><summary>Contact Us</summary>
<img src="">
</details>
<details><summary>Blog</summary>
<img src="">
</details>
<details><summary>Blog details</summary>
<img src="">
</details>
<details><summary>Register</summary>
<img src="">
</details>
<details><summary>Login</summary>
<img src="">
</details>
<details><summary>Logout</summary>
<img src="">
</details>
<details><summary>Enroll</summary>
<img src="">
</details>
<details><summary>403, 404, 500</summary>
<img src="">
</details>

### Waves
- The WAVE WebAIM web accessibility evaluation tool was used to test the websites accessibility.

#### Desktop

<details><summary>Home</summary>
<img src="">
</details>
<details><summary>Program</summary>
<img src="">
</details>
<details><summary>Program details</summary>
<img src="/docs/features/wireframes/validations/signuphtml-validation.JPG">
</details>
<details><summary>My Booking</summary>
<img src="">
</details>
<details><summary>Booking Edit</summary>
<img src="">
</details>
<details><summary>Booking Cancel</summary>
<img src="">
</details>
<details><summary>Contact Us</summary>
<img src="">
</details>
<details><summary>Blog</summary>
<img src="">
</details>
<details><summary>Blog details</summary>
<img src="">
</details>
<details><summary>Register</summary>
<img src="">
</details>
<details><summary>Login</summary>
<img src="">
</details>
<details><summary>Logout</summary>
<img src="">
</details>
<details><summary>Enroll</summary>
<img src="">
</details>
<details><summary>403, 404, 500</summary>
<img src="">
</details>

#### Mobile

<details><summary>Home</summary>
<img src="">
</details>
<details><summary>Program</summary>
<img src="">
</details>
<details><summary>Program details</summary>
<img src="/docs/features/wireframes/validations/signuphtml-validation.JPG">
</details>
<details><summary>My Booking</summary>
<img src="">
</details>
<details><summary>Booking Edit</summary>
<img src="">
</details>
<details><summary>Booking Cancel</summary>
<img src="">
</details>
<details><summary>Contact Us</summary>
<img src="">
</details>
<details><summary>Blog</summary>
<img src="">
</details>
<details><summary>Blog details</summary>
<img src="">
</details>
<details><summary>Register</summary>
<img src="">
</details>
<details><summary>Login</summary>
<img src="">
</details>
<details><summary>Logout</summary>
<img src="">
</details>
<details><summary>Enroll</summary>
<img src="">
</details>
<details><summary>403, 404, 500</summary>
<img src="">
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

1. As  a first time user I expect a bright feel energetic gym feel

   | **Step** | **Expected result** | **Actual Result** |
   |-------------|------------|---------------------|
   | 1 | 2 | 3 | 

   <details><summary>Screenshots</summary>
   <img src="docs/features/brightenergy.PNG">
   </details>

2.  As a firstime user I want to know the location of the gym

    | **Feature** | **Action** | **Expected Result** | **Actual Result** |
    |-------------|------------|---------------------|-------------------|
    | Map | Scroll down on first page and click the google mag  | Goolge show gym location in the city | Works as expected |

     <details><summary>Screenshots</summary>
     <img src="docs/features/test-user-story/inkedlocatmap.jpg">
     </details>

3. As a first time user I want to see the gym interior
   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Gym interior image | Scroll down on home page | Find pictures of the gym interior | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/features/test-user-story/intteaser.jpg">
    </details>

4. As a first time user I want to know what training programs are available 

   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Trian with us and Gym comforts list | Scroll down on home page  | Readable intriguing list | Works as expected |
    <details><summary>Screenshots</summary>
    <img src="docs/features/test-user-story/inkedfeatureslist.jpg">
    </details>

5. As a returning user I want to know where to sign up
   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Signup From | Cick signup button,Nav bar | Directed to signup page | Works as expected |

    <details><summary>Screenshots</summary>
    <img src="docs/features/signupform.PNG">
    </details>

6. As a returning user i want contact information   
   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Footer  on all pages | On any page scroll to the footer | See phone number and email address | Works as expected |

     <details><summary>Screenshots</summary>
     <img src="docs/features/test-user-story/inkedcontactinfo1.jpg">
     </details>

7. As a returning user I was to know the reason and the mission of the gym

   | **Feature** | **Action** | **Expected Result** | **Actual Result** |   
   |-------------|------------|---------------------|-------------------|
   | About Us pragraph | Navigate to the us page in menu bar  | Read  | Works as expected |

     <details><summary>Screenshots</summary>
     <img src="docs/features/test-user-story/inkedmenu-aboutusnav.jpg">
     <img src="docs/features/aboutus.PNG">
     </details>

8. As a returning user I want to know about the membership and options available

   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Membership Cards | Navigate to the About Uspage Scrooll down | Read | Works as expectd |

     <details><summary>Screenshots</summary>
     <img src="docs/features/test-user-story/inkedmenu-aboutusnav.jpg">
     <img src="docs/features/test-user-story/inkedcards.jpg">
     </details>

9. As a returning user, I want to see the gym's social media followings 

   | **Feature** | **Action** | **Expected Result** | **Actual Result** |
   |-------------|------------|---------------------|-------------------|
   | Footer - social media section | On any page scroll to the bottom | Click on social media links | Works as expected | 

     <details><summary>Screenshots</summary>
     <img src="docs/features/test-user-story/inkedsociallinks.jpg">
     </details>


10. As a siteowner I want the users to not only sign up but have membership option

    | **Feature** | **Action** | **Expected Result** | **Actual Result** |
    |-------------|------------|---------------------|-------------------|
    | Signup Form | U Navigate sign up page click dropdown option| Choose from drop down option | Works as expected |

    <details><summary>Screenshots</summary>
    <img src="docs/features/test-user-story/inkedsignupnav.jpg">
    <img src="/docs/features/test-user-story/inkedcardoptions.PNG">
    </details>

11. As a owner I want user to have a cutomized 404 error page if the wedsite fail to load

    | **Feature** | **Action** | **Expected Result** | **Actual Result** |
    |-------------|------------|---------------------|-------------------|
    | 404 error page | On non-matched URL| Choose from drop down option | Works as expected |

    <details><summary>Screenshots</summary>
    <img src="docs/features/test-user-story/404page.PNG">
    </details>

12. As a site owner I want users to leave comments upon sign up

    | **Feature** | **Action** | **Expected Result** | **Actual Result** |
    |-------------|------------|---------------------|-------------------|
    | Signup form | Navigate to signup page | Leave comments | Works as expected |

     <details><summary>Screenshots</summary>
     <img src="docs/features/test-user-story/inkedsignupnav.jpg">
     <img src="docs/features/comments.PNG">
     </details>
    
## Bugs
  List of bugs found and fixes used ti mitigate them.

- Bug: the first page had overflow to the right of the page.
  Fix: with from the slack community i was refered to unicorn revealer which showed my opentimes width was too much. Adjusted this and issue was fixed
- Bug: during accessibilty test my good practice points were low
  Fix: using the unicorn revealer again imanaged to find my logo image had margin space and my about us text had border radius value that were unneccessary. Adjusted these issues and my score got better
- Bug: during html validation signup.html error, signup form "for" value and "id" value were not matching  
    Fix: Change both value to the same which rectified error
- Bug: html validation for index.hmtl warnings for lack of heading h1-h6 in section tags
  Fix: removed unneccesary section tags
- Bug: html validation error for all html file h1-h6 heading, some sequence wer skipped h2-h4 and    h2-h5 
   Fix: changed heading tag for all html file to the correct sequences
- Bug: Wave error for color contrast on navbar and more about us button "deep orange and very dark blue"
  Fix: change to a slightly brighter orange to mitigate issue,
- Bug: Wave error for color conflicting contrast with cover text for the hero image on the home page
  Fix: Add a lite background overlay wrapped in a div tag to mitigate issue
- Bug: loading performance on the home page was low due to hero image loading time
  Fix: replaced hero-image 
- Bug: background image for the "Become a Member" page look streched with distorted pixels
  Fix: Replaced "Become a Member" page backgroung image
- Bug: hero image overlay half way over the image  onthe big screen and overflowing into the ethos section
   Fix: adjusted padding bottom and confirmed issue was no longer present


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
The website was deployed using GitHub Pages by following these steps:
1. In the GitHub repository navigate to the Settings tab
2. On the left hand menu select Pages
3. For the source select Branch: master
4. After the webpage refreshes automaticaly you will se a ribbon on the top saying: "Your site is published at "https://ewie1.github.io/CI_PP1_GLG/index.html"

You can for fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)  
7. Press Enter to create your local clone.

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
 - My HTML code from lessons and formats from the html module and walk through project which then evolved into my owm structure as i gain more knowledge by trail and error.
 - My CSS code was also built on the concept of trail and error, google W3School wedsite tips.



## Acknowledgements
- Tanks and acknowlegement goes to my mentor Mo Shami great guidance.
- Acknowledge my brother Addan Mc Collin for support form a user's veiw
- Thanks to my girlfriend Hiba Salem for support and input on a user veiw
- Thankful to the Slack team for tips