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
