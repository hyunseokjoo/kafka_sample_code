from ensurepip import bootstrap
from kafka import KafkaProducer
import csv
import json
import time

brokers = ["localhost:9091"]
producer = KafkaProducer(bootstrap_servers = brokers)

topicName = "yourTopic"

with open("./yourPath/read.csv", "r") as file:
    reader = csv.reader(file)
    headings = next(reader)

    for row in reader:
        producer.send(topicName, json.dumps(row).encode("utf-8"))
        print(row)
        time.sleep(1)