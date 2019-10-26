from pyspark.sql import *
from pyspark.sql.types import *
# The schema is encoded in a string. User provided variable
schemaString = "name age"
fieldsArray = schemaString.split(" ")
fields = map(
lambda f: StructField(f, StringType(), nullable = True),
fieldsArray)
schema = StructType(fields)
# Creating Rows RDD
filename = "/data/spark/people.txt"
peopleRDD = spark.sparkContext.textFile(filename)
arrRDD = peopleRDD.map(lambda x: x.split(","))
rowRDD = arrRDD.map(lambda attr: Row(attr[0], attr[1]))
# Creating Dataframe
peopleDF = spark.createDataFrame(rowRDD, schema)
peopleDF.show()
