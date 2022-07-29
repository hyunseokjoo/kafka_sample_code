# cluster(zookeeper 1 , broekr 3)을 구축하여 sample 만들기 
### Architecture
- payment producer가 application으로 생각하고 간단한 payment 내용 만들어 topic에 send하기 
- detect fraud에서 메세지 consume하여 데이터 분기 나눠 Fraud와 Legit 토픽으로 보내기 
- processor fraud, legit에서 메세지 받아 로그 남기기
![1](https://user-images.githubusercontent.com/49854618/179385251-ec11cc6d-e9a7-4c1f-94fc-c855e1d954d0.png)

### 사용법 정리 
- docker에 container올리기 
```bash
docker compose up -d
```
- topic 만들기
```bash
docker exec -it kafka kafka-topics --bootstrap-server=localhost:19091 --create --topic payments --partitions 3 --replication-factor 2
docker exec -it kafka kafka-topics --bootstrap-server=localhost:19092 --create --topic legit_payments --partitions 3 --replication-factor 2
docker exec -it kafka kafka-topics --bootstrap-server=localhost:19093 --create --topic fraud_payments --partitions 3 --replication-factor 2
```

- python 코드 실행
```bash 
python producer_payment.py # 결제 정보 생성 코드
python detectro_fraud.py  # 이상 감지 알고리즘 코드
python processor_fraud.py # 이상 감지 시 처리하는 코드
python processor_legit.py # 정상 결제 시 처리하는 코드 
```