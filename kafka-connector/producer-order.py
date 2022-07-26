"""
@author : 주현석
@date : 2022.07.18
@description : Order에 dummy 데이터 보내는 producer입니다.
"""

from kafka import KafkaProducer 
import datetime, pytz, time, random, json 

TOPIC_NAME = "order"
brokers = ["localhost:9092"]
producer = KafkaProducer(bootstrap_servers=brokers)

def generate_order_data():
    test_id= random.choice([0, 1, 2])
    test_text = random.choice([0, 1, 2])

    dic_test_id = ["1234", "5678", "90"]
    dic_test_text = ["test", "text", "vs"]

    choiced_test_id = dic_test_id[test_id]
    choiced_test_text = dic_test_text[test_text]

    return choiced_test_id, choiced_test_text


while True:
    choiced_test_id, choiced_test_text = generate_order_data()
    new_data = {
        "testid" : choiced_test_id,
        "testtext" : choiced_test_text,
    }
    print(new_data)
    producer.send(TOPIC_NAME, json.dumps(new_data).encode("utf-8"))
    
    time.sleep(1)

