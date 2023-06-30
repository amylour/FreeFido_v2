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

### HTML Validation

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
