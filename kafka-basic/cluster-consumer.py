from ensurepip import bootstrap
from kafka import KafkaConsumer

brokers = ["localhost:9091"]
consumer = KafkaConsumer("first-cluster-topic", bootstrap_servers=brokers)

for message in consumer:
    print(message)