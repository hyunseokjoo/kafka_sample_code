/*
spark 홈페이지에 있는 Dstream 형식으로
word Count 하는 Spark Streaming 예제

Dstream의 특징
- spark 기존 API
- RDD 기반
- Micro 배치 방식으로만 작동
- 이벤트 시간 기준으로 처리 지원 X

RDD기반이기 때문에 보통 사용하지 않고,
Streaming은 Structured Streaming으로 사용을 한다.
*/

package spark_streaming_home_demo

import org.apache.spark.SparkConf
import org.apache.spark.streaming.{Seconds, StreamingContext}

object streaming_dstream_wordcount extends App {
  val conf = new SparkConf().setMaster("local[2]").setAppName("NetworkWordCount") // local에 2개의 코어를 가지고 spark를 돌린다는 의미
  val ssc = new StreamingContext(conf, Seconds(1)) // 1초 단위로 Streaming한다는 의미

  val lines = ssc.socketTextStream("localhost", 9999) // Dstream socket이 localhost:9999를 바라봄
  val words = lines.flatMap(_.split(" ")) // " " 띄어씌기 단위로 나누기

  val pairs = words.map(word => (word, 1)) // (key, value) 형식으로 변경
  val wordCounts = pairs.reduceByKey( _ + _ )
  wordCounts.print()

  ssc.start() // Streaming 시작하기
  ssc.awaitTermination() // 들어오는 것을 기다리는 문구
}


