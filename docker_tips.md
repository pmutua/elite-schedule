# High level steps
- Install and start Docker compose
- Setup project – presume you already have a Django project.
- Create Dockerfile(s) and docker-compose.yml
- Build service images – docker-compose build
- Create database and database migrations – docker-compose run web python manage.py migrate
- Start services containers – docker-compose up
- View in browser http://127.0.0.1