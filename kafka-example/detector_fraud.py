from ensurepip import bootstrap
from kafka import KafkaConsumer, KafkaProducer
import json

PAYMENT_TOPIC = "payments"
FRAUD_TOPIC = "fraud_payments"
LEGIT_TOPIC = "legit_payments"

brokers = ["localhost:9091", "localhost:9092", "localhost:9093"]

consumer = KafkaConsumer(PAYMENT_TOPIC, bootstrap_servers=brokers)
producer = KafkaProducer(bootstrap_servers=brokers)

def is_suspicious(transactions):
    if transactions["PAYMENT_TYPE"] == "BITCOIN":
        return True
    return False

for message in consumer:
    msg = json.loads(message.value.decode()) # utf-8을 python code로 decode
    topic = FRAUD_TOPIC if is_suspicious(msg) else LEGIT_TOPIC # True이면 FRAUD_TOPIC False이면 LEGIT_TOPIC
    producer.send(topic, json.dumps(msg).encode("utf=8")) # 조건에 따라 맞게 Producer로 send
    print(topic, is_suspicious(msg), msg["PAYMENT_TYPE"])