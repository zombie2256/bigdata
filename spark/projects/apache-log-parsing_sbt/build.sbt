name := "Apache Log Parsing"

version := "0.0.1"

scalaVersion := "2.10.4"

// additional libraries
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "1.5.2" % "provided",
  "org.scalatest" % "scalatest_2.11" % "3.0.1" % "test"
)
