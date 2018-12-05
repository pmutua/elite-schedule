# # FROM python:3.5
# FROM phusion/baseimage 
# # See all logs in console 
# # ENV PYTHONUNBUFFERED 1

# RUN mkdir /elite_schedule 

# WORKDIR /elite_schedule_api 

# COPY requirements* /elite_schedule_api/

# COPY django/ /elite_schedule_api/django

# # COPY . /elite_schedule_api/

# COPY scripts /elite_schedule_api/scripts

# RUN mdir /var/log/elite_schedule_api/

# RUN touch /var/log/elite_schedule_api/elite_schedule_api.log


# RUN apt-get -y update 
# RUN aptget install -y \
#     nginx \
#     postgresql-client \
#     python3 \
#     python3-pip

# RUN pip3 install virtualenv 
# RUN virtualenv /elite_schedule_api/scripts/pip_install.sh /elite_schedule_api

# # collect the static files
# RUN bash /elite_schedule_api/scripts/collect_static.sh /elite_schedule_api

# COPY nginx/elite_schedule_api.conf /etc/nginx/sites-available/elite_schedule_api.conf
# RUN rm /etc/nginx/sites-enabled/*
# RUN ln -s /etc/nginx/sites-available/elite_schedule_api.conf /etc/nginx/sites-enabled/elite_schedule_api

# COPY runit/nginx /etc/service/nginx
# RUN chmod +x /etc/service/nginx/run 



# # RUN pip install -r requirements/base.txt 

# # Run the app.  CMD is required to run on Heroku
# # $PORT is set by Heroku
# # CMD python manage.py runserver 0.0.0.0:$PORT
# # CMD python manage.py runserver 0.0.0.0:$PORT 



FROM python:3.6

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app  # specifying the working dir inside the container

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy current dir's content to container's WORKDIR root i.e. all the contents of the web app
COPY . .