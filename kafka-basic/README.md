# cluster(zookeeper 1, broker 1)를 구성하여 메세지 보내고 받기 

### 목표 및 순서
- docker파일 작성
- docker-compose를 사용하여 cluster올리기
- topic 생성
- Producer code 생성
- Consumer code 생성
- python code 실행해서 메세지 보내고 받기


### Docker파일 작성
- docker desktop이나 docker linux가 다운로드 되어있어야 함
- 실습을 위해 docker-compose - zookeeper 1 개, broker 1 개 작성
- docker-compose.yml 파일에서 확인가능

### docker-compose를 사용하여 cluster올리기 
'''bash
docker-compose up -d
'''

### Kafdrop화면 확인하기
docker 파일에서 설정한 주소 localhost:9000로들어가면 화면을 볼 수 있다.



### Topic 생성
아래와 같이 입력하면 Topic을 만들 수 있다.


### Producer code 생성 
- cluster-producer.py 참조

### consumer code 생성
- cluster-consumer.py 참조 

### python code 실행해서 메세지 보내고 받기

kafdrop 해당 topic에 들어가면 메세지도 볼 수 있다.