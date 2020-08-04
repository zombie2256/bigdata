# Map Reduce Example
~~~~
git clone https://github.com/cloudxlab/bigdata.git
cd bigdata/hdpexamples/java

#Optionally Edit the files using Jupyter
    # From My Lab, open jupyter
    # Go to hdpexamples/java/src/com/cloudxlab
    # To change the wordcount example to use 2 reducer, uncoment line 43 in wordcount/StubDriver

ant jar

#To Run wordcount MapReduce, use:
hadoop jar build/jar/hdpexamples.jar com.cloudxlab.wordcount.StubDriver


This will create `javamrout` folder
You can check the result using -ls command
 `hadoop fs -ls javamrout`

It should display something like this:
<pre>
[sandeep@cxln4 java]$ hadoop fs -ls javamrout
Found 2 items
-rw-r--r--   3 sandeep hdfs          0 2020-08-04 14:14 javamrout/_SUCCESS
-rw-r--r--   3 sandeep hdfs     430471 2020-08-04 14:14 javamrout/part-r-00000

</pre>

You can see the output using `hadoop fs -tail javamrout/part-r-00000`

it should display something like this:
<pre>

yore    1
york    194
yorkers 1
...

</pre>



# You can open Hue from mylab and click file browser to check the output
