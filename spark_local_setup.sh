#!/bin/sh

set -e

wget http://mirror.cc.columbia.edu/pub/software/apache/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz
tar -xvzf spark-2.4.7-bin-hadoop2.7.tgz

mkdir etc
mkdir etc/spark
cp -r spark-2.4.7-bin-hadoop2.7/* etc/spark/
cp etc/spark/conf/spark-env.sh.template etc/spark/conf/spark-env.sh

export PYSPARK_PYTHON="python3.7"
export PYSPARK_DRIVER_PYTHON="python3.7"

cp etc/spark/conf/log4j.properties.template etc/spark/conf/log4j.properties