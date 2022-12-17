# **_The Pokemon Forum - Project Portfolio 4- Django_**

This is a Pokemon Reddit style Forum for all the Pokemon fans out there that want to interact with others in this community and create discussions but also make new friends in the Pokemon World.
This is my 4th Project that I have created.

# Contents

- [**Objective**](#objective)
- [**User Experience UX**](#user-experience-ux)
  - [Design Prototype](#design-prototype)
  - [Site Structure](#site-structure)
  - [Design Choices](#design-choices)
  - [Typography](#typography)
  - [Colour Scheme](#colour-scheme)
  - [Project Management](#project-management)
- [**Features**](#features)
  - [Startup Display](#startup-display)
  - [Main Menu](#main-menu)
  - [Quiz Hub Menu](#quiz-hub-menu)
  - [Select Difficulty](#select-difficulty)
  - [Quiz](#quiz)
  - [Quiz Leaderboards](#quiz-leaderboards)
  - [Quiz Statistics](#quiz-statistics)
  - [Quiz Rules](#quiz-rules)
  - [F1 Info Hub Menu](#f1-info-hub-menu)
  - [View F1 Fact](#view-f1-fact)
  - [Select A Track](#select-a-track)
  - [F1 2022 Calendar](#f1-2022-calendar)
  - [F1 2022 Drivers](#f1-2022-drivers)
  - [Submit Feedback](#submit-feedback)
  - [Exit App](#exit-app)
- [**Future Features**](#future-features)
  - [Latest News](#latest-news)
  - [Polls](#polls)
- [**Technologies Used**](#technologies-used)
- [**Python Packages**](#python-packages)
- [**Testing**](#testing)
- [**Deployment To Heroku**](#deployment-to-heroku)
- [**Credits**](#credits)
  - [**Content**](#content)
  - [**Media**](#media)
  - [**Code**](#code)
- [**Acknowledgments**](#acknowledgements)
- [**Personal Development**](#personal-development)

# Objective

The objective was to create a reddit style forum where user's can interact by commenting on posts and viewing other people's content and pages. This project was to show your ability to use Django with databases

# User Experience (UX)

## Site Structure

The design of this website is simply to terms of accessing everything on one page to keep the user focused on the main page.

# Features

## Existing Features

- ### Login Feature
  - This is a self made login
    feature that does not use Django own login feature.
  - You can add an email and password to it.
- ### Search Bar
  - a dynamic search bar where you can search even with just a letter to find any topic or post that was made on the website.
- ### Topics
  - created a topics section on the website where users will see a list of topics that are being discussed and has a more feature at the end that will show more topics that are created.

## Design Choices

- ### Typography

  DM Sans is a low-contrast geometric sans serif design, intended for use at smaller text sizes. DM Sans supports a Latin Extended glyph set, enabling typesetting for English and other Western European languages.

- ### Colour Scheme

# Testing

## Code Validation

The code on the 'Review | Alliance' site has been tested through W3C Markup Validation Service, W3C CSS Validation Service and JSHint. Errors were at first found on the site in the W3C Markup Validation Service but could quite easily be fixed (see bugs section). One error appeared as well in the W3C CSS Validation but that was connected to Font Awesome and not to the site code itself (see bugs section).

### Markup Validation

After fixing the inital errors that W3C Markup Validation Service reported, no errors were returned.

<details><summary><b>HTML Validation Result</b></summary>

![HTML Result Home Page](readme/assets/images/html_validation_no_error.png)

</details><br/>

[Back to top](#table-of-content)

### CSS Validaton

When validating my own code the W3C CSS Validator reports no errors.

<details><summary><b>CSS Validation Result</b></summary>

![CSS Result](readme/assets/images/css_validation_no_error.png)

</details><br/>

[Back to top](#table-of-content)

### PEP Validation

At the time of this project the website [pep8online](http://pep8online.com/) is currently offline.

- admin.py - No errors or warnings reported
- forms.py - No errors or warnings reported
- models.py - No errors or warnings reported
- test_forms.py - No errors or warnings reported
- urls.py - No errors or warnings reported
- views.py - No errors or warnings reported

[Back to top](#table-of-content)

### JavaScript Validation

The JSHint validator results can be seen below:

No errors were returned when passing through JSHint (script.js) but the test reported one undefined variable connected to Bootstrap which is no problem.

<details><summary><b>JSHint Validation Result</b></summary>

![JSHint Validation](readme/assets/images/js_hint_validation.png)

</details><br/>

[Back to top](#table-of-content)
