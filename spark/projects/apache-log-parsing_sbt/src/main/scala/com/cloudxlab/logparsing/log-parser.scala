package com.cloudxlab.logparsing

import org.apache.spark._
import org.apache.spark.SparkContext._

object EntryPoint {
	case class LogRecord( host: String, timeStamp: String, url:String,httpCode:Int)
	val PATTERN = """^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)(.*)" (\d{3}) (\S+)""".r

	def containsIP(line:String):Boolean = return line matches "^([0-9\\.]+) .*$"
	//Extract only IP
	def extractIP(line:String):(String) = {
	    val pattern = "^([0-9\\.]+) .*$".r
	    val pattern(ip:String) = line
	    return (ip.toString)
	}
    def main(args: Array[String]) {
        
        // Create a local StreamingContext with batch interval of 10 second
        val conf = new SparkConf().setAppName("WordCount")
        val sc = new SparkContext(conf);
        sc.setLogLevel("WARN")
		var accessLogs = sc.textFile("/data/spark/project/access/access.log.45.gz")
		accessLogs.take(10)

		//Keep only the lines which have IP
		
		var ipaccesslogs = accessLogs.filter(containsIP)
		var cleanips = ipaccesslogs.map(extractIP(_))
		var ips_tuples = cleanips.map((_,1));
		var frequencies = ips_tuples.reduceByKey(_ + _);
		var sortedfrequencies = frequencies.sortBy(x => x._2, false)
		var top10 = sortedfrequencies.take(10)
		println("===== TOP 10 IP Addresses =====")
		for(i <- top10){
			println(i)
		}
    }
}
