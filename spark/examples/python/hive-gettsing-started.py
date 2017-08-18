from pyspark.sql import SparkSession
s = SparkSession.builder.enableHiveSupport().getOrCreate()
s.sql("show databases").show();
