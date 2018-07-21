import json

def find_phrases(sc, phrases_neddle, text_hay):
    def towords((id, s)):
        arr = s.lower().split();
        output = []
        for i in range(len(arr)):
            output.append( ( arr[i],(i, id) ) )
        return output

    #towords(("this is cow", 10000))
    words = text_hay.flatMap(towords)
    #words.take(10)

    #https://github.com/caarmen/thesaurus/blob/master/library/src/main/resources/dictionary_files/roget/pg10681.txt

    def tocommonwords((id, ph)):
        ph = ph.lower()
        arr = ph.split();
        output = []
        l = len(arr)
        for i in range(l):
            output.append( (arr[i],(i, id, l, ph) ) )
        return output

    # tocommonwords(("a dead horse", 1))
    commonwords = phrases_neddle.flatMap(tocommonwords)
    #commonwords.take(10)
    joind = words.join(commonwords)

    #res = joind.take(10)
    #from pprint import pprint
    #pprint(res, indent=4)
    #[   (u'swap', ((4, 330137257023516672), (0, 47632, 1, u'swap'))),
    #    (u'swap', ((6, 330137650805751808), (0, 47632, 1, u'swap'))),
    #    (u'swap', ((6, 330137684104314880), (0, 47632, 1, u'swap'))),
    #    (u'swap', ((6, 330139028903038980), (0, 47632, 1, u'swap'))),
    #    (u'swap', ((6, 330140237948915715), (0, 47632, 1, u'swap'))),
    #    (u'acoustic', ((6, 330123953584603136), (0, 551, 1, u'acoustic'))),
    #    (u'acoustic', ((6, 330123953584603136), (0, 552, 2, u'acoustic organs'))),
    #    (u'unrelated', ((2, 330136502237528066), (0, 52314, 1, u'unrelated'))),
    #    (   u'nail',
    #        ((7, 330055897852305408), (3, 3217, 4, u'attack tooth and nail'))),
    #    (u'nail', ((7, 330055897852305408), (0, 32457, 1, u'nail')))
    #]

    def to_docs_key((w, (twdetails, phdetails))):
        (tw_loc, tw_id) = twdetails
        (ph_loc, ph_id, ph_len, w1) = phdetails
        return ((tw_id, ph_id), [(w, tw_loc, ph_loc, ph_len)])

    to_docs_key((u'swap', ((4, 330137257023516672), (0, 47632, 1, u'swap'))))

    ids_words_list = joind.map(to_docs_key)
    def concat_arr(x, y):
        return x + y;

    grped_by_ids = ids_words_list.reduceByKey(concat_arr)

    #grped_by_ids.take(10)
    #
    #   ((330143366031486976, 34529), [(u'the', 6, 1, 3)]), 
    #   ((330069166537195520, 23451), [(u'out', 2, 1, 4), (u'out', 17, 1, 4)]), ((330140950972219393, 48899), [(u'in', 19, 3, 5), (u'the', 14, 0, 5), (u'the', 20, 0, 5)]), 
    #   ((330167828860780544, 25151), [(u'in', 22, 0, 2)]), 
    #   ((330085409382076416, 28847), [(u'the', 3, 2, 4), (u'the', 9, 2, 4), (u'the', 13, 2, 4)]), 
    #   ((330048099072479232, 21012), [(u'to', 3, 1, 3)]), 
    #   ((330128676979089408, 34702), [(u'of', 1, 1, 3)]), 
    #   ((330094076009529344, 23451), [(u'the', 5, 2, 4)]), 
    #   ((330062596361314304, 29106), [(u'man', 1, 1, 2)]), 
    #   ((330142973415288835, 28274), [(u'out', 6, 1, 2)])
    #
    #Keep Only the one where length matched 
    # grped_by_ids1 = grped_by_ids.filter(lambda (t, a): len(a) > a[0][3])

    def find_matches((t, a)):
        #Sort the data based on tw_loc
        a.sort(key=lambda t: (t[1], t[2]))
        print("After sorting")
        print(a) #[(u'the', 14, 1, 2), (u'in', 19, 0, 2), (u'the', 20, 1, 2)]
        #Go from left to right breaking it into continuous strings
        found = []
        prev = a[0]
        start = a[0][1]
        current = [prev]
        for i in range(1, len(a)):
            if a[i][1] == prev[1]:
                if a[i][2] > prev[2]:
                    current.pop()
                else:
                    continue
            elif a[i][1] != prev[1] + 1:
                found.append(current)
                current = []
            prev = a[i]
            current.append(prev)
        found.append(current)
        res = search_continuous(found, prev[3])
        if len(res) > 0:
            return [(t, res)]
        return []

    def find_matches_new((t, a)):
        print("find_matches_new: (%s, %s)" % (t, a))
        #Sort the data based on tw_loc
        a.sort(key=lambda t: (t[1], t[2]))
        print("After sorting")
        print(a) #[(u'the', 14, 1, 2), (u'in', 19, 0, 2), (u'the', 20, 1, 2)]
        #Go from left to right breaking it into continuous strings
        locs = []
        phlen = a[0][3]
        prev = a[0]
        start = a[0][1]
        popped = 0
        if a[0][2] == 0:
            popped += 1
        i = 0
        print("a[%s] : %s" % (i, a[i]))
        print("popped: %s, locs: %s, start: %s" % (popped, locs, start))
        for i in range(1, len(a)):
            print("a[%s] : %s" % (i, a[i]))
            if a[i][1] > prev[1] + 1:
                if popped >= phlen:
                    locs.append(start)
                print("Restarting.., popped: %s, locs: %s" % (popped, locs))
                start = a[i][1]
                popped = 1
            else:
                # print("Either it is equal or just +1")
                if (a[i][1] - start) == a[i][2]:
                    popped += 1
                    print("Increased popped to: %s" % popped)
            print("popped: %s, locs: %s, start: %s" % (popped, locs, start))
            prev = a[i]
        if popped >= phlen:
            locs.append(start)
        result = []
        if len(locs) > 0:
            result = [(t,locs)]
        print("Result: %s" % result)
        return result

    def find_matches2((t, a)):
        print("find_matches_new: (%s, %s)" % (t, a))
        #Prepare the line
        #swap t
        t = (t[1], t[0])
        a.sort(key=lambda t: (t[1]))
        prev = a[0]
        line = [a[0][0]]
        line_locs = [a[0][1]]
        for i in range(1, len(a)):
            if prev[1] == a[i][1]:
                continue;
            elif prev[1] + 1 < a[i][1]:
                line.append(u" ")
                line_locs.append(-1)
            # line.append(u" ")
            line.append(a[i][0])
            line_locs.append(a[i][1])
            prev = a[i]
        #Prepare the phrase
        a.sort(key=lambda t: (t[2]))
        prev = a[0]
        phrase = [a[0][0]]
        
        count = 1
        l = a[0][3]
        for i in range(1, len(a)):
            if(count >= l):
                break;
            if prev[2] == a[i][2]:
                continue;
            # phrase.append(u" ")
            phrase.append(a[i][0])
            count += 1
            prev = a[i]
        result = []
        if count >= l:
            locs = inarray(phrase, line)
            print("line_locs: %s, line: %s" %(line_locs, line))
            vals = [line_locs[i] for i in locs]
            if len(vals) > 0:
                result = [(t, vals)]
        print("Result: %s" % result)
        return result
    # find_matches2(((2, 4), [(u'not', 8, 3, 6), (u'be', 6, 1, 6), (u'be', 6, 5, 6), (u'be', 10, 1, 6), (u'be', 10, 5, 6), (u'to', 5, 0, 6), (u'to', 5, 4, 6), (u'to', 9, 0, 6), (u'to', 9, 4, 6), (u'or', 7, 2, 6)]))

    def inarray(a, b):
        print("inarray: (%s, %s)" % (a, b))
        result = []
        for start in range(len(b)-len(a)+1):
            broke = False
            for i in range(len(a)):
                if a[i] != b[i+start]:
                    broke = True
                    break
            if not broke:
                result.append(start)
        print("INARR Result: %s" % result)
        return result

    def search_continuous(found, length):
        # to_find = ' '.join(map(str, range(length)))
        # print("Searching: %s in %s" % (to_find, found))
        for list in found:
            #target = ' '.join(map(str, [x[2] for x in list]))
            #print("target: %s" % target)
            if length == len(list):
                return list
        return []

    #ismatch([(u'in', 19, 3, 5), (u'the', 14, 0, 5), (u'the', 20, 0, 5)])
    #ismatch([(u'in', 19, 0, 2), (u'the', 14, 1, 2), (u'the', 20, 1, 2)])
    
    grped_by_ids2 = grped_by_ids.flatMap(find_matches2)
    
    #grped_by_ids2.take(100)
    return grped_by_ids2

