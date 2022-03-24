# Mindful App

St Robert Mindful Club Web Application

## Installation 

1. Clone the rep
2. Create mindful/.env file and populate
3. Install npm packages: `npm install`
4. Build nesscary packages: `npm run postcss` and `npm run dev`
5. Migrate Database: `python manage.py migrate`
6. Load fixtures: `python manage.py loaddata reflection/fixtures/choices.json`
7. Create initial admin superuser: `python manage.py createsuperuser` 
8. Run server: `python manage.py runserver`

## Usage

The Mindful App currently serves as a self reflection and journaling site. 
Users can create an account, fill out a short daily form, and see a dashboard of historical journal entries



