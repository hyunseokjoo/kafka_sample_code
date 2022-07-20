# confluent-platform 사용법
### 개발환경 
- ubuntu 20.04 LTS
- java 11
- confluent-platform
### confluent-platform 설치하기
java version 확인
```bash
java --version
```
ubuntu 업그레이드
```bash 
sudo apt-get update && sudo apt-get upgrade
```
java 설치
```bash
sudo apt-get install openjdk-11-jdk
```
[confluent platform 설치 주소](https://www.confluent.io/ko-kr/get-started/?product=software)
software에 들어가 tar 링크 주소 복사
```bash
wget https://packages.confluent.io/archive/7.1/confluent-7.1.2.tar.gz
```
압출풀기
```bash
tar -xvf confluent-7.1.2.tar.gz
```
confluent 홈 환경 변수 만들기 
```bash
export CONFLUENT_HOME=~/confluent-7.1.2
export PATH=$CONFLUENT_HOME/bin:$PATH
```
confluent platform 실행 하기 
```bash
confluent local services start
```
confluent platform 서버 확인하기 
http://localhost:9021/clusters 주소로 접속하여 확인 

confluent platform 서버 다운 
```bash 
confluent local services stop
```