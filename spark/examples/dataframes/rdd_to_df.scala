import spark.implicits._

case class Person(name: String, age: Long)

val txtRDD = sc.textFile("/data/spark/people.txt")
val arrayRDD = txtRDD.map(_.split(","))
val personRDD = arrayRDD.map(attributes => Person(attributes(0), attributes(1).trim.toInt))
val peopleDF = personRDD.toDF()
peopleDF.show()
