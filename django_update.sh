#!/bin/bash

source ~/Envs/geonode/bin/activate

pushd $(dirname $0)

DJANGO_SETTINGS_MODULE=igad_geonode.settings python -W ignore manage.py makemigrations --merge
DJANGO_SETTINGS_MODULE=igad_geonode.settings python -W ignore manage.py makemigrations
DJANGO_SETTINGS_MODULE=igad_geonode.settings python -W ignore manage.py migrate
DJANGO_SETTINGS_MODULE=igad_geonode.settings python -W ignore manage.py collectstatic --noinput

touch igad_geonode/wsgi.py

sudo service apache2 restart

exit 0
