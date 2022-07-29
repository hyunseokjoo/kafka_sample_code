# confluent-platform 사용법
confluent-platform이란? 
- confluent에서 제공하는 서비스를 하나의 설치 파일로 설치하여 사용하는 package 서비스 
- confluent-platform 를 설치하면 kafka, ksqldb, connector, schema registry등을 사용할 수 있음
- confluent-hub에서 connector같은 정보를 cli로 쉽게 다운로드 가능 
- confluent-control-centor라는 web ui를 제공하여 손쉽게 kafka cluster 모니터링 할 수 있음
- confluent community 버전으로 사용하면 무상으로 사용할 수 있음
### 개발환경 
- ubuntu 20.04 LTS
- java 11
- confluent-platform
### confluent-platform 설치하기
java version 확인
```bash
java --version
```
### ubuntu 업그레이드
```bash 
sudo apt-get update && sudo apt-get upgrade
```
### java 설치
```bash
sudo apt-get install openjdk-11-jdk
```
[confluent platform 설치 주소](https://www.confluent.io/ko-kr/get-started/?product=software)
### software에 들어가 tar 링크 주소 복사
```bash
wget https://packages.confluent.io/archive/7.1/confluent-7.1.2.tar.gz
```
### 압출풀기
```bash
tar -xvf confluent-7.1.2.tar.gz
```
### confluent 홈 환경 변수 만들기 
```bash
export CONFLUENT_HOME=~/confluent-7.1.2
export PATH=$CONFLUENT_HOME/bin:$PATH
```
### 자신이 사용할 툴 config 파일 수정 
etc폴더에 kafka, connector, ksqldb 등 설정을 할 수 있음

### confluent platform 실행 하기 
```bash
confluent local services start
```
### confluent platform 서버 확인하기 
http://localhost:9021/clusters 주소로 접속하여 확인 

### confluent platform 서버 다운 
```bash 
confluent local services stop
```