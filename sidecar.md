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

    ###difference between a project and an app in django
    project can contain many apps (and apps can be in more than one project, in theory)

django-admin startapp jobs

    add 'jobs' app to 'installed-apps' in settings.py

###url paths

    update settings.py

    update urls.py

    update views.py
