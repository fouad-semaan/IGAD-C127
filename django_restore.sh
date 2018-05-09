#!/usr/bin/env bash

# set -x

source ~/Envs/geonode/bin/activate

pushd $(dirname $0)

case $1 in
	"backup-file")
		case $2 in
                        "")
                                echo "Missing 'backup-file <backup-file>' path!"
                                ;;
			*)
				echo "Starting Restore from $2"
				DJANGO_SETTINGS_MODULE=igad_geonode.settings python -W ignore manage.py restore -c backup/settings.ini --backup-file=$2
				# DJANGO_SETTINGS_MODULE=igad_geonode.settings python -W ignore manage.py migrate_baseurl -f --source-address=igad.geo-solutions.it --target-address=igad-dev.geo-solutions.it
				;;
		esac
		;;
	*)
		echo "Missing 'backup-file' parameter!"
		;;
esac

exit 0
