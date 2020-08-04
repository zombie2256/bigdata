from pyspark.sql.types import Row

textRDD = sc.textFile("/data/spark/people.txt")

arrayRDD = textRDD.map(lambda x: x.split(","))

rowRDD = arrayRDD.map(lambda arr: Row(name=arr[0], age=int(arr[1].strip())))

peopleDF = rowRDD.toDF()
peopleDF.show()
