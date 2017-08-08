
import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.recommendation.ALS
 
case class Rating(userId: Int, movieId: Int, rating: Float, timestamp: Long)
def parseRating(str: String): Rating = {
  val fields = str.split("::")
  assert(fields.size == 4)
  Rating(fields(0).toInt, fields(1).toInt, fields(2).toFloat, fields(3).toLong)
}

var raw = spark.read.textFile("/data/ml-1m/ratings.dat")
val ratings = raw.map(parseRating).toDF()
val Array(training, test) = ratings.randomSplit(Array(0.8, 0.2))

// Build the recommendation model using ALS on the training data
//Alternating Least Squares (ALS) matrix factorization.
val als = new ALS().setMaxIter(5).setRegParam(0.01).setUserCol("userId").setItemCol("movieId").setRatingCol("rating")

val model = als.fit(training)
model.save("mymodel")

//Prepare the recommendations
val predictions = model.transform(test)
predictions.take(10)

predictions.write.format("com.databricks.spark.csv").save("ml-predictions.csv")
