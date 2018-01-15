#!/usr/bin/env bash

# set -x

source ~/Envs/geonode/bin/activate

pushd $(dirname $0)

case $1 in
	"backup-dir")
		case $2 in
			*)
				echo "Starting Backup to $2"
				DJANGO_SETTINGS_MODULE=igad_geonode.settings python -W ignore manage.py backup --backup-dir=$2
				;;
			"")
				echo "Missing 'backup-dir <backup-dis>' path!"
				;;
		esac
		;;
	*)
		echo "Missing 'backup-dir' parameter!"
		;;
esac

exit 0
