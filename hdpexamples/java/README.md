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

