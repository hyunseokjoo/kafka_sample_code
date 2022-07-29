/*
kafka to spark-streaming 예제 입니다.
Structured Streaming을 사용하여 작성한 코드 입니다.
*/

import org.apache.spark.SparkConf
import org.apache.spark.sql.{SparkSession}
import org.apache.spark.sql.functions._
import org.apache.spark.sql.streaming.Trigger
import org.apache.spark.sql.types.{IntegerType, StringType, StructType}

object KafkaStreaming extends App {
  // sparkSession-conf 생성
  val conf = new SparkConf()
    .setAppName("Spark-Kafka")
    .set("spark.streaming.stopGracefullyOnShutdown", "true")

  // session 실행
  val spark = SparkSession.builder()
    .master("local")
    .config(conf)
    .getOrCreate()

  // kafka 정보 받아오기
  val df = spark.readStream
    .format("kafka") // format kafka
    .option("kafka.bootstrap.servers", "localhost:9091,localhost:9092,localhost:9093") // bootstrap server 설정 여러 개일 때 ','로 구분
    .option("subscribe", "order") 
    .option("startingOffsets", "earliest")
    //.option("endOffsets", "latest")
    //.option("value.deserializer", "StringDeserializer")
    .load()

  // key, value, topic등 내용이 들어오게 되고 
  // value에 메세지가 내용이 들어 오게 됨
  val personStringDF = df.selectExpr("CAST(value AS STRING)")

  // schema 구성 데이터의 맞게
  val schema = new StructType()
    .add("DATE",StringType)
    .add("TIME",StringType)
    .add("USER_ID",StringType)
    .add("CUSTOMER_TYPE",StringType)
    .add("MENU",StringType)
    .add("PRICE",IntegerType)

  // value를 json으로 변형 및 모든 데이터 select
  val personDF = personStringDF.select(from_json(col("value"), schema).as("data"))
    .select("data.*")

  // 받아온 데이터 console로 출력
  println(personDF)
  personDF.writeStream
    .format("console")
    .outputMode("append")
    .trigger(Trigger.ProcessingTime("20 seconds"))
    .start()
    .awaitTermination()
}
