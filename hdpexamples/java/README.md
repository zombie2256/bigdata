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


#To Run charcount MapReduce example, please use:

    hadoop jar build/jar/hdpexamples.jar com.cloudxlab.charcount.StubCCDriver /data/mr/wordcount/input charcount

#This will save the result in charcount folder. Take a look at result:
    
    hadoop fs -ls charcount

#It would look something like this:
<pre>
Found 5 items
-rw-r--r--   3 sandeepgiri9034 sandeepgiri9034          0 2019-09-12 01:26 charcount/_SUCCESS
-rw-r--r--   3 sandeepgiri9034 sandeepgiri9034        657 2019-09-12 01:26 charcount/part-r-00000
-rw-r--r--   3 sandeepgiri9034 sandeepgiri9034          0 2019-09-12 01:26 charcount/part-r-00001
-rw-r--r--   3 sandeepgiri9034 sandeepgiri9034          0 2019-09-12 01:26 charcount/part-r-00002
-rw-r--r--   3 sandeepgiri9034 sandeepgiri9034          0 2019-09-12 01:26 charcount/part-r-00003
</pre>

#To see char counts
    
    hadoop fs -cat charcount/part-r-00000

#To further clean the result
    
    hadoop fs -cat charcount/part-r-00000|tr 'A-Z' 'a-z'|awk '{print $2" "$1}'|sort -nr|more

#Result will look like this:

<pre>
 1036519
628237 e
444466 t
395879 a
382683 o
362397 n
348467 i
326242 s
303980 r
287325 h
211677 d
195904 l
138855 c
137114 u
120829 m
116374 f
94576 w
93732 g
89967 p
88196 y
77675 ,
67206 b
58672 .
50525 v
31160 k
26108 "
17174 i
17127 -
16282 t
12217 a
10018 '
9196 x
8946 p
8659 s
7358 h
6621 n
6255 w
6234 m
6119 c
5962 b
5584 e
5578 r
5572 1
5488 _
5114 j
4501 f
4422 q
4345 !
4184 o
4155 ?
4029 d
3651 z
3511 ;
3184 g
3064 0
3053 2
2744 l
2527 8
2492 3
2417 4
2285 y
2192 5
1999 9
1993 6
1890 7
1855 :
1853 v
1764 =
1748 )
1748 (
1638 k
1618 u
1748 )
1748 (
1638 k
1618 u
1322 j
742 #
614 x
489 *
435 ]
435 [
408 |
149 q
145 z
132 /
110 $
91 +
 12
8 %
8 &
8 @
3 >
2 <
2 ~
2 ^
</pre>
