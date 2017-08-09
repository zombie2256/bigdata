//export YARN_CONF_DIR=/etc/hadoop/conf/
//export HADOOP_CONF_DIR=/etc/hadoop/conf/
//Start Spark Shell /usr/spark2.0.2/bin/spark-shell 

import org.apache.spark.graphx.GraphLoader

// Load the edges as a graph
val graph = GraphLoader.edgeListFile(sc, "/data/spark/graphx/followers.txt")
// Run PageRank
val ranks = graph.pageRank(0.0001).vertices

//Take a look at the output
ranks.collect()
//res1: Array[(org.apache.spark.graphx.VertexId, Double)] = Array((4,0.15), (6,0.7), ....

// Join the ranks with the usernames
val users = sc.textFile("/data/spark/graphx/users.txt").map { line =>
  val fields = line.split(",")
  (fields(0).toLong, fields(1))
}
val ranksByUsername = users.join(ranks).map {
  case (id, (username, rank)) => (username, rank)
}
// Print the result
println(ranksByUsername.collect().mkString("\n"))
