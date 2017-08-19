## This is how I created this project

#Install maven
brew install maven

#Create the project
mvn archetype:generate -DgroupId=com.cloudxlab.zk -DartifactId=ZookeeperExample -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

# Copied the code from https://zookeeper.apache.org/doc/trunk/javaExample.html#sc_design
# into ZookeeperExample/src/main/com.cloudxlab.zk

#TO Build go into
cd ZookeeperExample

mvn package

export CLASSPATH=./target/ZookeeperExample-1.0-SNAPSHOT.jar 

java  com.cloudxlab.zk.Executor
