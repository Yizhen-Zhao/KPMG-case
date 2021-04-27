# Kafka + Spark Streaming Data Processing

Simple case study of using Kafka and Spark to do some data processing

Table of Contents
=================

   * [case-study](#case-study)
      * [Table of Contents](#table-of-contents)
      * [Case Requirements](#case-requirements)
      * [Project Status](#project-status)
      * [Project Documentation](#project-documentation)
         * [Project structure](#project-structure)
         * [Project design](#project-design)
         * [Requirements](#requirements)
         * [Development](#development)
            * [Start Kafka, Zookeeper, Mysql servers](#experiment)
            * [Start Kafka producer](#start-kafka-producer)
            * [Start Spark streaming consumer](#start-spark-streaming-consumer)
            * [Validate result in database](#validate-result-in-database)
      * [Future Work](#future-work)
      
      
## Case Requirements
Make a Docker container setup that provides a data processing service using a cluster of machines. The environment should have the following:
 
- A Kafka as a pub/sub system and a Spark node/cluster for working with Kafka. 
  - How to stand out: have it well composed, run on a PaaS, run in a container manager/orchestrator
- Load some data (any data) into a Kafka topic 
  - How to stand out: Use a solid way to load data (e.g. Apache NiFi), reason about data formats and how to manage that, load an actual online streaming source (e.g. Twitter)
- Consume the data from the Kafka topic and do some arbitrary transformation (like a word count)
  - How to stand out: spend effort in making it a streaming application, make an impressive transformation
- Write results into a database
  - How to stand out: reason about which database, create your own Docker image
  
## Project Status
- Implemented:
  - Kafka, Zookeeper, Mysql are started by docker-compose command.
  - Data processing logic:
    - Producer: Send some random data to Kafka topic
    - Consumer: Load data from Kafka topic and do word count processing via Spark.
    - Export: Write data to database (i.e. Mysql)
- Unfinished:
  - Using dockerfile to start the data processing service and included in docker-compose.yaml
  
## Project Documentation 

### Project structure

```
|-- case-study
    |-- data
    |-- src
        |-- case_study
            |-- process
                |-- producer.py
                |-- consumer.py
    |-- mysql
    |-- docker-compose.yaml
    |-- run_spark.sh
    |-- spark_local_setup.sh
```

- data: sample data used to send into Kafka topic
- src: source folder include data processing logic
- mysql: dockerfile that used to build docker image for create mysql service
- docker-compose.yaml: start kafka + zookeeper + mysql services
- run_spark.sh: start spark streaming and comsuming data in kafka topic
- spark_local_setup.sh: create spark local environment in order to submit spark job (because of the 
`unfinished` task mentioned above)

### Project design
The project design is shown below: 

Docker helps us to start the necessary services (Kafka, Zookeeper and MySQL).
Then `producer.py` script read data from `sample_data.json` and send data into Kafka topic: `kpmg_topic`.
Next in `consumer.py` we use pyspark to consume data in Kafka topic and do some transformation (i.e. word count).
Finally, write the processed data into MySQL database.

![alt text](./data/case_study.png?raw=true)
### Requirements

Needed packages:
- Please see the file `requirements.txt`

Spark env:
- In order to start spark job, we need spark environment. Because of the unfinished task, I created a script
to setup spark env.
- Steps:
  - go into the project folder and execute `spark_local_setup.sh`
  
  ``$ ./spark_local_setup.sh``
  
  After execute the script, it will download the spark package to your local project. 
  
### Development
Here are the steps to start and validate the project. Starting the necessary services and executing data processing job, finally check 
if data exist in database.

#### Start Kafka, Zookeeper, Mysql servers
First we need to start those services, we use `docker-compose up` to help us start all services.

```shell script
$ docker-compose pull zookeeper kafka
$ docker-compose build
$ docker-compose up -d
```

#### Start Kafka producer
Then we need to start Kafka producer to send data to Kafka topic, it will read data from our sample data
file and send to `kpmg_topic` topic. In producer, it has been set to iterate and keep sending data to Kafka topic. 

```shell script
$ python3 src/kpmg_case/process/producer.py
```

#### Start Spark streaming consumer
Now we could consume data that stores in Kafka topic and do data processing (i.e. word count)

```
$ ./run_spark.sh
```

#### validate result in database
Finally we can check if data has been write to database

- Check mysql docker container and go inside:
```shell script
$ docker ps  # check all running container

$ docker exec -it MYSQL_CONTAINER_ID /bin/bash
```

- Login to mysql and check data (Database user: root, password: 123456) -> (Bad practice, do not put credentials on github)
```shell script
$ mysql -u root -p123456
$ use kpmg;  # Database name
$ show tables; # Should see the table: wordCount

$ select * from wordCount;
```


## Future Work
Due to my time limit and limited knowledge about Kafka + Spark, there are some features that haven't implement yet.

- Package data processing process (producer + consumer) in a dockerfile, with spark environment. And include 
in docker-compose.yaml. Then other people don't need to worry about the environment issue (e.g. Spark setup).
- Try loading real-time data from Twitter
- More solid way of loading data, do more research about proper data format and why.
- Investigate more details about Kafka, how it works with Spark.
