# English Tutor - Backend

Backend system for recommending English-speaking exercises, built on [DRF](https://www.django-rest-framework.org/)

## Requirements

##### For running


- [Python](https://www.python.org/downloads/)

## Clone

* Use `git clone` to clone the repo
```bash
git clone git@github.com:FumaxIN/english-tutor.git
```

## Run

* Create a virtual environment
```bash
python -m venv ./venv
source ./venv/bin/activate
```

* Install the requirements
```bash
  pip install -r requirements.txt
```
* Migrations
```bash
python manage.py migrate
```
* Apply fixtures to load data
```bash
python manage.py loaddata tutor/fixtures/*
```
* Run server and start celery in a new terminal
```bash
python manage.py runserver
```

## Swagger-Doc

The base url i.e, the root endpoint `/` will redirect to the swagger documentation.

### Generate Exercise

* Get top errors by `user_id`
    ```
    GET: /api/generate-exercise
    ```
    Params:
    * `?user_id=dcc44822-4b8d-43cf-be83-fb510ea07bae` [Required]
    * `?top_n_errors=3` [Optional]
    * `?last_n_days=7` [Optional]
