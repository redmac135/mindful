# Mindful App

St Robert Mindful Club Web Application

## Required Packages

- Python 3.x 
- NVM, Node.js, NPM

## Installation 

1. Clone the rep
2. Create mindful/.env file and populate
3. Install python packages: `pip install -r requirements.txt`
4. Install npm packages: `npm install`
5. Build nesscary packages: `npm run postcss` and `npm run dev`
6. Migrate Database: `python manage.py migrate`
7. Load fixtures: `python manage.py loaddata reflection/fixtures/choices.json`
8. Create initial admin superuser: `python manage.py createsuperuser` 
9. Run server: `python manage.py runserver`

## Usage

The Mindful App currently serves as a self reflection and journaling site. 
Users can create an account, fill out a short daily form, and see a dashboard of historical journal entries



