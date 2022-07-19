"""
@author : 주현석
@date : 2022.07.18
@description : stream, table로 만든 topic consume하기
1. ksql에서 show streams, show tables로 topic확인하기
2. 아래 topic_name 변수를 변경하여 처리
"""

from kafka import KafkaConsumer
import json

TOPIC_NAME = "ORDERGROUPBYMENU"
brokers = ["localhost:9092"]
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=brokers)

for message in consumer:
    msg = json.loads(message.value.decode())
    print(f"[MESSAGE] Consume orderGroupByMenu message : {msg}")

