## How to run it

 hadoop jar  /usr/hdp/2.6.5.0-292/hadoop-mapreduce/hadoop-streaming.jar -input /data/mr/wordcount/big.txt -output word_count_r -mapper mapper.r -file mapper.r -reducer reducer.r -file reducer.r 
