# Running Spark Locally using Docker Compose

### Steps to run spark job:

- Run `docker-compose up -d`

- If need to update the `spark_version` make change in Dockerfile

- After starting all the containers copy the python job to the master node on `/opt/spark/`

- Execute the master node in bash and run `./bin/spark-submit <file_name>.py`