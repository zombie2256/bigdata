import org.apache.spark.sql.types._
import org.apache.spark.sql._

// The schema is encoded in a string
// User provided variable
val schemaString = "name age"
val filename = "/data/spark/people.txt"

val fieldsArray = schemaString.split(" ")
val fields = fieldsArray.map(
f => StructField(f, StringType, nullable = true)
)
val schema = StructType(fields)

val peopleRDD = spark.sparkContext.textFile(filename)
val rowRDD = peopleRDD.map(_.split(",")).map(attributes => Row.fromSeq(attributes))
val peopleDF = spark.createDataFrame(rowRDD, schema)
peopleDF.show()
