mkdir project-repo-name or git clone from github

which python

python3 -m venv VenvDjangoPortfolio

source VenvDjangoPortfolio/bin/activate

pip install django

which python

django-admin startproject portfolio

    rename 'portfolio' folder to 'portfolio-project'

cd portfolio-project

python3 manage.py runserver

    update the TIME_ZONE = from 'UTC' to 'EST' in the settings.py file

## difference between a project and an app in django

    project can contain many apps (and apps can be in more than one project, in theory)

django-admin startapp jobs

    add 'jobs' app to 'installed-apps' in settings.py

## url paths

    update settings.py

    update urls.py

    update views.py

    create  templates folder inside of jobs app

    create jobs folder inside of templates folder

    create lu.html file inside of jobs folder

## some clicks on /home

        urls file is checked
            if there is a matching url patterns/path, then follow the dot notation path to the appropriate views folder and find the named function

## models

image needs pillow
pip3 install pillow

install postgres

## postgres debugging

    see what processes are currently using postgres.
    ▶ ps aux|grep postgres

/Library/PostgreSQL/12/bin/pg_ctl start -D /Library/PostgreSQL/12/data -l postgres.log

postgres=# \password postgres
Enter new password:
Enter it again:
postgres=# CREATE DATABASE porfoliodb;
CREATE DATABASE
postgres=#

found postgresql settigns in studioapp project

pip install --upgrade pip

pip3 install psycopg2
()if necss
python3 -m pip install --upgrade requests

pip3 install psycopg2-binary
might need to change when making site live...need to figure out how I got the postgresql version in studioScheduler to work.

python3 manage.py makemigrations (in porfolio-project folder)

## admin

python3 manage.py createsuperuser

    add job model to admin site
         import jobs in admin.py

    create super user and object from Jobs Model

createsuperuser and object from Jobs Model

python3 manage.py createsuperuser

    update html page
        SYNTAX = {%variable %}
        i.e  {%for jobs in jobs.objects %}

## Bootstrap framework to make the app pretty

        view-source:https://getbootstrap.com/docs/4.4/examples/album/#

        use chome 'view page source' then copy source code
        then import bootstrap libraries into django/python


    click 'get started' view-source:https://getbootstrap.com/docs/4.4/examples/album/

copy css core & js and replace in html document

use the below to display objects in django

````

            <h1>All my jobs</h1>

    {% for job in jobs.all %}

    {{ job.summary }}

   <br>

    {% endfor %}
            ```
````

    (search for '' terms below)
    update 'title' tag (changes title of chrome tab)
    remove 'header' (deletes the grey bar)

    add links to buttons for email/ linkedin/ github
    test links

    remove footer

    create static folder( in jobs) and add a photo (drag and drop)

    add a static root to setting.py

    add a static root to setting.py

    import settings and static in urls.py

▶
python3 manage.py collectstatic

> > 131 static files copied to '/Users/LHD/Development/code/practice/practice-python/DjangoPortfolioProject/portfolio-project/static'.
> > (VenvDjangoPortfolio)

add a new folder called static
add lu.jpg to new static folder.

run collect static,to have django collect all static files and copy them to one folder.

update settings.py to point to STATIC_ROOT.

add load static (at the top) and image tag to home.html we had to load the static up at the top,

    load up the following

        Bootstrap - https://getbootstrap.com/docs/4.4/getting-started/download/
        Jquery - https://jquery.com/download/
        PopperJs - https://popper.js.org/ couldn't find file had to copy popper.min.js file from node.js pre-existing module

npm i @popperjs/core

update js script tags at the bottom of home.html

place bootstrap, popper, jquery, css in static folder then static collect/copy to static folder inside of jobs

the below was pasted in home.html after row but before col-4

on line 75

```
            <h1>All my jobs</h1>

    {% for job in jobs.all %}

    {{ job.summary }}

   <br>

    {% endfor %}

```

---

    next up

    class based views
    authentication
    Rest API's

    deploy
    digital ocean/postgres
    aws
    heroku/postgres
    python

    nick@zappycode.com

    deployment ideas from python event 2017 video 5 deployment options

    #1
    NGrok - https://ngrok.com/download + directions

cd into code/practice/practice-python  
./ngrok authtoken 1XTxsRKP8XyxvaJigX9XFXU2FvK_4dqzLxNRJHBz8A3aoPC85

added 'ngrok url' and 'localhost' to allowed hosts in settings.py
