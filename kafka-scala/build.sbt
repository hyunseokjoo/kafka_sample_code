ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "2.13.8"

// https://mvnrepository.com/artifact/io.confluent.ksql/ksqldb-udf
libraryDependencies += "io.confluent.ksql" % "ksqldb-udf" % "6.0.8"


lazy val root = (project in file("."))
  .settings(
    name := "untitled"
  )
