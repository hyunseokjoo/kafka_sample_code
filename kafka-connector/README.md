docker에 container 올리기
```bash
docker-compose up -d
```
confluent-hub에서 jdbc connector 다운로드하고 broker서버에 압축풀기 
https://www.confluent.io/hub/confluentinc/kafka-connect-jdbc

connect 서버 properties에 plugin-path에 압축푼 경로 정해주기
```bash 
vi ./etc/kafka/connect-distributed.properties
plugin-path=/usr/share/java
```

DB 만들기
```bash
docker exec -it mysql bash   

mysql -u root -p
Enter password : admin
```

```bash
CREATE DATABASE IF NOT EXISTS source;

USE source;

DROP TABLE source_table;

CREATE TABLE source_table(
    testid varchar(40),
    testtext varchar(50)
);

CREATE DATABASE IF NOT EXISTS sink;

USE sink;

DROP TABLE sink_table;

CREATE TABLE sink_table(
    testid varchar(40),
    testtext varchar(50)
);
```

AllowPublicKeyRetrieval 오류 시 
allowPublicKeyRetrieval = true 로 변경

order-topic 생성하기
```bash
docker exec -it {broker_host_name} kafka-topics --bootstrap-server {broker_server 주소} --create --topic {토픽명}
docker exec -it broker kafka-topics --bootstrap-server broker:9092 --create --topic order
```
ksql 서버 실행하기 
```bash
docker exec -it ksqldb-cli ksql {ksqldb서버 주소}
docker exec -it ksqldb-cli ksql http://ksqldb-server:8088
```
Source Connector 만들기
```bash
CREATE SINK CONNECTOR mysqlSinkConnector WITH(
    "connector.class"='io.confluent.connect.jdbc.JdbcSinkConnector',
    "connection.url"='jdbc:mysql://localhost:3306/sink',
    "connection.user"='root',
    "connection.password"='admin',
    "auto.create"='true',
    "auto.evolve"='true',
    "delete.enabled"='false',
    "topics"='example_topic_sink',
    "tasks.max"='1'
);
```