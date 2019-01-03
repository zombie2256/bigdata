
Sys.setenv(SPARK_HOME = "/usr/hdp/current/spark2-client")

library(SparkR, lib.loc = c(file.path(Sys.getenv("SPARK_HOME"), "R", "lib")))

sparkR.session(appName = "SparkR-LinearRegression")

sparkR.session(master = "yarn-client")

# Read the data

dataset <- read.df("/data/spark/sample_multiclass_classification_data.txt", source="libsvm")

# Split the data into training and test set

df_list <- randomSplit(dataset, c(7, 3), 2)

# Define training and test set

training <- df_list[[1]]
test <- df_list[[2]]

# Train the Linear Regression model

linear_regression_model <- spark.glm(training, label ~ features, family = "gaussian")

# Model summary

summary(linear_regression_model)


# Check the predictions

predictions <- predict(linear_regression_model, test)
head(predictions)

# Train a simple linear regression model for the 
# data set faithful, and estimate the next eruption duration based on the waiting time 

# Check the first few rows of the dataset
head(faithful)

# Create R Dataframe

dataset <- as.data.frame(faithful)
head(dataset)

# Create Spark dataframe

dataset <- createDataFrame(dataset)

# Split the Data into training and test set in 80:20 ratio

df_list <- randomSplit(dataset, c(8, 2), 2)

# Define training and test set

training <- df_list[[1]]
test <- df_list[[2]]

# Train the model

linear_regression_model <- spark.glm(training, eruptions ~ waiting, family = "gaussian")

# See the model summary

summary(linear_regression_model)

# Check the predictions

predictions <- predict(linear_regression_model, test)

# Question 

# Find the eruption duration if the waiting time since the last eruption has been 80 minutes.


newdata = data.frame(waiting=80)
newdata <- createDataFrame(newdata)
head(predict(linear_regression_model, newdata))
