"""
@author : 주현석
@date : 2022.07.18
@description : ksql에서 사용하는 기본적인 sql형태 정리
"""

-- stream으로 들어온 값 처음 부터 출력하는 설정
set 'auto.offset.reset' = 'earliest';

-- ksql에서 topic 리스트 조회 
list topics;
show topics;

-- ksql에서 stream 리스트 조회
list streams;
show streams;

-- 카프카 topic으로 들어온 데이터 보기 
PRINT 'kafka_topic' FROM BEGINNING;

-- log처음 부터 조작하기 
SET 'auto.offset.reset' = 'earliest';

-- ksql-Stream 생성
CREATE STREAM order_stream(date varchar, time varchar, customer_type varchar, menu varchar, price int) WITH (kafka_topic='order', value_format='json',partitions=1);

-- ksql-Stream 생성 with select  
-- stream에서는 group by 를 사용할 수 없는 듯
--CREATE STREAM order_stream_count as select menu, count(*) from order_stream group by menu; 
CREATE STREAM order_stream_sel_platinum as select * from order_stream where customer_type='PLATINUM';  

-- ksql-Table 만들기 
-- table을 만들 때는 꼭 primary key를 설정하여야 한다.
CREATE TABLE order_table(date varchar, time varchar, customer_type varchar, menu varchar primary key, price int) WITH (kafka_topic='order', value_format='json',partitions=1);

-- ksql-Table 생성 with select  
CREATE TABLE order_table_groupby_menu as select menu, sum(price) from order_stream group by menu;  
CREATE TABLE order_table_groupby_menu as select customer_type, count(*) from order_stream group by customer_type;  
-- window 함수 test용 query 1시간 안에 주문이 3개가 넘는 것을 가져오는 쿼리
create table order_window_1hour as select menu, count(*) from order_stream window tumbling(size 1 hour) group by menu having count(*) > 3 emit changes;

-- ksql-stream push query(실시간 consume)
-- EMIT CHANGES 절을 추가하면 push query(실시간으로 consume하게)하게 된다.
SELECT date, time, menu, price FROM order_stream EMIT CHANGES;
SELECT date, time, menu, price FROM order_table EMIT CHANGES;

-- EMIT CHANGES 절을 추가하지 않으면 pull query가 된다.
SELECT date, time, menu, price FROM order_stream;
SELECT date, time, menu, price FROM order_table;



--삭제--
--stream 삭제
drop stream {stream_name}

--table 삭제
drop table {table_name}
