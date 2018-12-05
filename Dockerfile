FROM python:3.6.2 

ENV PYTHONUNBUFFERED 1

RUN mkdir /elite_schedule 
WORKDIR /elite_schedule_api 
COPY . /elite_schedule_api/

RUN pip install -r requirements/base.txt 

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
# CMD python manage.py runserver 0.0.0.0:$PORT
CMD python manage.py runserver --settings=core.settings.development 0.0.0.0:$PORT 



