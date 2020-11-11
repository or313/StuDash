# !/bin/bash -ex
sudo -n dnf install -y pipenv
cd /vagrant

# Install dependencies with Pipenv
pipenv sync


# Remove comment when django is installed and running
# pipenv run python manage.py migrate


# Remove comment when django is installed and running
# nohup pipenv run python manage.py runserver 0.0.0.0:8000 &