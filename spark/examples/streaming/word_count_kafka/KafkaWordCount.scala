import org.apache.spark.SparkConf
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.Seconds
import org.apache.spark.streaming.kafka.KafkaUtils

object KafkaWordCount {
    def main(args: Array[String]) {
        if (args.length < 3) {
            System.err.println("Usage: KafkaWordCount <zkQuorum> <consumerGroup> <topic>")
                System.exit(1)
        }
        val Array(zkQuorum, consumerGroup, topic) = args
            val conf = new SparkConf().setMaster("local[*]").setAppName("KafkaWordCount")
            val ssc = new StreamingContext(conf, Seconds(2))
            val lines = KafkaUtils.createStream(ssc, zkQuorum, consumerGroup, Map(topic -> 1)).map(_._2)
            val words = lines.flatMap(_.split(" "))
            val pairs = words.map(word => (word, 1))
            val wordCounts = pairs.reduceByKey(_ + _)
            wordCounts.print()
            ssc.start()
            ssc.awaitTermination()
    }
}
