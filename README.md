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


## Ideal Database

For demonstration purpose, I have simply used SQLite.

When it comes to ideal database, we need to consider 2 factors:
* The data will be ingested from throughout the world.
* This is a part of real time conversation. So processing huge data with low latency is a must.

Considering the above factor, there are different approaches that can be taken:

**NoSQL approach - MongoDB**
* Using NoSQL database like MongoDB ensures very quick reads with its read-preference configuration making it suitable for real time data.
* Horizontal scaling is easier in MongoDB.
* The flexibility of storing unstructured data in MongoDB can be both an advantage and disadvantage, as it can lead to inconsistencies and violating ACID properties.

**Hybrid approach - Postgresql + Redis Cache**
* Using SQL database like Postgresql ensures that the data is stored in a structured format.
* Postgresql gives the flexibility to store JSON as well for semi-structured data.
* Postgresql is excellent for handling complex queries.
* Postgresql's concurrency control can be used in real time data processing.  
* Redis cache can be used to store the frequently accessed data.
* Real time data from conversation can be stored in Redis cache and then flushed to Postgresql in a batch.
* This way, we can query from Redis cache with low latency to generate suitable exercises.

**Cassandra**
* Cassandra is a distributed database that can handle large amounts of data across many servers.
* I am not very well versed with Cassandra, but with its hybrid approach, it brings the best of both worlds(SQL and NoSQL).
* AFAIK, Cassandra has a node system with P2P architecture with data replication, ensuring no point of failure.


Among the above approaches, I would prefer the **Hybrid approach of Postgresql + Redis Cache**.<br /> 
This is because, the data is structured and can be queried easily. Redis cache can be used to store frequently accessed data and Postgresql can be used to store the data in a structured format.<br />
This way, we can ensure that the data is consistent and can be queried easily, along with low latency from Redis Cache for real time data processing.