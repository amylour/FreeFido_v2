# FreeFido

![freefido responsive screenshot](documentation/final_views/freefido_amiresponsive.png)

## Introduction

FreeFido is a social media and booking app for a private dog park. FreeFido has been developed as part of the Code Institute's Full-Stack Developer course as my 4th project - focusing on Django and Bootstrap frameworks, Database manipulation and CRUD functionality. It is for educational purposes only.

View live site here : [FreeFido](https://freefido.herokuapp.com/)

<hr>

## Table of Contents

- [FreeFido](#freefido)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
  - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
    - [Font](#font)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
  - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [Sprints](#sprints)
  - [User Stories](#user-stories)
    - [Visitor User Stories](#visitor-user-stories)
    - [Epic - User Profile](#epic---user-profile)
    - [Epic - Articles](#epic---articles)
    - [Epic - Booking](#epic---booking)
    - [Epic - Photo Gallery](#epic---photo-gallery)
    - [Epic - Visit Us/Reviews](#epic---visit-usreviews)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton Plane](#skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
    - [Security](#security)
  - [Features](#features)
    - [User View - Registered/Unregistered](#user-view---registeredunregistered)
    - [CRUD Functionality](#crud-functionality)
  - [Future Features](#future-features)
  - [Technologies \& Languages Used](#technologies--languages-used)
    - [Libraries \& Frameworks](#libraries--frameworks)
    - [Tools \& Programs](#tools--programs)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Heroku deployment](#heroku-deployment)
    - [Cloudinary API](#cloudinary-api)
    - [Clone project](#clone-project)
    - [Fork Project](#fork-project)
  - [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
  - [Acknowledgements](#acknowledgements)

## Overview

FreeFido is an social media and booking app for a private dog park. Users are invited to:

- Join the Freefido community
- Create their own profiles
- Add and interact with articles
- Create and manage their bookings
- Upload their favourite snaps from the park
- Discover more about the dog park

FreeFido is accessible via all browsers with full responsiveness on different screen sizes. Its aim is to create a safe, informed community of dog owners who can interact and share with each other and avail of the essential booking feature to reserve a spot in the secure, private dog park. I have created this site to meet the needs of the growing private dog park business. Private dog parks have become a highly sought after service for dog owners to exercise and train their dogs in a safe, secure area, without the fear of a strange dog running up to them. Dog reactivity is unfortunately on the rise at public dog parks due to some dog owners being unaware of dog body language and basic etiquette. FreeFido aims to offer a starting point for creating a community of regular users of this dog park who can book one hour slots through the basic booking system. In future development of this project, I hope to offer users an upgraded booking system with payment options, the opportunity to connect with other parks users with compatible dogs via adding a friend and direct messaging, hire a trainer and purchase merchandise and training equipment.


# UX - User Experience

## Design Inspiration

I was really excited to get working on this project's frontend as I could see the final product from the very beginning. I wanted to create a website that had plenty of clean whitespace that allowed colourful, bright icons to pop for each section of the website. The colours chosen were very specific from the beginning and I was careful to manipulate the CSS for each section to carry the relevant, related colour through. Original inspiration was from the Fisher-Price toy games controller, I had wanted to create an interactive, service-based website, with it's own logo using the colour scheme of the games controller. Once I had chosen the font of 'Outfit' and created the logo on Procreate, the website content followed swiftly and I had great fun developing it.

![Fischer Price controller](documentation/final_views/fp_toy.webp)  
*Original inspiration for the design process*

![FreeFido logo](documentation/final_views/logo.png)  
*FreeFido logo in font 'Outfit' using colours inspired by the toy*

### Colour Scheme

As mentioned above, the colour scheme and logo drove the design of the website. I wanted to create a 'fun' environment for the user to create the connection with the enjoyment that they would have with their dog at the park. The colours represent different sections/features of the website. I balanced the vibrant shades with a classic, #fff white background and an off-black shade of #0d0d0d, as I felt that it yielded a slightly more matte effect that #000 black. This combination also yielded a high contrast ratio of 19.44 for accessibility, with my colour scheme also passing a Colour Blind Safe check via [Adobe Color](https://color.adobe.com/create/color-wheel). This check was important for accessibility as the colours would form the base for my page and feature icons. Each colour in the scheme was also contrast checked with black #0d0d0d to ensure no contrast issue, all passed.

The corresponding sections and colours and identifying CSS variables are:

- Authentication: #AC44F2 '--purple'
- Gallery: #3BD952 '--green'
- User Profile: #F29F05 '--orange'
- Visiting Information: #F25C5C '--coral'
- Booking: #4CE0C3 '--blue'

For the Login/Logout icon, a grey #a6a6a6 was used as a base colour. I felt this grey helped to balance the colours and prevent the icons from 'popping' too much for the eye in the navigation bar.

![balancing colours for website text,background and Login/Logout icon](documentation/final_views/safe_colours.png)  
*Black, white and grey used for backgrounds, text and Login/Logout icon*

![screenshot of colour scheme](documentation/final_views/color_small.png)  
*Colour Scheme for FreeFido website*

![colour blind safe colour swatch](documentation/final_views/color_blind_safe.png)  
*Accessibility check for colour scheme*

### Font

Using [Google Fonts](https://fonts.google.com/), I imported 'Outfit' and 'Montserrat' as a complementary font to my CSS file. Outfit is a playful, clear sans-serif which I felt worked well in designing my logo and for headers in my project. For future use, I envisoned merchandise bearing the logo for the FreeFido stall at the dog park. Montserrat was chosen as it gave more structure to the paragraph sections.

![outfit font design sheet](documentation/final_views/outfit.png)  
*Outfit, a Google Font designed by Rodrigo Fuenzalida*

In development, 'Outfit' was identified by variable '--title', whilst 'Montserrat' was set as '--main-font' within the CSS file. Similar to my setup for the project's colours, using variables helped to speed up the frontend process.

## Strategy Plane

The project goal was to build a simple booking app for a service. The 'product' was a one hour slot in a private, secure dog park and the 'user' was dog owners, trainers and walkers. As the service itself was uncomplicated, I aimed to create an easy, uncomplicated booking system for the user. Through planning and design prep work, I realised that there was an opportunity to treat this service like a 'brand' and develop the idea further. A social element was born from this with an idea for dog owners to be able to share advice and images of their furry friends on the website. This would hopefully help to create a happy group of park users who would recommend the park to others, share articles outside of the core group, and attract more users to sign up. Following common social-media design trends, I planned to use icons, high-quality, photographic images and an attractive, connected colour scheme.

### Site Goals

- Create a safe, happy environment for dog owners
- Use of playful colour to identify connected features of the website, plenty of white space to keep it fresh and to-the-point
- Commononly used, identifiable icons with some redesigns to fit the theme
- Easy UI for quick fulfillment of feature CRUD functionalities
- UX remains the same whther on mobile, tablet or desktop
- Scalable idea, for addition of future features to easily grow the business

## Agile Methodologies - Project Management

FreeFido is my first project following Agile planning methods. As someone who loves to prepare and plan, it was a joy to get to know and use. I used my [Github Projects Board](https://github.com/users/amylour/projects/4) to plan and document all of my work, initially I started with a Trello board to allow myself to make some mistakes and gather any scraps of notes or information that I had and then refined them into my Projects board. I'm sure the next time around will be a smoother process.

### MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for Freefido, identifying and labelling my:

- **Must Haves**: the 'required', critical components of the project. Completing my 'Must Haves' helped me to reach the MVP (Minimum Viable Product) for this project early, allowing me to develop the project further than originally planned.
  
- **Should Haves**: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves**: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.
- **Won't Haves**: the features or components that either no longer fit the project's brief or are of very low priority for this release. 

### Sprints

I broke down the time available to me before project submission and pushed to have the MVP completed a month out from the submission date of 17th July 2023. This was primarily due to family duties and wanting to have the bulk of the project completed before my son's school finished for summer. It was a busy time frame and I reached MVP status ahead of schedule, allowing me to push my learning and add some extra features. Initially I had started FreeFido (v1) in a separate repo and I was utilising my simultaneous learning of Tailwind to great success, until I ran into issues with my database. This was to be expected on my first project using database schemas and Django. I understood what my issues were and even after flushing the database successfully, I felt that time allowed to start afresh. This version of Freefido was set up much quicker, I had more confidence in understanding the process and I chose to stick with Bootstrap this time around to concentrate on reaching MVP. 

I broke my process into Dev (Developer) Tasks, User Stories and Testing Tasks, which I converted into issues and labelled fully on my projects board. I found adding comments to my issues helpful, as I could quickly record information/sources/fixes for developing later in my README.

My Sprints are representative of a general timeframe of focus on the stated areas, with study, project work and running a household, some sprints timeframes blended with each other as work was completed during every available free moment.

| Sprint No. | Sprint Content | Start/Finish Dates |
|------------|----------------|--------------------|
| #1 | Project Setup | 23/05/23 -> 25/05/23 |
| #2 | All Auth Setup/Site Navigation | 25/05/23 -> 01/06/23 |
| #3 | Profile/Articles Features | 27/05/23 -> 06/06/23 |
| #4 | Booking/Gallery Features | 07/06/23 -> 12/06/23 |
| #5 | Frontend Development | 13/06/23 -> 20/06/23 |
| #6 | Testing/Documentation | 04/07/23 -> 11/07/23 |


## User Stories

User stories and features recorded and managed on GitHub Projects -> (<https://github.com/users/amylour/projects/4>)


### Visitor User Stories

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **user**, I would like to **view the websites home page** so that I can **learn about it and the services it offers** | **MUST HAVE** |
| As a **user**, I can **find the websites navigation area** so that I **may easily navigate around the website** | **MUST HAVE** |
| As a **user**, I can **see the sites social media links at the bottom of the webpage** so that I can **visit, contact the business and follow them online** | **MUST HAVE** |
| As a **user**, I can **view any error pages with a 'Home' button** so that I **can get back to the homepage easily** | **MUST HAVE** |
| As a **user**, I want **to see a message when I have successfully/unsuccessfully completed an action** so that I can **receive feedback from my interaction with the website** | **MUST HAVE** |

### Epic - User Profile

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|    
| As a **user**, I can **use my email and password to login to my profile account** so that I can **use my profile to connect to the websites features** | **MUST HAVE** |
| As a **user**, I can **enter my email and password** so that I can **register an account with the website** | **MUST HAVE** |
| As a **user**, I can **enter my personal details** so that I can **create an account with FreeFido** | **MUST HAVE** |
| As a **user**, I can **receive feedback in the form of a logout page** so that **I can confirm that I have been logged out successfully** | **MUST HAVE** |
| As a **user**, I can **edit my user profile** to **update my personal details** | **MUST HAVE** |
| As a **user**, I can **click a delete button in my user profile setup** so that I **can delete all personal data, photos and bookings that are connected to me on the website** | **COULD HAVE** |

### Epic - Articles

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As an **user**, I want to be able to **create and view articles** so that I can **learn more about dog related topics** | **MUST HAVE** |
| As a **user**, I would like to **move to the next page** so that I can **view all of the articles** | **SHOULD HAVE** |
| As a **user**, I would like to **view an article's likes** so that I can **find the most interesting articles** | **COULD HAVE** |
| As a **user**, I can **visit the articles page** so that I **can read and interact with the articles** | **MUST HAVE** |
| As a **user**, I can **click on an article** so that I **can view it's contents** | **MUST HAVE** |
| As a **user**, I can **click a button icon** so that I **can like/unlike and article** | **COULD HAVE** |
| As a **user**, I can **comment on a post** so that I can **interact and get involved with the conversation** | **SHOULD HAVE** |
| As a **user**, I can **fill-in, edit and save an article text field** so that I can **create and share an article from my profile** | **MUST HAVE** |
| As a **user**, I can **click on the edit button of my article** so that I can **edit the article and save it again** | **MUST HAVE** |
| As a **user**, I can **click on the delete button on my own article page** so that I can **delete the article** | **MUST HAVE** |
| As a **user**, I can **enter a search term into the search bar** so that I can **search for particular articles and articles with information topics that I am interested in** | **SHOULD HAVE** |
| As a **user**, I can **click a delete button** so that I **can remove a comment that I have made** | **COULD HAVE** |
  
### Epic - Booking

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **user**, I can **view the booking home page** so that I can **learn about booking and see my active bookings** | **MUST HAVE** |
| As a **user**, I can **use the bookings page** so that I can **make a booking at the dog park** | **MUST HAVE** |
| As a **user**, I can **receive feedback via email when I make a booking** so that I **can confirm my booking and keep a copy of it in my email account** | **COULD HAVE** |
| As a **user**, I can **edit my confirmed bookings** so that I **can choose a different day or time slot or add an extra dog** | **MUST HAVE** |
| As a **user**, I can **click the 'Trash' icon under my booking** so that I can **delete that booking from my bookings list** | **MUST HAVE** |
| As a **user**, I can **get feedback from the website** that will **explain that only four active bookings are allowed per person** | **SHOULD HAVE** |

### Epic - Photo Gallery

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **user**, I can **visit the gallery page** so that I can **view the gallery wall of photos** | **COULD HAVE** |
| As a **user**, I can **click the upload image button on the Gallery page** so that I can **upload an image of my dog have fun in the park** | **COULD HAVE** |
| As a **user**, I can **click the trash can icon when I hover/click on a photo** so that I can **delete the photo** | **COULD HAVE** |

### Epic - Visit Us/Reviews

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **user**, I can **view the 'Visit Us' page** so that I can **see the businesses location and details** | **MUST HAVE** |
| As a **user**, I can **fill out a review form** so that I can **leave feedback about my park visit** | **COULD HAVE** |
| As a **user**, I can **edit my review** so that I can **correct a mistake or change my review** | **COULD HAVE** |
| As a **user**, I can **click the delete button beside my review** so that I can **delete a review that I made** | **COULD HAVE** |
    
    
## Scope Plane

As this would be a dual learning/building project using technologies that were new to me, such as Django, SQL, Bootstrap and Cloudinary, I was cautious to maintain consistent control over the scope of the project and not let my idea grow too big. With the sheer amount of files, I needed to lockdown my project features early on into manageable blocks so as not to lose track of the MVP. Following my learning of the Django MVC framework I was able to identify how to change the templated structure to produce different website features from my base HTML. This allowed me to build upon my original idea of 'Booking app' only, and to add a social experience around articles and shared images. Following Agile Planning Methodologies, I added my Developer Tasks, User Stories and Testing Tasks as issues on my [GitHub project board](https://github.com/users/amylour/projects/4), and set up Sprints to keep the flow of the project in check.

Essential features of my project were:

- A striking, accessible website that fulfils user needs
- Responsive website for users of mobile, tablet and desktop devices
- User authentication
- User Profile creation and editing
- Article feature with full CRUD functionality
- Booking feature with full CRUD functionality
- Gallery wall with adding/deletion of images
- Business details to inform the user

Planning my project thoroughly from the start allowed me to identify areas of importance for MVP completion and satisfaction of assessment criteria, and to balance them with the feasibility of the features.


## Structural Plane

From initial concept to finished product, icons as the navigation area was an idea that I stuck with. I wanted to understand how to implement icon-based UX successfully so that the user can easily understand its purpose. Combining icons from Google's [Material Symbols & Icons](https://fonts.google.com/icons?icon.set=Material+Icons) pack, icons from Flaticon and my colour scheme, I created my navbar icons. I edited my Login/Logout icons with a pawprint to have them fit the theme better.

![navbar icons](documentation/final_views/icons_row.png)  
*Navigation icons for FreeFido*
  
Accessibility is very important to me and in case I missed the mark with my icon idea, I ensured that I created tooltips for both mobile and desktop views that reveal the icons purposes on hover with the mouse and hover/light touch on mobile.
  
![desktop tooltips](documentation/final_views/tooltip_gif.gif)  
*Navigation bar tooltips demonstrated on Desktop*
  
Continuing with a similar shape of the icons, images and buttons on the Freefido website are given a border-radius ranging from 20px - 30px to round off the corners and keep the styling consistent throughout the project. 
  
![image with rounded corners](documentation/final_views/article_card_br.png)  
*Article card from the Articles section with rounded corner styling*
  
Headings were given thick, dashed, underline styling in the coordinating colour of their feature to mark the beginning of a section.
  
![header with underline](documentation/final_views/header_underline.png)  
*Sign Up page header with purple underline for Authentication related sections*  

A favicon was added of a purple tennis ball to fit with the theme of the website, keeping it playful.

![tennis ball favicon](documentation/final_views/ball_favicon.png)  
*Ball Favicon*

I utilised webkits to change the appearance of my scrollbar to include rounded endpoints and a muted, purple/teal colour-gradient. This was especially so the smaller scrollbar within the profile dashboard would fit in with the projects design.  
  
![scrollbar](documentation/final_views/scrollbar.png)  
*Modified Scrollbar*

To allow for ease of responsiveness, each section was designed keeping in mind the switch from 'row' to 'column' when moving from Desktop to Mobile/Tablet view. This approach allowed me to add more features to the project early on by reusing and repurposing sections of code.

## Skeleton Plane

### Wireframes

The wireframes for FreeFido were created in Figma and were high-spec from the beginning as I was sure of my design concept. [Figma](www.figma.com) is an easy and fast design system for web and software mockups that allows for great control and testing of ideas particularly within the specific frame sizes which represent different devices. As I was using Bootstrap, I was confident that I had created a modular structure for my feature elements that would suit a grid system and that would allow them to easily work across different devices and screen sizes. 

**Mobile/Tablet view for:**
- Home
- Sign Up
- Profile

Originally I had planned for the home page to be mostly icon based for quick and easy use. However, I felt that this format would suit a downloadable app version of FreeFido, instead of the web version, which regular users might avail of to give them quicker access to the booking page, especially if they are one-handed, walking the dog on the way to the park. This will be part of my future features for the project growth.

<details open>
    <summary>Mobile/Tablet Home Page Wireframe</summary>  
    <img src="documentation/wireframes/mt_home.png">  
</details>

<details>
    <summary>Mobile/Tablet Sign Up Page Wireframe</summary>  
    <img src="documentation/wireframes/mobile_tablet_sign_up.png">
</details>

<details>
    <summary>Mobile/Tablet Profile Page Wireframe</summary>  
    <img src="documentation/wireframes/profile_mt.png">
</details>

**Desktop view for:**
- Home
- Sign Up
- Profile
- Booking
- Gallery
- Find Us
- Contact Us

<details open>
    <summary>Desktop Home Page Wireframe</summary>  
    <img src="documentation/wireframes/home_desktop.png">  
</details>

<details>
    <summary>Desktop Home Page Footer Wireframe</summary>  
    <img src="documentation/wireframes/home_2_desktop.png">
</details>

<details>
    <summary>Desktop Sign Up Page Wireframe</summary>  
    <img src="documentation/wireframes/signup_in_desktop.png">
</details>

<details>
    <summary>Desktop Profile Create Page Wireframe</summary>  
    <img src="documentation/wireframes/profile_desktop.png">
</details>

<details>
    <summary>Desktop Profile View Page Wireframe</summary>  
    <img src="documentation/wireframes/profile_view_desktop.png"> 
</details>

<details>
    <summary>Desktop Booking Page Wireframe</summary>  
    <img src="documentation/wireframes/booking_desktop.png">
</details>

<details open>
    <summary>Desktop Booking Create Page Wireframe</summary>  
    <img src="documentation/wireframes/booking_create_desktop.png">  
</details>

I had grand ideas for re-creating this exact booking page in this deployment of FreeFido. However, as this was a learning/building project, my understanding of implementing packages such as Django agenda, scheduler and dj-booking reached a point after a few struggles where I felt that it was more important to follow my planning steps for MVP and deliver a basic, functional booking system first. I look forward to developing my booking sytem in the next version of FreeFido.

<details>
    <summary>Desktop Gallery Page Wireframe</summary>  
    <img src="documentation/wireframes/gallery_desktop.png">
</details>

<details>
    <summary>Desktop Gallery Add Photo Page Wireframe</summary>  
    <img src="documentation/wireframes/photo_desktop.png">
</details>

<details>
    <summary>Desktop Find Us/Contact Us Page Wireframe</summary>  
    <img src="documentation/wireframes/map_contact_desktop.png">  
</details>

Through the early development of FreeFido, I created an Article section to help with my learning and understanding of Django before I tackled a booking system. This feature stayed in and helped to grow the idea of having a social/educational theme to the website. There are no wireframes for my Article section but I was able to continue my modular approach to it's design by using other elements from the project's planning in it's creation.

### Database Schema - Entity Relationship Diagram

![ERD Image](documentation/wireframes/freefidov2.png)  
*Database Schema (ERD) for FreeFido displaying relationships between feature components saved within the database*

This Entity Relationship Diagram(ERD) demonstrates how each feature interacts with each other and the connected database. Using Django's User Model, and Django AllAuth to carry out all user authentication, a user_id is created when the user registers with their username and email. This allows the user to edit a blank profile, create new articles, add comments and photos which will display their username, and create and manage their bookings. For future development, a Feedback system will be included allowing users to leave a review of the park.

The Profile, Articles and Comments Models were inspired by the blog walkthrough by the Code Institute and the [Recipe App by Daisy McGirr](https://github.com/Daisy-McG/Recipe-Tutorial) during my learning of Django. They helped me to get a good and secure grasp of the templating structure and connected Python files to push my features further, make them my own and then develop my Booking and Gallery Models.

My Booking Model collects data from the user about them and their dog(s) which can be used by the Admin to confirm the booking and entry to the park at their alloted time. The booking form displays a dropdown menu for Breed Choices and the hourly slots that are available for booking. A DateField allows that booking date to be chosen.

Through the Admin Django Dashboard, the connected user_id to all data entered to the site means that the Admin can remove a User and their data completely through the additon of on_delete=models.CASCADE. At the moment, a user can remove any data they share with the site, but they cannot delete their account completely. This feature will come in the next version.

### Security

- AllAuth
- Defensive Design
- CSRF Tokens

## Features

### User View - Registered/Unregistered

It was important to me from the beginning that FreeFido be accessible to an unregistered user, in some capacitites. I wanted the website to sell the product to a new user quickly by immediately inviting them into the community through the park's information, articles and gallery sections. The following is a breakdown of the site's accessibility for registered/unregistered users:

| Feature   | Unregistered User | Registered User |
|-----------|-------------------|-----------------|
| Home Page | Visable           | Visable         |
| Profile   | Not Visible - 'Profile' icon only appears for registered users | Visable and full feature interaction available |
| Articles  | Visable but not interactable via 'Likes/Comments', 'Add Article' button not visible | Visable and full feature interaction available |
| Booking   | Icon visible but redirected to Sign In page/Sign Up through link | Visable and full feature interaction available |
| Gallery   | Visable but no option to 'Add Photo' | Visable and full feature interaction available |
| Visit Us  | Visable and map interaction available | Visible and map interaction available |


### CRUD Functionality

Users are able to Create, Read, Update and Delete their shared information on FreeFido. Some features make full CRUD functionality available, whilst others present the necessary options only. Here is my CRUD breakdown for FreeFido:

| Feature | Create | Read | Update | Delete |
|---------|--------|------|--------|--------|
| Profile | Created upon registration | Yes | Yes | Full Profile deletion is currently only available to Admin upon User Account deletion, the profile dashboard clears automatically if a user removes all of their articles or bookings |
| Articles | Yes | Yes | Yes | Yes |
| Bookings | Yes | Yes | Yes | Yes |
| Gallery | Yes | Yes | No - this feature felt unneccessary as it's intention is a 'quick-sharing' of a photo, a minimal amount of information is required and users are able to delete the image if they wish | Yes |


**Header & Navigation**

*For features showcase, screenshots of the features in use were taken on Laptop/iPad Pro/iPhone 12 Pro*

<details open>
    <summary>Header & Navigation - All Users (Profile Icon only visible to Registered, Logged-In Users)</summary>  
    <img src="documentation/final_views/nav.png">  
</details>

![Profile Icon](documentation/final_views/profileicon_nav.png)  
*Registered, Logged In view with Profile Icon*
    
    
**Home Page**

<details open>
    <summary>Home Page - Visible to all Users</summary>  
    <img src="documentation/final_views/home.png">  
</details>

In the Home Page 'Hero' section, when a user is not registered they will see a 'Sign Up' button under the section text, which will bring them to the sign up page. When logged in, they will see 'Book Today!' which will bring them to the booking page.


**About Page**

<details open>
    <summary>About Page - Visible to all Users</summary>  
    <img src="documentation/final_views/about.png">  
</details>

The 'About' section of the Home Page contains three sections of information for the user, 'About', 'Safety', 'Benefits'. These sections display paragraphs and bulleted lists of information about the park and its positive values and benefits. Within each paragraph is a colour-coded word which acts as a link to bring the user to an important section of the website.

![Paragraph link](documentation/final_views/linkarea.png)  
*'visit' provides a link to the Visit Us page as the user reads through the park's information*

<hr>

**Registration/SignUp**

<details open>
    <summary>Sign Up Page</summary>  
    <img src="documentation/final_views/signup.png">  
</details>


**Sign In**

<details open>
    <summary>Sign In Page</summary>  
    <img src="documentation/final_views/login.png">  
</details>

On successful Sign In, the user is greeted with feedback through a message which confirms sign in. The 'open padlock' Log In icon now changes to a 'closed padlock' Log Out icon that the user can click to begin the Log Out process.

![incorrect username/email warning](documentation/final_views/incorrect_sign_in.png)  
*User is given feedback if they submit incorrect details where one item is correct and the other is incorrect*

![fill out field warning](documentation/final_views/fill_field_warning.png)  
*Django built in field warnings for incorrect/forgotten fields input*

![Sign In message and Log In icon change](documentation/final_views/signin_message.png)  
*Sign In message and Log In icon change*


**Sign Out**

<details open>
    <summary>Sign Out Page</summary>  
    <img src="documentation/final_views/logout.png">  
</details>

![sign out message](documentation/final_views/signed_out.png)  
*User is given feedback in message format to confirm sign out, Profile icon no longer visible in navigation bar - message disappears after 3 seconds*  

<hr>

**Profile**

<details open>
    <summary>Profile Page - Registered Users only</summary>  
    <img src="documentation/final_views/profile.png">  
</details>


**Profile Edit**

<details>
    <summary>Edit Profile Modal</summary>  
    <img src="documentation/final_views/edit_profile.png">  
</details>

Modal appears over the Profile page and allows users to edit their Profile Picture, Display Name (Display Name will be required for the future features of leaving Feedback/Reviews and Direct Messaging) and Bio. Using the RichTextField input field, user's have more control of the formatting of their text if they wish.

<hr>

**Articles**

<details open>
    <summary>Articles Page - Unregistered User View (mobile/tablet), Registered User View with 'Add Article' icon (desktop)</summary>  
    <img src="documentation/final_views/articles.png">  
</details>

<details open>
    <summary>Read Article Page - Unregistered User View</summary>  
    <img src="documentation/final_views/art_unregview.png">  
</details>

![site pagination arrow for moving page every 6 articles](documentation/final_views/site_pag.png)  
*Site pagination kicks in to display 6 articles per page. Arrows at the base of the article section allow users to move forward and back*

Unregistered Users are free to read the articles and comments left on FreeFido but they cannot 'Like/Comment' them until they have signed up and logged in.

![like/comment count under article](documentation/final_views/like_comment.png)  
*A Likes and Comments counter is visible under every article. Logged-In Users can interact by clicking the heart outline to like. 'Heart outline' icon is replaced by filled Heart icon*

![zero likes icon](documentation/final_views/zerolikes.png)  
*Likes icon is represented by an outlined heart icon. When it receives a like from the logged-in user, it becomes a filled heart icon*

<details open>
    <summary>Add a Comment - Registered User View</summary>  
    <img src="documentation/final_views/comments.png">  
</details>

A comment box is visible to logged-in users only. Their comment is submitted for review by the Admin, once approved, the comment appears on the website.

![comment awaiting approval message](documentation/final_views/approval_comment.png)  
*Comment is awaiting approval message displayed after comment submit*

<details>
    <summary>Delete Comment - Registered User View for Comment Author only</summary>  
    <img src="documentation/final_views/comm_del_icon.png">  
</details>

For the author of the comment, when logged in, a trash icon will appear to allow them to delete the comment if they wish. 


**Create Article**

<details open>
    <summary>Create Article Page - Registered, Logged In User View</summary>  
    <img src="documentation/final_views/add_article.png">  
</details>

![feedback that article is awaiting spproval by Admin](documentation/final_views/art_approve.png)  
*Admin approval is required for articles to keep FreeFido on topic. Feedback is provided to the user by message that the article is awaiting approval*


**Edit Article**

<details open>
    <summary>Edit Article Page - Registered, Logged In User View - Article Author View - Edit/Delete Icon</summary>  
    <img src="documentation/final_views/art_eddel_reg.png">  
</details>

<details open>
    <summary>Edit Article Page - Only accessible to the Article Author</summary>  
    <img src="documentation/final_views/edit_article.png">  
</details>

<details open>
    <summary>Edit Article Message</summary>  
    <img src="documentation/final_views/art_updated_msg.png">  
</details>


**Delete Article**

<details open>
    <summary>Delete Article Page - Only accessible to the Article Author </summary>  
    <img src="documentation/final_views/delete_article.png">  
</details>

![delete article successful message](documentation/final_views/del_art_msg.png)  
*User is informed that their article has been deleted - message disappears after 3 seconds*


**Search Function**

<details open>
    <summary>Search Function - Visible on Article pages only</summary>  
    <img src="documentation/final_views/search.png">  
</details>

<details>
    <summary>Search Function No Articles Found - Visible on Article pages only</summary>  
    <img src="documentation/final_views/no_articles.png">  
</details>

<hr>

**Bookings**

<details open>
    <summary>Bookings Page - Registered Users only</summary>  
    <img src="documentation/final_views/booking.png">  
</details>


<details open>
    <summary>Bookings Page - Max Bookings Reached</summary>  
    <img src="documentation/final_views/maxbooking.png">  
</details>


**Booking Create**

<details open>
    <summary>Booking Create Page - Visible only to Logged-In Users</summary>  
    <img src="documentation/final_views/booking_c.png">  
</details>  
  
![past booking warning](documentation/final_views/past_book.png)  
*Warning shown to Users if they choose a date in the past, can only save a booking with a valid date/time*  
  
![unavaialable date/time](documentation/final_views/unavailable_datetime.png)  
*If a date/time combo is unavailable then the user is informed via warning message - future version of the booking system will have shaded out portions for the unavailable dates/times to make it easier on the user*

![booking saved message](documentation/final_views/booking_saved_msg.png)  
*User feedback is delivered by message once a booking has been submitted through creation or edit- message disappears after 3 seconds*


**Edit Booking**

<details open>
    <summary>Edit Booking Page - Visible for Logged-In Users who have made a previous Booking</summary>  
    <img src="documentation/final_views/booking_e.png">  
</details>


**Delete Booking**

<details>
    <summary>Delete Booking Page - Visible for Logged-In Users who have made a previous Booking</summary>  
    <img src="documentation/final_views/booking_d.png">  
</details>

![deleted booking message](documentation/final_views/booking_del_msg.png)  
*User feedback is delivered by message once a booking has been deleted - message dissappears after 3 seconds*

<hr>

**Gallery**

<details open>
    <summary>Gallery Page - Registered User View with 'Add Photo' icon, Unregistered User View without icon</summary>  
    <img src="documentation/final_views/gallery.png">  
</details>

<details open>
    <summary>Gallery Page - Unregistered User view with photo info on hover(Desktop)/touch (on Mobile)</summary>  
    <img src="documentation/final_views/gal_unreg_info.png">  
</details>

**Add Photo**

<details open>
    <summary>Add Photo Page - Registered Users only</summary>  
    <img src="documentation/final_views/add_photo.png">  
</details>

**Delete Photo**

<details open>
    <summary>Photo Delete - Registered User View - delete icon only visible over the photos uploaded by that logged-in user. </summary>  
    <img src="documentation/final_views/gal_reg_del.png">  
</details>

<details open>
    <summary>Delete Photo Page</summary>  
    <img src="documentation/final_views/del_photo_modal.png">  
</details>

![delete photo user message, successful deletion](documentation/final_views/photo_del_msg.png)  
*User feedback is provided by message, informing user that the photo has been deleted successfully - message disappears after 3 seconds*


**Visit Us**

<details>
    <summary>Visit Us Page</summary>  
    <img src="documentation/final_views/visit.png">  
</details>


**403, 404, 500 Pages**

These templates were added to this project in order to give the user the functionality to return to the website by using the links in the navigation bar or the Back to Homepage button on the Error page.

![404 error page](documentation/final_views/404error.png)

- They are triggered when a user tries to access:
  - information that is not theirs - 403,
  - information that does not exist anymore - 404,
  - something has gone wrong with the server and cannot retrieve database - 500

**Admin Panel**

Through Django's built-in Administration Panel, the Admin has full access over the data submitted to the website by registered Users.

![django admin panel view](documentation/final_views/dj_adminpanel.png)  
*Django Admin panel view for FreeFido Administrator - content selection menu on left hand side*

Users articles and comments require approval by the Admin of FreeFido to keep the website content on topic. Admin can change the status of articles from 'Draft' to 'Published'.


![dj admin panel articles approval](documentation/final_views/draft_art.png)  
*Dropdown menu allowing Admin to 'publish' a users article*  
    
    
![dj admin panel comments approval](documentation/final_views/comment_apprv.png)  
*Dropdown menu allowing Admin to 'approve' a users comment*
  
Admin can control users booking via the panel.

![dj admin panel bookings](documentation/final_views/djbooking.png)  
*All bookings are made available to the Admin*



## Future Features

- Admin key icon for superuser login
- Updated Booking system using django agenda/scheduler that shows unavailable dates and times
- Downloable app with quicker access to booking system for regular users
- Member to member contact via DM, connecting profiles to allow for sharing bookings with compatible dogs
- Merchandise section with dog training items/treats available for collection at the Freefido coffee hut at dog park entrance
- Book a Trainer/Join training classes
- Quick info about local area for visitors eg pet stores/vets/dog-friendly restaurants

## Technologies & Languages Used

- HTML
- CSS
- JavaScript
- Python
- [Git](https://git-scm.com/) used for version control.
- [Github](https://www.github.com) used for online storage of codebase and Projects tool.
- [CodeAnywhere](https://app.codeanywhere.com) as an online, cloud-based IDE for development.
- [Figma](https://www.figma.com) for project design planning and wireframe creation.
- [Adobe Color](https://color.adobe.com) for colour theme creation and accessibility checkers.
- [Django](https://www.djangoproject.com/) was used as the Python framework for the site.
- [Cloudinary]()
- [ElephantSQL]()
- [Heroku]()
- [WAVE](https://wave.webaim.org/) to evaluate the accessibility of the site.
- [Procreate](https://procreate.com/) for image creation and editing.
- 

### Libraries & Frameworks

- Bootstrap v5.2.3
- Django v3.2.19
- Django AllAuth v0.54.0
- Django Crispy Forms v2.0
- Crispy Bootstrap5 v0.7
- Django Resized v1.0.2
- Django RichTextField v1.6.1
- Django Summernote v0.8.2
- Python Slugify v8.0.1
- Pillow v9.5

### Tools & Programs

- [EZGif](<https://ezgif.com/>) for gif conversion.
- [Convertio](https://convertio.co/) for file conversion to PNG, WEBP.
- [Tiny Png](https://tinypng.com/) for file size reduction.
- [Lucidchart](https://www.lucidchart.com/pages) for ERD (entity relationship diagram) creation.
- [Trello](https://www.trello.com) for intial project agile planning.
- [Perplexity AI](https://www.perplexity.ai/) for breaking down Python concepts and documentation into more understandable chunks.

## Testing

- For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

### Heroku deployment

### Cloudinary API

### Clone project

### Fork Project

## Credits

Django save method in models.py (<https://docs.djangoproject.com/en/4.2/ref/models/instances/>)
Django UserCreationForm | Creating New User (<https://www.javatpoint.com/django-usercreationform>)
Advanced User Profile creation using allauth/signals (<https://dev.to/thepylot/create-advanced-user-sign-up-view-in-django-step-by-step-k9m>)
Override Django's save method (<https://www.sankalpjonna.com/learn-django/how-to-override-the-save-method-in-your-django-models>)
TypeError Datetime object issue for same day bookings - (<https://bobbyhadz.com/blog/python-check-if-variable-is-datetime-object>)
                                                      - (<https://bobbyhadz.com/blog/python-typeerror-datetime-datetime-object-is-not-callable#:~:text=The%20Python%20%22TypeError%3A%20'datetime,and%20the%20built%2Din%20classes.>)
Find the parent form element of delete confirm button (<https://www.geeksforgeeks.org/difference-between-dom-parentnode-and-parentelement-in-javascript/>)
Bootstrap documentation for credited components used in project (<https://getbootstrap.com/>)
Scrollbar styling ( https: //www.w3schools.com/howto/tryit.asp?filename=tryhow_css_custom_scrollbar2)
Browser autofill styling overrule (<https://stackoverflow.com/questions/2338102/override-browser-form-filling-and-input-highlighting-with-html-css>)
Django Docs to make model item readonly for search function showing deleted articles (<https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields>)
Django cleaned data how to (<https://overiq.com/django-1-10/django-form-basics/?utm_content=cmp-true>)

### Code

### Media

- Code Institute Student Channel on Youtube: for guidance on project setup, tips and guidance.
- [Daisy McGirr's Youtube playlist on Django](https://www.youtube.com/@IonaFrisbee) a great help for understanding how to get a Django project moving from the beginning stages.
- [Adel Codes - Youtube - Service Appointment Sys using Django](https://www.youtube.com/watch?v=HTHqEr3R_Kw&t=81s)

### Additional reading/tutorials/books/blogs

## Acknowledgements
