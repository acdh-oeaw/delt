# DELT
Database of English Learner Texts (DELT).

## About
The Database of English Learner Texts (DELT) aims to promote research on the learning and use of English.

The current web application is based on [djangobaseproject](https://github.com/acdh-oeaw/djangobaseproject).


## Install
1. Clone this repository.
2. Create and activate a virtual environment.
3. Install the required packages `pip install -r requirements.txt`.
4. Run `makemigrations`, `migrate` and `runserver`.
5. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

This project uses modularized settings (to keep sensitive information out of version control or to be able to use the same code for development and production). Therefore you'll have to append a `--settings` parameter pointing to the settings file you'd like to run the code with to all `manage.py` commands. For example, run `python manage.py makemigrations --settings=delt.settings.dev`.


Be aware that the actual data for this database/web-app is not part of this repository. 
