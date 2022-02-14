"""
__AUTHOR__="lerina"
__URL__="razafy.com"

Base templates for lean projects or nano-services

USAGE:
    python 1stRun.py

Don't forget to remove/delete 1stRun on production server
cd .. ; rm -fr demo; django-admin startproject --template=https://github.com/lerina/agileBase/archive/master.zip --extension=env demo ; cd demo; python 1stRun.py ; python manage.py runserver
"""
import subprocess

subprocess.call("python manage.py migrate", shell=True)
CMD="""echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell"""
subprocess.call(CMD, shell=True)
