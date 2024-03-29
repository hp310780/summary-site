# Simple Summary Site

![](site_home_page.png)

Simple summary site will allow you to add items and summarise their total cost.

*** **WARNING: This is a rudimentary proof-of-concept and requires much alteration to be productionised.** ***

## Requirements
* Python 3.9+
* Poetry

## Installation

1. Run `export FLASK_APP=summary_site`.
2. Run `export FLASK_DEBUG=1`.
2. Run `poetry install`.
3. Run `poetry run flask run`.
4. Navigate to http://127.0.0.1:5000 in your browser.

## Running Tests
1. Run `poetry run pytest`.

## User Flow
1. User signs up with email and password.
2. User can log in with above email and password.
3. User can add items to their list.
4. Users can select "Summarise" to calculate the total cost of their items.

## Requirements Fulfilled
* User sign up, log in and log out.
* User ability to add items to their list.
* User ability to calculate total cost of items.

Note, I am aware these are very rudimentary! Please see improvements needed for how this should be tackled properly.

## Improvements Needed
* Encapsulate flask app and environment variables needed in a docker image.
* Security and strength on sign up and log in process - E.g. Password strength checker, email verification and disabling multiple log in attempts in a short period of time. Could investigate AWS Cognito for this.
* Sqlite datastore adequate for small amount of users, would investigate other datastores for larger load.
* SQL queries need to be investigated for optimisation.
* Robust testing of functionality including edge cases. Test cases currently missing due to time constraints.
* Readability - Is this maintainable? Is this structured well?

## References
* [Authentication with Flask](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)