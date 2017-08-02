name := "KafkaWordCount"

libraryDependencies ++= Seq(
    "org.apache.spark" % "spark-streaming_2.10" % "1.4.1",
    "org.apache.spark" % "spark-streaming-kafka_2.10" % "1.4.1"
)
