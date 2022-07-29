# Kafka 연습 및 sample 코드
description : Kafka연습 환경과 sample코드 입니다.
---
- 환경 만드는 법
- Kafka 기본 서버 
```bash
cd kafka-basic
docker-compose up -d
```
- kafka 클러스터 서버 
```bash
cd kafka-example
docker-compose up -d
```
- kafka ksqldb 서버 
```bash 
cd kafka-ksqldb
docker-compose up -d
``` 
- kafka to spark streaming 서버
```bash 
cd kafka-streaming
docker-compose up -d
```
- kafka streams 서버 
```bash 
cd kafka-streams
docker-compose up -d
```

```bash 
docker exec -it kafka2 kafka-topics --bootstrap-server broker:9092 --create --topic order --replication-factor 1 --partitions 3
```
