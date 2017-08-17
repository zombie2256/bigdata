from pyspark.sql import Row

# Load a text file and convert each line to a Row.
txtRDD = sc.textFile("/data/spark/people.txt")
arrayRDD = txtRDD.map(lambda l: l.split(","))
personRDD = arrayRDD.map(lambda p: Row(name=p[0], age=int(p[1])))

# Infer the schema, and register the DataFrame as a table.
peopleDF = spark.createDataFrame(personRDD)

peopleDF.show()

# Register the DataFrame as a temporary view
peopleDF.createOrReplaceTempView("people")

# SQL statements can be run by using the sql methods provided by Spark
teenagersDF = spark.sql("SELECT name, age FROM people WHERE age BETWEEN 13 AND 19")

# The columns of a row in the result can be accessed by field index
teenagersDF.rdd.map(lambda p: "Name: " + p.name).collect()
