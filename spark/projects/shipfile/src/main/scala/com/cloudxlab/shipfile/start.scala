import org.apache.spark.sql.SparkSession
import scala.io.Source

object HelloWorld {
	def readfile():Array[String] = {
		return Source.fromFile("props.txt").getLines.toArray	
	}
	def main(args: Array[String]) {
		val bigfile = "/data/mr/wordcount/input/big.txt" // Should be some file on your system
		val spark = SparkSession.builder.appName("Simple Application").getOrCreate()
		var lines = spark.sparkContext.textFile(bigfile);
		var words = lines.flatMap(_.split(" ")).map(_.toLowerCase)
		words.foreachPartition(x=> readfile().foreach(println))
		spark.stop()
	}
}
