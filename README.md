### Make requirements.txt

```bash
pip freeze > requirements.txt
```

delete psycopg2-binary from requirements.txt, psycopg2 installed in Dockerfile


### Docker

ossec-rest_api_1 - default api container name

ossec-rest_postgres_1 - default postgres container name

```bash
docker-compose up
```

rebuild:

```bash
docker container rm ossec-rest_api_1 && docker image rm ossec-rest_api
```


### Apply ossec data

connect into container:

```bash
docker ps
docker exec -it ossec-rest_api_1 /bin/sh
```

apply ossec sql: 

```bash
PGPASSWORD=ossec psql -h ossec-rest_postgres_1 -p 5432 -d ossec -U ossec -f ossec.sql
PGPASSWORD=ossec psql -h ossec-rest_postgres_1 -p 5432 -d ossec -U ossec -f ossec_ext.sql
```

apply test data:

```bash
python3 manage.py shell < ossec_test_data.py
```

### Clear .pyc and pycache

```bash
find . -name ".pyc" -exec rm -rf {} \;
find . -name "__pycache__" -exec rm -rf {} \;
```
