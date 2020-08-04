# Map Reduce Example

~~~~
git clone https://github.com/cloudxlab/bigdata.git
cd bigdata/hdpexamples/java

Optionally Edit the files using Jupyter
From My Lab, open jupyter
Go to hdpexamples/java/src/com/cloudxlab
To change the wordcount example to use 2 reducer, uncoment line 43 in wordcount/StubDriver

ant jar

### To Run wordcount MapReduce, use:
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

In order to run char count, please use:

`hadoop jar build/jar/hdpexamples.jar com.cloudxlab.charcount.StubCCDriver /data/mr/wordcount/input/big.txt charcount_out`

This should create a directory in HDFS with the name `charcount_out`. This should display, something like the following:

<pre>
[sandeep@cxln4 java]$ hadoop fs -ls charcount_out
Found 5 items
-rw-r--r--   3 sandeep hdfs          0 2020-08-04 20:35 charcount_out/_SUCCESS
-rw-r--r--   3 sandeep hdfs        657 2020-08-04 20:35 charcount_out/part-r-00000
-rw-r--r--   3 sandeep hdfs          0 2020-08-04 20:35 charcount_out/part-r-00001
-rw-r--r--   3 sandeep hdfs          0 2020-08-04 20:35 charcount_out/part-r-00002
-rw-r--r--   3 sandeep hdfs          0 2020-08-04 20:35 charcount_out/part-r-00003
</pre>

In order to see the content of a file, please use the tail command: `hadoop fs -tail charcount_out/part-r-00000`

<pre>
		12
 	1036511
!	4345
"	26108
#	742
$	110
%	8
&	8
'	10018
(	1748
)	1748
*	489
+	91
,	77675
-	17127
.	58672
/	132
0	3064
1	5572
2	3053
3	2492
4	2417
5	2192
6	1993
7	1890
8	2527
9	1999
:	1855
;	3511
<	2
=	1764
>	3
?	4155
@	8
A	12217
B	5962
C	6119
D	4029
E	5584
F	4501
G	3184
H	7358
I	17174
J	1322
K	1638
L	2744
M	6234
N	6621
O	4184
P	8946
Q	149
R	5578
S	8659
T	16282
U	1618
V	1853
W	6255
X	614
Y	2285
Z	145
[	435
]	435
^	2
_	5488
a	395872
b	67206
c	138853
d	211677
e	628234
f	116374
g	93732
h	287323
i	348464
j	5114
k	31160
l	195904
m	120829
n	362397
o	382683
p	89967
q	4422
r	303977
s	326238
t	444459
u	137114
v	50525
w	94576
x	9196
y	88196
z	3651
|	408
~	2
</pre>

=======
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
