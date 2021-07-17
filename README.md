# DPhi Assignment for SDE 1 - Backend

## Objective -

Create an online nursery marketplace API where users can signup, login, view, and order plants available in different nurseries.

## Application overview -

- Users should be able to signup and see all the plants available from different nurseries. They should also be able to add the plants to their cart and place orders.
- Nurseries should be able to signup and add plants to their shop. They should also be able to view orders placed by users.

## Live Links -

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/4ccb52febc632cc66dfd?action=collection%2Fimport#?env%5BDPhi%20Task%5D=W3sia2V5IjoiYmFzZV91cmwiLCJ2YWx1ZSI6Imh0dHBzOi8vbnVyc2VyeS1kamFuZ28uaGVyb2t1YXBwLmNvbSIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoidG9rZW4iLCJ2YWx1ZSI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUowYjJ0bGJsOTBlWEJsSWpvaVlXTmpaWE56SWl3aVpYaHdJam94TmpJMk5qQXpPRFF5TENKcWRHa2lPaUk0TURrek1UZGpOMkppWldRMFpEaGlZakpoTW1ZMk1qWmxPVFkzWkdNMk5TSXNJblZ6WlhKZmFXUWlPakY5LkY0YmNnQVVLZXNkMVhIcW1EcUVVMkhxQjdPUmY1azBGX3phYS1qU3YwV1UiLCJlbmFibGVkIjp0cnVlfV0=)

> See Demo Video [here](https://share.getcloudapp.com/7Kuo9KEj)

- **Postman Collections:** [https://www.getpostman.com/collections/4ccb52febc632cc66dfd](https://www.getpostman.com/collections/4ccb52febc632cc66dfd)
- **API Documentation:** [https://documenter.getpostman.com/view/10608582/TzmCgY2K](https://documenter.getpostman.com/view/10608582/TzmCgY2K)
- **Heroku Hosted Link:** [https://nursery-django.herokuapp.com/](https://nursery-django.herokuapp.com/)

## Demo Credentials -

**Username:** admin
**Email:** admin@gmail.com
**Password:** admin

## Setup Instructions

First make sure that you have the following installed.

- Python 3 and virtualenv

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
