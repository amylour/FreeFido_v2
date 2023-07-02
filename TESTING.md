# Testing

This is the TESTING file for the [FreeFido](https://github.com/amylour/FreeFido_v2) website.

Return back to the [README.md](README.md) file.

## Testing Contents  
  
- [Testing](#testing)
  - [Testing Contents](#testing-contents)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Score](#wave-accessibility-score)
  - [User Input Validation](#user-input-validation)
  - [Defensive Design](#defensive-design)
  - [Browser Testing](#browser-testing)
  - [Manual Testing](#manual-testing)
    - [Testing User Stories](#testing-user-stories)
  - [Bugs](#bugs)
    - [Known Bugs](#known-bugs)

## Validation

I like to ensure that I have completed a thorough testing of my project so that no surprises are left for the user. 

### HTML Validation

For validation of my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

I have had to follow a different approach for validating my HTML for this project as the majority of my pages are developed using Jinja syntax such as '{% extends "base.html" %}' and '{{ form|crispy }}' and most require user authentication. The HTML validator will throw errors if I were to use my website's URL so I have had to follow the below approach for every page:

- Via the deployed Heroku app link, I have navigated to each individual page.
- Right clicking on the screen/CTRL+U/⌘+U on Mac, allows a menu to appear, giving me the option to 'View page source'.
- The complete HTML code for the deployed page will appear, allowing you to select the entire code using CTRL+A/⌘+A on Mac.
- Paste the copied code into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, revalidate by following the above steps and record the results.

| Page | Screenshot | Errors | Warnings |
| ---- | ---------- | ------ | -------- | 
| Home | ![screenshot of home page validation](documentation/testing/) |   |   |
| Sign In | ![screenshot of sign in page validation](documentation/testing/) |  |  |
| Sign Up | ![screenshot of sign up page validation](documentation/testing/) |  |  |
| Profile | ![screenshot of profile page validation](documentation/testing/) |  |  |
| Edit Profile | ![screenshot of edit profile page validation](documentation/testing/) |  |  |


### JavaScript Validation

### Python Validation

![Pep8 Linter Validation]()  

### Lighthouse Scores

![Lighthouse scores]()

### Wave Accessibility Score

<hr>

## User Input Validation

| Feature                    | Tested?  | User Input Required | User Feedback Provided     |
|----------------------------|----------|---------------------|----------------------------|

<hr>

## Defensive Design

- Security features, AllAuth, csrf tokens, error pages
- Google deceptive site issue docs/info

## Browser Testing

<hr>

## Manual Testing

### Testing User Stories


## Bugs

| No. | Bug | Solved | Fix | Solution Credit | Commit no. |
| --- | ---------------- | ---- | ------------- | -------------- | ------------|
| 1   |   Slug not saving as prepopulated field with 'Title' data entered by user  |    U+2713    |   <https://www.sankalpjonna.com/learn-django/how-to-override-the-save-method-in-your-django-models>  |   e6fb88e  |
| 2   |  Search function not yielding article return  |  U+2713  | removed 'author', a ForeighKey from the search function in articles/views.py   |   <https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains>         |          |
| 3   |     |       |     |          |            |

### Known Bugs
