from pyspark.sql import Row

# Load a text file and convert each line to a Row.
txtRDD = sc.textFile("/data/spark/people.txt")
arrayRDD = txtRDD.map(lambda l: l.split(","))
personRDD = arrayRDD.map(lambda p: Row(name=p[0], age=int(p[1])))

# Infer the schema, and register the DataFrame as a table.
peopleDF = spark.createDataFrame(personRDD)

peopleDF.show()
