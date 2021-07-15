# DPhi Assignment for SDE 1 - Backend

## Objective -
Create an online nursery marketplace API where users can signup, login, view, and order plants available in different nurseries.

## Application overview - 
- Users  should be able to signup and see all the plants available from different nurseries. They should also be able to add the plants to their cart and place orders.
- Nurseries should be able to signup and add plants to their shop. They should also be able to view orders placed by users.

## Setup Instructions

First make sure that you have the following installed.

* Python 3 and virtualenv

Now do the following to setup project

```bash
# assuming that the project is already cloned.

cd nursery

# one time
virtualenv -p $(which python3) pyenv

source pyenv/bin/activate

# one time or whenever any new package is added.
pip install -r requirements/dev.txt

# update settings
cp src/nursery/settings/local.sample.env src/nursery/settings/local.env

# generate a secret key or skip(has a default value) and then replace the value of `SECRET_KEY` in environment file(here local.env)
./scripts/generate_secret_key.sh

# update relevant variables in environment file

# run migrate
cd src
python manage.py migrate
```

To access webserver, run the following command

```bash
cd src
python manage.py runserver
```
