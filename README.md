# Mindful App

St Robert Mindful Club Web Application

## Required Packages

- Python 3.x
- NVM, Node.js, NPM

## Installation

Clone the repository:

```bash
git clone https://github.com/redmac135/mindful.git
cd mindful
```

Create a `mindful/.env` file and fill out correct information:

```bash
cd mindful
touch .env
cat .env
>>> SECRET_KEY=YOUR_SECRET_KEY
>>> SENDGRID_API_KEY=YOUR_SENDGRIND_API_KEY
>>> ZENQUOTES_API_KEY=YOUR_ZENQUOTES_API_KEY
cd ..
```

Install Python packages:

```bash
pip install -r requirements.txt
```

Install and build npm packages:

```bash
npm install
npm run postcss
npm run dev
```

Migrate database:

```bash
python manage.py migrate
```

Load fixtures:

```bash
python manage.py loaddata reflection/fixtures/choices.json
```

Create initial admin user:

```bash
python manage.py createsuperuser
```

Run server:

```bash
python manage.py runserver
```

## Usage

The Mindful App currently serves as a self reflection and journaling site.
Users can create an account, fill out a short daily form, and see a dashboard of historical journal entries
