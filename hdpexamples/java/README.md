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


#This will create javamrout folder
# You can open Hue from mylab and click file browser to check the output
