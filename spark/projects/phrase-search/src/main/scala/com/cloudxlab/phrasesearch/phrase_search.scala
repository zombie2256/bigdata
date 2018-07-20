// export HADOOP_CONF_DIR=/etc/hadoop/conf/
// export YARN_CONF_DIR=/etc/hadoop/conf/
// /usr/spark-2.3.1/bin/spark-shell
// /usr/spark2.0.2/bin/spark-shell
package com.cloudxlab.phrasesearch

import scala.collection.mutable.ArrayBuffer

import org.apache.spark._
import org.apache.spark.SparkContext
import org.apache.spark.rdd.RDD
import org.apache.spark.SparkContext._

case class Result(w:String, tw_loc:Int, ph_loc:Int, ph_len:Int)

class Utils extends Serializable {
    def lineToWords(row:(String, String)):ArrayBuffer[(String, (Int,String))] = {
        var id = row._1
        var res = ArrayBuffer[(String, (Int,String))]()
        if(id != null) {
            var txt:String = row._2
            var arr = txt.split(" ")
            for(i <- 0 to arr.length-1) {
                res += Tuple2(arr(i), (i, id));
            }
        }
        return res
    }
    
    def phraseToWords(t:Tuple2[String, String]):ArrayBuffer[(String, (Int, String, Int, String))] = {
            var ph = t._2.toLowerCase()
            var arr = ph.split(" ");
            var output = ArrayBuffer[(String, (Int, String, Int, String))]()
            var l = arr.length
            // Do we need ph
            for(i <- 0 to l-1) output.append( (arr(i),(i, t._1, l, ph) ) )
            return output
    }
    def toDocsKey(a:Tuple2[String, ((Int, String), (Int, String, Int, String))]): Tuple2[(String, String), Array[Result]] = {
            var w = a._1
            var twdetails = a._2._1
            var phdetails = a._2._2
            var tw_loc = twdetails._1
            var tw_id = twdetails._2
            
            var ph_loc = phdetails._1
            var ph_id = phdetails._2
            var ph_len = phdetails._3
            var w1 = phdetails._4
            return ((tw_id, ph_id), Array(Result(w, tw_loc, ph_loc, ph_len)))
        }
    def crossjoin(sc:SparkContext, phrases:RDD[(String, String)], txt:RDD[(String, String)]):RDD[((String, String), Array[Result])] = {
      var phrasewords = phrases.flatMap(phraseToWords)
        var txtwords = txt.flatMap(lineToWords)

        var joind = txtwords.join(phrasewords)
        var isMapJoined = joind.map(toDocsKey)
        return isMapJoined.reduceByKey(_ ++ _);
    }
    
    def search(sc:SparkContext, phrases:RDD[(String, String)], txt:RDD[(String, String)]):RDD[((String, String), Array[Int])] = {
        
        return null
    }
    
}

object EntryPoint {
    val usage = """
        Usage: EntryPoint <how_many> <file_or_directory_in_hdfs>
        Eample: EntryPoint 10 /data/spark/project/access/access.log.45.gz
    """
    
    def main(args: Array[String]) {
        
        // if (args.length != 3) {
        //     println("Expected:3 , Provided: " + args.length)
        //     println(usage)
        //     return;
        // }

        var utils = new Utils

        // Create a local StreamingContext with batch interval of 10 second
        val conf = new SparkConf().setAppName("WordCount")
        val sc = new SparkContext(conf);
        sc.setLogLevel("WARN")

        // var accessLogs = sc.textFile("/data/spark/project/access/access.log.45.gz")
        // var accessLogs = sc.textFile(args(2))

        var tinytext = sc.textFile("/Users/sandeep/projects/bigdata/spark/projects/phrase-search/data/tiny_text.tsv").map(_.split("\t"));
        print(tinytext.collect())

        //var commonphrases = sc.textFile("/Users/sandeep/projects/bigdata/spark/projects/phrase-search/data/phrase_tiny.tsv").map(_.split("\t"))
        var commonphrases = sc.textFile("/Users/sandeep/projects/bigdata/spark/projects/phrase-search/data/phrase_tiny.tsv").map(_.split("\t"));
        print(tinytext.collect())

        
    }
}
