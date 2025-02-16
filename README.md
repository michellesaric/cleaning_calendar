# cleaning_calendar

## Description

This is an app that calculates dates when cleanings should occur when renting apartments. The goal is to make as less dates as possible so that cleanings occur on a minimum number of days.

## Technology

This app only containes the backend part of the web app and the technology used is FastAPI, database used is PostgreSQL.

## Packages

Packages used in this project are:

- fastapi - to import fastapi
- uvicorn - to start a web server
- httpie - to test the api endpoints
- sqlalchemy - provides the ORM for connecting PostgreSQL with FastAPI
- alembic - used for migrations
- python-jose - from JWT tokens
- psycopg2-binary - PostgreSQL database adapter for Python
- bcyrpt - for hashing passwords
- ics - for parsing .ics files
- validators - for validation of data
- dotenv - for creating enviroment variables(to hide secrets and algorithms)

## Detailed description of the task

This app is a cleaning schedule app. Actions that users can do are import and export calendars that are
guest reservations. Imports can occur by importing an .ics file or by putting an url that gets translated
to an ics file. After that, you can export those calendars(all of them or by id) and you get the name of
the apartment, all the start and end dates, the person that reserved the apartment and the cleaning schedule for that apartment.

Ideally, the number of dates for cleaning should be minimum. So, if there are possibilites to clean more
apartments on the same day, that should be done.

For auth, HTTPBearer and JWT tokens are used.
