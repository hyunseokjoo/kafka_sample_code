package spark_streaming_home_demo

import org.apache.spark.sql.functions._
import org.apache.spark.sql.SparkSession

object structured_streaming extends App{

  val spark = SparkSession.builder()
    .appName("StructuredNetworkWordCount")
    .getOrCreate()

  import spark.implicits._
}
