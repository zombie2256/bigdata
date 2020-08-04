import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.rdd.RDD

object HelloWorld1 {
  def main(args: Array[String]) {
    val bigfile = "/data/mr/wordcount/input/big.txt" // Should be some file on your system
    val conf:SparkConf = new SparkConf().setAppName("Hello")
    val sc:SparkContext = new SparkContext(conf)
    sc.setLogLevel("ERROR")
    var rdd = sc.textFile(bigfile)
    for(line <- rdd.take(10)){
	print(line)
    }
    rdd.saveAsTextFile("big_copy_spark");
    print("Created big_copy_spark directory");
  }
}
