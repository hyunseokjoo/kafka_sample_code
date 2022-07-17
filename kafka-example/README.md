### cluster(zookeeper 1 , broekr 3)을 구축하여 sample 만들기 
Architecture
- payment producer가 application으로 생각하고 간단한 payment 내용 만들어 topic에 send하기 
- detect fraud에서 메세지 consume하여 데이터 분기 나눠 Fraud와 Legit 토픽으로 보내기 
- processor fraud, legit에서 메세지 받아 로그 남기기
![1](https://user-images.githubusercontent.com/49854618/179385251-ec11cc6d-e9a7-4c1f-94fc-c855e1d954d0.png)

### 선행 작업 
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




---
출처 패스트 캠퍼스


