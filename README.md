# Mindful App

St Robert Mindful Club Web Application

## Required Packages

- Docker-compose

## Installation

Clone the repository:

```bash
git clone https://github.com/redmac135/mindful.git
cd mindful
```

Create a copy of `.env.template` name it `.env` and fill out correct information:

```bash
cp .env.template .env
```

Create Docker Images and Run

```bash
docker-compose up --build -d
```

Create initial admin user in dg01 instance cli:

```bash
python manage.py createsuperuser
```

## Usage

The Mindful App currently serves as a self reflection and journaling site.
Users can create an account, fill out a short daily form, and see a dashboard of historical journal entries
