#launch pyspark as follows:
# /usr/spark2.0.2/bin/pyspark  --packages com.databricks:spark-xml_2.10:0.4.1

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

df = sqlContext.read.format('com.databricks.spark.xml').options(rowTag='book').load('/data/spark/books.xml')
df.show()
