linesRDD = sc.parallelize( ["this is a dog", "named jerry"])
def toWords(line):
  return line.split()

wordsRDD = linesRDD.flatMap(toWords)
wordsRDD.collect()
['this', 'is', 'a', 'dog', 'named', 'jerry']
