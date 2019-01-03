
## Initialiaze the environment

Sys.setenv(SPARK_HOME = "/usr/hdp/current/spark2-client")

library(SparkR, lib.loc = c(file.path(Sys.getenv("SPARK_HOME"), "R", "lib")))

sparkR.session(appName = "SparkR-ML-kmeans-example")

sparkR.session(master = "yarn-client")

# Load titanic dataset as R dataframe

t <- as.data.frame(Titanic)
head(t)

# Create Spark dataframe using R dataframe

training <- createDataFrame(t)


# split into train and test

df_list <- randomSplit(training, c(7,3), 2)

train <- df_list[[1]]
test <- df_list[[2]]

# Fit the kmeans model using class, sex, age and frequency attribute
# The number of clusters are 3

kmeansModel <- spark.kmeans(train, ~ Class + Sex + Age + Freq, k = 3)

# Check the summary of the model

summary(kmeansModel)

# See the first few rows of the model

head(fitted(kmeansModel))

# Evaluate the model on the test data

kmeansPredictions <- predict(kmeansModel, test)
head(kmeansPredictions)
