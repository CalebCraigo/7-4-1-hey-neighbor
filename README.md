# Hey, Neighbor!

Gordon is a startup founder with a great idea that's "Uber for neighborhood tool sharing".

You've been tasked with making Gordon's dream of peer to peer tool sharing come true.

## Objectives

### Learning Objectives

After completing this assignment, you should know:

 * How to customize authentication in Django
 * How to configure `django.contrib.auth` templates
 * How to configure `django.contrib.auth` urls
 * How to create a foreign key to the `django.contrib.auth` user model
 * How to build a signup form
 * How to build a login form
 * How to determine if a user is logged in in a view
 * How to determine if a user is logged in in a template
 
## Requirements

* pep8 compliant 
* pep20 compliant
* responsive Bootstrap

## I am a Web Developer Mode

You need to build a tool sharing website that allows for users to create an account and login. Users should be able to add their items with a picture and price of the item.

Each user should have a screen that lets them see just their rental items that they've added.

Users should be able to see a list of other users and the tools that are available and select one that they would like to borrow. Users can borrow multiple items, but each item should only be borrowed by a single user at one time.

If an item is already borrowed, it should be marked as not available.

 * Setup your django project with a custom user model.
 * Create an `accounts` app that will have your login and signup views.
 * Create a `tools` app that will have your models, views, and templates for the following screens:
 	* Home page: Welcome screen with links to create account, etc.
 	* My Items: Screen of just items that a user has added.
 	* User List: Screen with a listing of all users in the system.
 	* User Tool List: Screen with a listing of tools that are added by a specific user. Each tool marked as available or not and a "Borrow Now" button if the tool is available.
 	
## Hey Mikey I think He Likes It

 * Allow users to borrow a tool with a "Check out" button
 
## Caffeinated Mode

 * Allow users to create a favorite tool list for easy lending in the future.
