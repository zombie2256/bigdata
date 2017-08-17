txtRDD = sc.textFile("/data/spark/temps.csv")
def cleanRecord(line):
    arr = line.split(",");
    return (arr[1].strip(), int(arr[0]))
recordsRDD = txtRDD.map(cleanRecord)
def max(a, b): return b if b > 1 else a
res = recordsRDD.reduceByKey(max)
res.collect()
