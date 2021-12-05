#!/bin/sh -ex

python manage.py collectstatic --no-input --clear

/app/docker/wait-for-it.sh ${POSTGRES_HOST:-db}:${POSTGRES_PORT:-5432}

exec "$@"
