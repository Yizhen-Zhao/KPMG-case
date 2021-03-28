import os
from pathlib import Path
import json
from kafka import KafkaProducer, KafkaClient


class Producer:
	def __init__(self):
		self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

	def load_data_to_topic(self):
		data_path = os.path.join(
			Path(__file__).parents[3],
			f"data/sample_data.json",
		)
		with open(data_path) as f:
			data = json.load(f)
			for k in data:
				self.producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
				self.producer.send("kpmg_topic", data[k])
				self.producer.flush()
				print("message sent")


if __name__ == '__main__':
	# keep iterating input data and keep sending
	for i in range(100):
		Producer().load_data_to_topic()

