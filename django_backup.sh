#!/usr/bin/env bash

# set -x

source ~/Envs/geonode/bin/activate

pushd $(dirname $0)

case $1 in
	"backup-dir")
		case $2 in
                        "")
                                echo "Missing 'backup-dir <backup-dis>' path!"
                                ;;
			*)
				echo "Starting Backup to $2"
				DJANGO_SETTINGS_MODULE=igad_geonode.settings python -W ignore manage.py backup -c backup/settings.ini --backup-dir=$2
				;;
		esac
		;;
	*)
		echo "Missing 'backup-dir' parameter!"
		;;
esac

exit 0
