import org.apache.spark.SparkConf
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.Seconds
import org.apache.spark.streaming.kafka.KafkaUtils

object KafkaWordCount {
    def main(args: Array[String]) {
        val conf = new SparkConf().setMaster("local[*]").setAppName("KafkaWordCount")
        val ssc = new StreamingContext(conf, Seconds(10))
        val lines = KafkaUtils.createStream(ssc, "localhost:2181","spark-streaming-consumer-group", Map("test" -> 5)).map(_._2)
        val words = lines.flatMap(_.split(" "))
        val pairs = words.map(word => (word, 1))
        val wordCounts = pairs.reduceByKey(_ + _)
        wordCounts.print()
        ssc.start()
        ssc.awaitTermination()
    }
}
