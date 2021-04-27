#!/bin/sh

set -e


etc/spark/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.3,org.apache.spark:spark-sql-kafka-0-10_2.11:2.2.3 ./src/case_study/process/consumer.py
