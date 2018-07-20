package com.cloudxlab.phrasesearch

import org.scalatest.FlatSpec

class PhraseSearchSpec extends FlatSpec {

  "Line2WordsLengthCheck" should "Check Length of lineToWords" in {
    val utils = new Utils
    var words = utils.lineToWords(("1", "this is good"))
    assert(words.length == 3)
    assert(words(0)._1 == "this")
    assert(words(1)._1 == "is")
    assert(words(2)._1 == "good")
    assert(words(0)._2._2 == "1")
    assert(words(0)._2._1 == 0)
    assert(words(1)._2._1 == 1)
  }
  
  "phraseToWordsCheck" should "Check if phrasetoword is working" in {
    val utils = new Utils
    var words = utils.phraseToWords(("1", "This is a phrase"));
    assert(words(0)._1 == "this")
    assert(words.length == 4)
    //for(i <- 0 to l-1) output.append( (arr(i),(i, t._2, l, ph) ) )
    assert(words(1)._2._1 == 1)
    assert(words(1)._2._2 == "1")
    assert(words(1)._2._3 == 4)
    assert(words(1)._2._4 == "this is a phrase")
  }
  
  "toDocsKeyCheck1" should "Check if todockeys is working" in  {
    val utils = new Utils
    var result = utils.toDocsKey(("is", ((1, "1"), (2, "2", 10, "1"))))
    
//    Result(w, tw_loc, ph_loc, ph_len)
//    var w = a._1
//            var twdetails = a._2._1
//            var phdetails = a._2._2
//            var tw_loc = twdetails._1
//            var tw_id = twdetails._2
//            
//            var ph_loc = phdetails._1
//            var ph_id = phdetails._2
//            var ph_len = phdetails._3
//            var w1 = phdetails._4
      var k = ("1", "2")
      var r = Result("is", 1, 2, 10)
    assert(result._1 == k)
    assert(result._2(0) == r)
  }
  // "overallCheck" should "check if the search is giving right results" in {
    
  // }
}

