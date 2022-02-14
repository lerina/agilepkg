# agiletemplate
template for django nano projects

## What do you get ?
minimal file structure

## What is it for ?
This is the common setup to host various apps and components

## Starting with the project template

You'll need Django to start.

> pip install Django 

### First time

Let Django get the project
> django-admin startproject --template=https://github.com/lerina/agileForms/archive/master.zip --extension=env demo

Set it up
> cd demo; pip install -r requirements.txt; cp sample_local.env ../local.env

Create the dev admin (admin.admin) and fire-it-up
> python 1stRun.py ; python manage.py runserver

Open the browser at http://127.0.0.1:8000/


Before working on your project please edit local.env

----


