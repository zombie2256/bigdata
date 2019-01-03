
## Initialiaze the environment

Sys.setenv(SPARK_HOME = "/usr/hdp/current/spark2-client")

library(SparkR, lib.loc = c(file.path(Sys.getenv("SPARK_HOME"), "R", "lib")))

sparkR.session(appName = "SparkR-Recommendation")

sparkR.session(master = "yarn-client")

# Create custom schema for the data

customSchema <- structType(
   structField("userId", "integer"),
   structField("movieId", "integer"),
   structField("rating", "double"))

# Load the CSV file using the custom schema

csvPath = "/data/ml-1m/user_ratings.csv"
df <- read.df(csvPath, "csv", header = "false", schema = customSchema, na.strings = "NA")
printSchema(df)

# Split into training and test set

df_list <- randomSplit(df, c(8,2), 2)
training <- df_list[[1]]
test <- df_list[[2]]

# Fit the model

# maxIter is the maximum number of iterations to run (defaults to 10).
# regParam specifies the regularization parameter in ALS (defaults to 1.0)

model <- spark.als(training, maxIter = 5, regParam = 0.01, userCol = "userId",
                   itemCol = "movieId", ratingCol = "rating")

# Check the summary of the model

summary(model)

# Evaluate the model's performance

predictions <- predict(model, test)
head(predictions)
