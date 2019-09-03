# Terminal 1 - Create topic in Kafka
<pre>
#Include Kafka binaries in the path. HDP includes the kafka and installs at /usr/hdp/current/kafka-broker
  
  export PATH=$PATH:/usr/hdp/current/kafka-broker/bin
   
#Create the topic
#Replace localhost with the hostname of node where zookeeper server is running. Generally, zk runs on all hosts on the cluster.
#Replace test with your topic name
  
  kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sandeepgiri9034_test

#Check if topic is created
  
  kafka-topics.sh  --list --zookeeper localhost:2181
</pre>

# Terminal 1 - Produce the results
<pre>
  # Locate the kafka brokers
  # The kafka brokers inform zookeeper about their IPs adresses. Most of the eco-system considers the zookeeper as a central registry.
  # First launch zookeeper client
  
  zookeeper-client

  # I found the for me the location of one of the brokers was ip-172-xx-xx-xxx.ec2.internal:6667

  # find the ip address of any broker from zookeeper-client using command get /brokers/ids/0
  # On the zookeeper-client prompt, list all the brokers that registered
  ls /brokers/ids

  # Now, get the information about all the ids using the get command with the nodes listed in previous command
  # For example:
  get /brokers/ids/1001
  get /brokers/ids/1002
  get /brokers/ids/1003

  # Include Kafka binaries in the path. HDP includes the kafka and installs at /usr/hdp/current/kafka-broker
  export PATH=$PATH:/usr/hdp/current/kafka-broker/bin

  # Push messages to topic, type "my first kafka topic"
  kafka-console-producer.sh --broker-list cxln4.c.thelab-240901.internal:6667 --topic sandeepgiri9034_test

  #This will give you a prompt to type the input which will be pushed to the topic
  # Say I typed here: this is a cow this is a bow

</pre>

# Terminal 2 - Test Consuming Messages
<pre>
  # Test if producer is working by consuming messages in another terminal
  # Replace localhost with the hostname of broker
  export PATH=$PATH:/usr/hdp/current/kafka-broker/bin
  kafka-console-consumer.sh --zookeeper localhost:2181 --topic sandeepgiri9034_test --from-beginning
  
  # Please come out of it by pressing CTRL+C once you have checked if the messages are reaching the consumer. 
</pre>

# Terminal 2 - Consume using Pyspark

## Launch the pyspark
```
  pyspark --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2
```
## Copy-paste the following code

```
#    Spark
from pyspark import SparkContext
#    Spark Streaming
from pyspark.streaming import StreamingContext
#    Kafka
from pyspark.streaming.kafka import KafkaUtils
#    json parsing
import json

# Every 5 seconds
ssc = StreamingContext(sc, 5)

lines = KafkaUtils.createStream(ssc, 'localhost:2181', "spark-streaming-consumer", {'sandeepgiri9034_test':1})

# Split each line in each batch into words
words = lines.flatMap(lambda line: line[1].split(" "))

# Count each word in each batch
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

# Print the elements of each RDD generated in this DStream to the console
wordCounts.pprint()

# Start the computation
ssc.start()

# Wait for the computation to terminate
ssc.awaitTermination()

```
