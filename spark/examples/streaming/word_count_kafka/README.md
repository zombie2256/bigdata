Spark streaming using Kafka

```
sbt package
spark-submit --class "KafkaWordCount" --jars spark-streaming-kafka-assembly_2.10-1.5.2.jar target/scala-2.10/kafkawordcount_2.10-0.1-SNAPSHOT.jar
```
