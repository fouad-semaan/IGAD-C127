#!/bin/bash

source ~/Envs/geonode/bin/activate

pushd $(dirname $0)

DJANGO_SETTINGS_MODULE=igad_geonode.settings python manage.py makemigrations --merge
DJANGO_SETTINGS_MODULE=igad_geonode.settings python manage.py makemigrations
DJANGO_SETTINGS_MODULE=igad_geonode.settings python manage.py migrate
DJANGO_SETTINGS_MODULE=igad_geonode.settings python manage.py collectstatic --noinput

touch igad_geonode/wsgi.py

sudo service apache2 restart

exit 0
