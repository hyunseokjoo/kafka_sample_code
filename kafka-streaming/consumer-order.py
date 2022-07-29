"""
@author : 주현석
@date : 2022.07.18
@description : order topic Consumer-Test용 입니다. pub/sub확인용 입니다.
사용법 
1. python producer-order.py
2. python consumer-order.py
"""

from kafka import KafkaConsumer
import json

TOPIC_NAME = "order"
brokers = ["localhost:9092"]
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=brokers)

for message in consumer:
    msg = json.loads(message.value.decode())
    menu = msg["MENU"]
    price = msg["PRICE"]
    print(f"[MESSAGE] Consume order message : {menu} - {price}")

