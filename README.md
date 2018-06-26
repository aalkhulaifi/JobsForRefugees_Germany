# JobsforRefugees_Germany
Django project that matches refugees with local demand based on their location, allowing consumers to find help with everyday tasks .In addition, this project allows getting help with tasks that doesn't require a degree including cleaning, moving, delivery and handyman job.
## Installation

This is a Django 2.0 project. use the following steps:

1. Create a virtualenv
2. Manually install Django and other dependencies
3. `pip freeze > requirements.txt`
4. `django-admin startproject project .`
5. `./manage.py startapp rabbit_clone`.

From this initial state you can:

* install more Python libraries and add them to the `requirements.txt` file

## Local development

To run this project in your development machine, follow these steps:
1. Create a virtualenv
2. Manually install Django `pip install django`.
4. `django-admin startproject rabbit_clone .`
5. `./manage.py startapp main`.

6. Fork this repo and clone your fork:

    `https://github.com/aalkhulaifi/JobsforRefugees_Germany.git`

7. Install dependencies:

    `pip install -r requirements.txt`

8. Create a development database:

    `./manage.py migrate`

9. If everything is alright, you should be able to start the Django development server:

    `./manage.py runserver`

10. Open your browser and go to http://127.0.0.1:8000/main/home , you will see the home page.






