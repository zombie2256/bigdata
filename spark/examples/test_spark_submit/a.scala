import org.apache.spark._
import org.apache.spark.SparkContext
import org.apache.spark.rdd.RDD
import org.apache.spark.SparkContext._


object Main
{
	def main(args:Array[String]): Unit = {
		val conf = new SparkConf().setAppName("WordCount")
		val sc = new SparkContext(conf);
		sc.setLogLevel("WARN");
		val arr = 1 to 10000
		val nums = sc.parallelize(arr)

		def multiplyByTwo(x:Int) = Array(x*2)
		var dbls = nums.flatMap(multiplyByTwo);
		var ret  = dbls.take(5)
		for(e <- ret){
			print(e)
		}
	}
}

