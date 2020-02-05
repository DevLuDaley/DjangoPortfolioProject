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
