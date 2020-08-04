
Sys.setenv(SPARK_HOME = "/usr/hdp/current/spark2-client")


library(SparkR, lib.loc = c(file.path(Sys.getenv("SPARK_HOME"), "R", "lib")))

sparkR.session(appName = "SparkR-Manipulation")

sparkR.session(master = "yarn-client")

# Create a spark dataframe

flightsDF <- read.df("/data/spark/flights.csv", "csv", header = TRUE)

# Print the schema of this SparkDataFrame
printSchema(flightsDF)

# Print the first 6 rows of the SparkDataFrame
showDF(flightsDF, numRows = 6) ## Or
head(flightsDF)

# Show the column names in the SparkDataFrame
columns(flightsDF)

# Show the number of rows in the SparkDataFrame
count(flightsDF)

# Select specific columns
destDF <- select(flightsDF, "dest", "cancelled")

# Using SQL to select columns of data
# First, register the flights SparkDataFrame as a table
createOrReplaceTempView(flightsDF, "flightsTable")
destDF <- sql("SELECT dest, cancelled FROM flightsTable")

# Filter flights whose destination is JFK
jfkDF <- filter(flightsDF, flightsDF$dest == "JFK")

head(jfkDF)

if("magrittr" %in% rownames(installed.packages())) {
  library(magrittr)

  # Group the flights by date and then find the average daily delay
  # Write the result into a SparkDataFrame
  groupBy(flightsDF, flightsDF$date) %>%
    summarize(avg(flightsDF$dep_delay), avg(flightsDF$arr_delay)) -> dailyDelayDF

  # Print the computed SparkDataFrame
  head(dailyDelayDF)
}

