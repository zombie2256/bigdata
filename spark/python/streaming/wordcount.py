// Copy the code and run it in spark-shell

from pyspark import *
from pyspark.streaming import *

sc.setLogLevel("ERROR")
// Create a local StreamingContext with batch interval of 10 second
ssc = StreamingContext(sc, 2)

// Create a DStream that will connect to hostname:port, like localhost:9999
lines = ssc.socketTextStream("localhost", 9999)

// Split each line in each batch into words
words = lines.flatMap(lambda x: x.split())

// Count each word in each batch
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

// Print the elements of each RDD generated in this DStream to the console
wordCounts.pprint()

// Start the computation
ssc.start() 

// Wait for the computation to terminate
ssc.awaitTermination()