#[
#    ((330134383979802625, 26759), [(u'iron', 0, 0, 1), (u'iron', 13, 0, 1)]),
#    ((330137945724030976, 30366), [(u'man', 6, 0, 1), (u'man', 11, 0, 1)]), #((330043911940751360, 26759), [(u'iron', 2, 0, 1), (u'iron', 14, 0, 1)]), #((330159869292331009, 48830), [(u'the', 6, 0, 1), (u'the', 15, 0, 1)]), #((330076953656840194, 48830), [(u'the', 0, 0, 1), (u'the', 8, 0, 1), (u'the', 11, 0, 1)]), 
#    ((330145470863253504, 30366), [(u'man', 4, 0, 1), (u'man', 12, 0, 1)]), #((330153108011372545, 30366), [(u'man', 4, 0, 1), (u'man', 15, 0, 1)]), #((330138208451035137, 49779), [(u'to', 2, 0, 1), (u'to', 5, 0, 1)]), 
#    ((330139079704461312, 43140), [(u'see', 5, 0, 1), (u'see', 11, 0, 1)]), 
#    ((330055329847070720, 49779), [(u'to', 9, 0, 1), (u'to', 14, 0, 1)])
#]

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession


if __name__ == "__main1__":
        # conf = SparkConf().setAppName("Phrase Search")
        # sc = SparkContext(conf=conf)

        spark = SparkSession\
        .builder\
        .appName("PythonPi")\
        .getOrCreate()

        sc = spark.sparkContext
        # tweetsraw = sc.textFile("/data/SentimentFiles/SentimentFiles/upload/data/tweets_raw")
        tweetsraw = sc.textFile("/Users/sandeep/projects/bigdata/spark/projects/phrase-search/data/tweets")

        def extract_text(s):
            o = json.loads(s)
            return (o['id'], o['text'])

        text_hay = tweetsraw.map(extract_text)
        # commonphrases = sc.textFile("/data/common_phrases_pg10681.txt").zipWithIndex()
        commonphrases = sc.textFile("/Users/sandeep/projects/bigdata/spark/projects/phrase-search/data/phrases/common_phrases_pg10681.txt").zipWithIndex()

        def swap((x, y)):
            return (y, x)

        phrases_rdd =  commonphrases.map(swap)
        results = find_phrases(sc, phrases_rdd, text_hay)
        results.saveAsTextFile("phrase-search2")

if __name__ == "__main__":
        spark = SparkSession\
        .builder\
        .appName("PythonPi")\
        .getOrCreate()

        sc = spark.sparkContext
        
        sc.setLogLevel("WARN")
        spark.sparkContext.setLogLevel("ERROR")

        # tweetsraw = sc.textFile("/data/SentimentFiles/SentimentFiles/upload/data/tweets_raw")
        tinytext = sc.textFile("/Users/sandeep/projects/bigdata/spark/projects/phrase-search/data/tiny_text.tsv")

        def extract_text(s):
            if len(s) > 0:
                o = s.split("\t")
                return [(int(o[0]), o[1])]
            return []

        text_hay = tinytext.flatMap(extract_text)
        # commonphrases = sc.textFile("/data/common_phrases_pg10681.txt").zipWithIndex()
        commonphrases = sc.textFile("/Users/sandeep/projects/bigdata/spark/projects/phrase-search/data/phrase_tiny.tsv")
        phrases_neddle =  commonphrases.flatMap(extract_text)
        results = find_phrases(sc, phrases_neddle, text_hay)
        from pprint import pprint
        pprint(results.collect())
        #results.saveAsTextFile("tiny-phrase-search2")
