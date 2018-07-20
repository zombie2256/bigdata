package com.cloudxlab.phrasesearch

import org.scalatest.FunSuite
import com.holdenkarau.spark.testing.{RDDComparisons, SharedSparkContext}

class SampleTest extends FunSuite with SharedSparkContext {
    test("Computing top10") {
        val utils = new Utils
        
        val txt = sc.parallelize(Array(("1", "nice line"), ("2", "another line")));
        val phrases = sc.parallelize(Array(("11", "nice"), ("22", "another")));
        var results = utils.crossjoin(sc, phrases, txt)
        var localresults = results.collect()
        //nice (1, 11)
        //another (2, 22)
          
        
//        assert(rdd.count === list.length)   
//
//        val records = utils.gettop10(rdd, sc, 10)
//        assert(records.length === 1)    
//        assert(records(0)._1 == "121.242.40.10")
    }
//    test("Should remove IP addresses having 1st Octet Decimal more than 126") {
//        var line1 = "121.242.40.10 - - [03/Aug/2015:06:30:52 -0400] \"POST /mod_pagespeed_beacon?url=http%3A%2F%2Fwww.knowbigdata.com%2Fpage%2Fabout-us HTTP/1.1\" 204 206 \"http://www.knowbigdata.com/page/about-us\" \"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0\""
//        var line2 = "216.113.160.77 - - [03/Aug/2015:06:30:52 -0400] \"POST /mod_pagespeed_beacon?url=http%3A%2F%2Fwww.knowbigdata.com%2Fpage%2Fabout-us HTTP/1.1\" 204 206 \"http://www.knowbigdata.com/page/about-us\" \"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0\""
//        val list = List(line1, line2)
//        val rdd = sc.parallelize(list);
//
//        val utils = new Utils
//        val records = utils.gettop10(rdd, sc, 10)
//        assert(records.length === 1)
//        assert(records(0)._1 == "121.242.40.10")
//    }
}