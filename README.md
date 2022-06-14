### Top 
<h1 style="text-align: center;"><strong>Axtaris</strong></h1>
<h2 style="text-align: center;"><strong>Welcome to the README PAGE of the Axtaris app</strong></h2>

### Link to the Axtaris app:  

<a href="https://axtaris.herokuapp.com/">https://axtaris.herokuapp.com/</a>

### Link to the GitHub page of Axtaris app:

<a href="https://github.com/cgauci87/axtaris">https://github.com/cgauci87/axtaris</a>

<p align="center">
<img width="350" height="250" src="./assets/images/axtaris.jpg" alt="Axtaris">
</p>

# Introduction

I had brief exposure to Python and its frameworks through personal projects done in the past year. 
This time round, I have decided to code a more advanced level of Python. I've chosen to build a web 
application which it functions as a price comparison tool through the given algorithm.


# Content

* [Built to practice](#built-to-practice)
* [User experience](#user-experience)
* [Buildpacks Used](#buildpacks-used)
* [Frameworks, Libraries & Programs I Used:](#frameworks-libraries-and-programs-i-used)
    * [Django](#django)
    * [Beautifulsoup](#beautifulsoup)
* [Proved By](#proved-by)
* [Features](#features)
* [Future features](#future-features)
* [Deployment](#deployment)
    * [How To Fork A Repository](#how-to-fork-a-repository)
    * [How To Clone A Repository](#how-to-clone-a-repository)
    * [How To Make A Local Clone](#how-to-make-a-local-clone)
* [Testing](#testing)
* [Code](#code)
* [Issues and bugs](#issues-and-bugs)
* [Special thanks](#special-thanks)
* [Contact](#contact)

# Built to practice

- Implement a given algorithm as a computer program.
- Adapt and combine algorithms to solve a given problem.
- Adequately use standard programming constructs: repetition, selection, functions, composition, modules, aggregated data (arrays, lists, etc.)
- Explain what a given program does.
- Identify and repair coding errors in a program.
- Use library software for building a web application.
- Implement a data model, application features, and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.
- Demonstrate and document the development process through a version control system such as GitHub.

# User experience

The user is welcomed with a search bar for quick and simple user experience.
The user is expected to  input a keyword related to a product i.e. electronic items.
The algorithm kicks in and once results fetch, user will be shown the lowest price of the searched item across different stores i.e. ebay and amazon.
Each result has description of the item, price and link to go directly to the said store to view product details and/or purchasing the item.


# Buildpacks Used

- heroku/python
- heroku/nodejs

# Frameworks, Libraries and Programs I Used

- [Django](https://www.djangoproject.com/)
- [Beautifulsoup](https://pypi.org/project/beautifulsoup4/)

# Proved By

- <a href="http://pep8online.com/" target="_blank">PEP8: </a> No errors found.

<p align="right">(<a href="#top">Back to top</a>)</p>

# Features

- The dominant feature in this app is a search bar where user can simply input their a keyword related to a product, to lookup for the lowest price in the market.
- The interactive feature in this app is an on-loading gif. This simple loading animated gif is perfect for catching the user's attention that data (results) are being 
pulled and will display the search results in a moment.
- Results will be featured, right below the search bar once data is fetched from the source.


# Future features

* In the future, I would like to add more stores and include a list of keywords as suggestions. The latter was initially on plan to be implemented within this version , however required more time and effort.
* Include attribute filtering where the end-user can filter by various attributes such as categories, shipping costs, item location, low to high price and vici versa.

<p align="right">(<a href="#top">Back to top</a>)</p>

# Deployment

This project was deployed using a personal Heroku account.

Steps for deployment:
- Fork or clone this repository
- Create a new Heroku app
- Set the buildpacks to Python and NodeJS in the order
- Link the Heroku app to the repository
- Click on **Deploy**


[How to Fork a Repository:](https://support.atlassian.com/bitbucket-cloud/docs/fork-a-repository/)
1. Login or Sign Up to [GitHub](https://github.com/).
2. On GitHub, go to [https://github.com/cgauci87/axtaris](https://github.com/cgauci87/axtaris)
3. In the top right corner, click "Fork".

[How to Clone a Repository:](https://support.atlassian.com/bitbucket-cloud/docs/clone-a-repository/)
1. Login in to [GitHub](https://github.com/).
2. Fork the repository [https://github.com/cgauci87/axtaris](https://github.com/cgauci87/axtaris) using the steps above in [How To Fork a Repository](#how-to-fork-a-repository)
3. Above the file list, click "Code".
4. Choose if you want to close using HTTPS, SSH or GitHub CLI, then click the copy button to the right.
5. Open Git Bash.
6. Change the directory to where you want your clone to go.
7. Type git clone and then paste the URL you copied in step 4.
8. Press Enter to create your clone.

How to make a Local Clone:
1. Login in to [GitHub](https://github.com/)
2. Under the repository name, above the list of files, click "Code".
3. Here you can either Clone or Download the repository.
4. You should close the repository using HTTPS, clicking on the icon to copy the link.
5. Open Git Bash.
6. Change the current working directory to the new location, where you want the cloned directory to be.
7. Type git clone and then paste the URL you copied in step 4.
8. Press Enter and your local clone will be created.

The site was deployed to Github pages using the following steps:
* In the Github repository, navigate to the settings tab.
* Scroll down and select Pages from the left side navigation menu to open Github pages.
* In the Source section, click on the dropdown menu and select the Main branch.
* Once the Main branch is selected the page, click Save and then will refresh to display a message stating "Your site is ready to be published at https://cgauci87.github.io/axtaris/"

<p align="right">(<a href="#top">Back to top</a>)</p>

# Testing

I have manually tested this project by conducting the following:
- Passed the code through a PEP8 linter and confirmed there are no flagged issues.
- Input keywords which are included in suggestions list to test functionality.
- Checked if the search button is working as expected.
- Checked for the on-loading gif
- Checked if the Item details are showing correctly.
- Checked if the price is being displayed as per store pricing.
- Tested the populated hyperlink once the View item is clicked.


# Code

**[Code explained in detail](./functions.md)**

* All code was written by myself.
* As far as I am aware, a simple price comparison app alike, does not exist online.
* Inspired by [webautomation.io](https://webautomation.io/blog/how-to-create-price-comparison-tool-with-beautiful-soup/)

# Issues and bugs

* At the initial testing, I came across an issue where I had no loading upon clicking Submit. Later I figure out that django-cors-headers which is a Django application for handling the server headers is required for Cross-Origin Resource Sharing (CORS)..
I solved the issue by adding django-cors-headers in requirments.txt so to get installed with the rest of other dependencies. <br>

<p align="right">(<a href="#top">Back to top</a>)</p>

# Special thanks

* I would like to thank the following people for the help they gave me with this project:

  - My mentor Brian O'Hare.
  - Help from my fellow students at Code Institute, through the relevant channels on Slack.

<p align="right">(<a href="#top">Back to top</a>)</p>