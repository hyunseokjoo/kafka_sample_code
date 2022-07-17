from ensurepip import bootstrap
from kafka import KafkaProducer 

# producer 생성 
producer = KafkaProducer(bootstrap_servers = ['localhost:9092'])
# 메세지 보내기 message는 byte형식으로 보내는 것을 익숙해져야한다.
producer.send('first-topic', b'hello world from python')
# producer제거 
producer.flush()