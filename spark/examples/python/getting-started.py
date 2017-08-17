from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()
sc = spark.sparkContext
