#!/bin/bash 

NAME="elite_schedule"
DJANGODIR=/home/ubuntu/core
SOCKFILE=/home/ubuntu/env/run/gunicorn.sock 
USER=ubuntu
GROUP=ubutnu 
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=core.settings.development
DJANGO_WSGI_MODULE=core.wsgi 
echo "Starting $NAME as `whoami`"

# Activate the virtual environment

cd $DJANGODIR
source /home/ubuntu/env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist 

RUNDIR$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR 

 # Start your Django Gunicorn 

# Programs meant to be run under supervisor should not daemonize themselves 

exec gunicorn ${DJNAGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user= $USER --group=$GROUP \
    --bind=unix:$SOCKFILE \
    --log-level=debug \
    --log-file=-


# Make file executable sudo chmod u+x gunicorn_start.bash