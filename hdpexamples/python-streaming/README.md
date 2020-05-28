# First find the Streaming file location


  [sandeepgiri9034@cxln4 python-streaming]$ find /usr/hdp -name hadoop-streaming.jar
  /usr/hdp/2.6.2.0-205/hadoop-mapreduce/hadoop-streaming.jar
  
# Execute Same DNA Exercise like the following. Please use the streaming file location from previous step

  hadoop jar /usr/hdp/2.6.2.0-205/hadoop-mapreduce/hadoop-streaming.jar -input /data/mr/dna/dna.txt -output mapreduce-programming/find_anagrams -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py
  
  
