import findspark
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
import pymysql


class KafkaStreaming:
	def __init__(self):
		findspark.init('./etc/spark')

	@staticmethod
	def _wordcount(line):
		"""Read data line by line and count words
		"""
		line = line.collect()
		for word in line:
			print(word, len(word.split(" ")))
			conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='kpmg',
								   charset="utf8")
			cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
			sql = "INSERT INTO wordCount (words, count) VALUES (%s, %s)"
			cursor.execute(sql, (word, len(word.split(" "))))
			conn.commit()

	def pyspark_consume_data(self):
		"""Start spark streaming job and consume data in Kafka topic,
		count words for each line of data and finally write to Mysql database
		"""
		# Spark context details
		sc = SparkContext(appName="PythonSparkStreamingKafka")
		ssc = StreamingContext(sc, 5)
		# Creating Kafka direct stream
		dks = KafkaUtils.createDirectStream(ssc, ["kpmg_topic"],
											{"metadata.broker.list": "localhost:9092"})
		counts = dks.map(lambda x: json.loads(x[1])).flatMap(lambda line: line.split("\n")).foreachRDD(self._wordcount)

		ssc.start()
		ssc.awaitTermination()


if __name__ == '__main__':
	KafkaStreaming().pyspark_consume_data()
