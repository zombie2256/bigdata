
Sys.setenv(SPARK_HOME = "/usr/hdp/current/spark2-client")

library(SparkR, lib.loc = c(file.path(Sys.getenv("SPARK_HOME"), "R", "lib")))

sparkR.session(appName = "SparkR-LogisticRegression")

sparkR.session(master = "yarn-client")

# Let's train logistic regression on mtcars which determines the
# transmission type (am) by the horsepower (hp) and weight (wt)



# Get the dataset information

?mtcars

# Check the first few rows of the dataset

head(mtcars)

# Create R Dataframe

dataset <- as.data.frame(mtcars)
head(dataset)

# Create Spark dataframe

dataset <- createDataFrame(dataset)


# Split the Data into training and test set in 80:20 ratio

df_list <- randomSplit(dataset, c(8, 2), 2)

# Define training and test set

training <- df_list[[1]]
test <- df_list[[2]]

# Train the model

logistic_model <- spark.logit(training, am ~ hp + wt)

# See the model summary

summary(logistic_model)

# Check the predictions

predictions <- predict(logistic_model, test)
head(predictions)

# Question

# find the transmission type(am) of the vehicle
# which has a 120hp engine (hp) and weights 2800 lbs (wt)

# Answer 

newdata = data.frame(hp=120, wt=2.8)
newdata <- createDataFrame(newdata)

head(predict(logistic_model, newdata))
