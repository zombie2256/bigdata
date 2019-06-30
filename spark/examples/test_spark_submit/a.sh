export CLASSPATH=$CLASSPATH:/usr/hdp/current/spark-client/lib/spark-hdp-assembly.jar
scalac a.scala && jar -cvf a.jar * && spark-submit --class Main a.jar

