## What is this?

This is an example to demonstrate how the "--files" work or how to ship files to all the nodes.

To run follow these steps:

	+ sbt package
	+ spark-submit --master yarn --files props.txt target/scala-2.11/read-shipped-file_2.11-1.0.jar
	+ FInd out the application id from the previous step. for me it was application_1547862802432_6923
	+ yarn logs -applicationId application_1547862802432_6923

It should display something like:

![From the logs of ship file]
(shipfile_output.png)

