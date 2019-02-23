import org.apache.spark.sql.SparkSession

object HelloWorld {
  def main(args: Array[String]) {
    val bigfile = "/data/mr/wordcount/input/big.txt" // Should be some file on your system
    val spark = SparkSession.builder.appName("Simple Application").getOrCreate()
    //val logData = spark.read.textFile(logFile).cache()
    //val numAs = logData.filter(line => line.contains("a")).count()
    //val numBs = logData.filter(line => line.contains("b")).count()
    //println(s"Lines with a: $numAs, Lines with b: $numBs")
    var rdd = spark.sparkContext.textFile(bigfile);
    for(line <- rdd.take(10)){
	print(line)
    }
    spark.stop()
  }
}
