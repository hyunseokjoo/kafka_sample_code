# KsqlDB sample code, sql
### 사용법 정리
1. docker에 container 올리기
```bash
docker-compose up -d
```
2. order-topic 생성하기
```bash
docker exec -it {broker_host_name} kafka-topics --bootstrap-server {broker_server 주소} --create --topic {토픽명}
docker exec -it broker kafka-topics --bootstrap-server broker:9092 --create --topic order
```
3. ksql 서버 실행하기 
```bash
docker exec -it ksqldb-cli ksql {ksqldb서버 주소}
docker exec -it ksqldb-cli ksql http://ksqldb-server:8088
```
4. producer-order.py로 메세지 send
```bash
python producer-order.py
```
5. ksql-basic.sql에 있는 query문으로 테스트 진행
```bash
ksql-basic.sql 확인
```
