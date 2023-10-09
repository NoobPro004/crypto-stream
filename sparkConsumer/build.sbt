name := "sparkConsumer"

version := "1.0-RELEASE"

scalaVersion := "2.12.18"

libraryDependencies ++= {
  val sparkVersion = "3.2.4"
  val cassandraConnectorVersion = "2.4.3"
  Seq(
    "org.apache.spark" %% "spark-core" % sparkVersion % "provided",
    "org.apache.spark" %% "spark-sql" % sparkVersion % "provided",
    "com.datastax.spark" %% "spark-cassandra-connector" % cassandraConnectorVersion
  )
}