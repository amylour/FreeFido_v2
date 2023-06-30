# FreeFido

![freefido responsive screenshot](documentation/final_views/freefido_amiresponsive.png)

## Introduction

FreeFido is a social media and booking app for a private dog park. I have created this app for the Code Institute's Full-Stack Developer Course and it is for educational purposes only. FreeFido has been developed as part of the Code Institute's Full-Stack Developer course as my 4th project - focusing on Django and Bootstrap frameworks, Database manipulation and CRUD functionality.

View live site here : [FreeFido](https://https://freefido.herokuapp.com/)

<hr>

## Table of Contents

- [FreeFido](#freefido)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [UX](#ux)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
    - [Agile Methodologies](#agile-methodologies)
    - [Epics/Milestones](#epicsmilestones)
    - [User Stories](#user-stories)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton Plane](#skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
    - [Security](#security)
  - [Features](#features)
  - [Features](#features-1)
  - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
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




## UX

## Strategy Plane

### Site Goals

### Agile Methodologies

### Epics/Milestones

### User Stories

User stories and features recorded and managed on GitHub Projects -> (<https://github.com/....>)

- Business Owner/Site Admin
- Visitor
- Regular Visitor

**EPIC | Site Navigation**
- As a User I can easily navigate around the site so that I can view different pages and sections on the site.
- As a User I can click on the about page so that so that I can find out what the website is about and how to use it.

**EPIC | Crud Functionality**

**EPIC | Administration**
- As a Site admin I can administer the site so that I can manage the sites content.
- As a User I can reset my password so that I can change it if I have forgotten it or want to change it.

**EPIC | Register / Sign in and out**

## Scope Plane

- MVP/Identifying necessary features/Sprints
- Opportunities(arising from user stories) -> Importance  |  Vialbility/Feasibility
- Responsive Design
- CRUD Functionality

## Structural Plane

- Accessibility
- Responsiveness
- Navigation

## Skeleton Plane

### Wireframes

- Mobile/Tablets/Desktop
- Index/Home
- Register
- Login
- Profile
- About
- Booking
- Contact Us/Map

<details>
    <summary>Home Page</summary>  

![Wireframe of home page](readme-docs/wireframes/wireframe-home.jpg)  
</details>

### Database Schema

- AllAuth User Model
- ERD Diagram
- Custom Models
  - Profile Model
  - Booking Model

### Security

## Features

## Features

**Header & Navigation**
    - details
    - details

**Home Page**

**About Page**

**Registration**
    - Email
    - Username (unique)
    - First Name
    - Last Name
    - Password
    - Password repeat

**Login**
- It includes a small welcome back message and a link to the Registration form for users who have not yet registered for an account.
- It uses django-allauth to provide all the settings for user authentication and includes the following fields:  

  - Email
  - Password

**Logout**

**Profile**

**Relevant pages included in build........

**CRUD Booking**

**Footer**

**403, 404, 500 Pages**

These templates were added to this project in order to give the user the functionality to return to the website by using the links in the navigation bar or the Back to Homepage button at the bottom of the page.

- They are triggered when a user tries to access:
  - information that is not theirs - 403,
  - information that does not exist anymore - 404,
  - something has gone wrong with the server and cannot retrieve database - 500

**Admin Panel**
Business Owner/Django Admin Panel/Superuser

## Future Features

## Technologies Used

### Languages Used

### Libraries & Frameworks

### Tools & Programs

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

### Code

### Media

### Additional reading/tutorials/books/blogs

## Acknowledgements
