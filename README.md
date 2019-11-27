# django-react-boilerplate




# docker 

    docker-compose  -f .\docker-compose-local.yml build
    docker-compose  -f .\docker-compose-local.yml up -d
    docker-compose  -f .\docker-compose-local.yml run djangoreact python manage.py migrate
    docker-compose  -f .\docker-compose-local.yml run djangoreact python manage.py createsuperuser --username north --email abc@abc.com