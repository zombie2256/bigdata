import org.apache.spark._
import org.apache.spark.streaming._

object WordCountStatful {
    def updateFunction(newValues: Seq[Int], runningCount: Option[Int]): Option[Int] = {
        val newCount = runningCount.getOrElse(0) + newValues.sum
        Some(newCount)
    }
    
    def main(args: Array[String]) {
        // Create a local StreamingContext with batch interval of 10 second
        val conf = new SparkConf().setMaster("local[*]").setAppName("WordCount")
	val sc = new SparkContext(conf);
        sc.setLogLevel("WARN")
        val ssc = new StreamingContext(sc, Seconds(2))
        ssc.checkpoint("chk")
        // Create a DStream that will connect to hostname:port, like localhost:9999
        val lines = ssc.socketTextStream("localhost", 9999)

        // Split each line in each batch into words
        val words = lines.flatMap(_.split(" "))

        // Count each word in each batch
        val pairs = words.map(word => (word, 1))
        val wordCounts = pairs.reduceByKey(_ + _)
        val runningCounts = pairs.updateStateByKey[Int](updateFunction _)
        // Print the elements of each RDD generated in this DStream to the console
        runningCounts.print()

        // Start the computation
        ssc.start()

        // Wait for the computation to terminate
        ssc.awaitTermination()
    }
}
