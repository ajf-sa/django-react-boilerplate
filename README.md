# django-react-boilerplate


    git clone git@github.com:alfuhigi/django-react-boilerplate.git
    cd django-react-boilerplate
    # change .env.example to .env
    pipenv shell
    pipenv install
    pipenv install --dev





# docker 

    docker-compose  -f .\docker-compose-local.yml build
    docker-compose  -f .\docker-compose-local.yml up -d
    docker-compose  -f .\docker-compose-local.yml run djangoreact python manage.py migrate
    docker-compose  -f .\docker-compose-local.yml run djangoreact python manage.py createsuperuser --username north --email abc@abc.com