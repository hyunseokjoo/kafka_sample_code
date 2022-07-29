# Kafka-to-spark 예제 -> kafkaStreming.scala 소스 확인
### 먼저 해야하는 설치 사항 
hadoop version 확인
```bash
hadoop version
```
spark version 확인 
```
spark-submit --version
# scala 버전이 나옴 ex) 2.12.10
```
scala version 확인
```bash
scala
# spark와 맞는 버전 다운로드 
```
### docker로 kafka 올리기 
```bash 
docker-compose up -d
```
### topic 생성 
```bash 
docker exec -it kafka2 kafka-topics --bootstrap-server broker:9092 --create --topic order --replication-factor 1 --partitions 3
```
### producer message 개시
```bash 
python producer-order.py
```
### spark으로 message 받기 
```
# kafkaStreaming intellij에서 실행 하거나 jar파일 spark-submit
```

