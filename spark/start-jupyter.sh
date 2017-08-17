export SPARK_HOME="/usr/spark2.0.1/" 
export PYTHONPATH=$SPARK_HOME/python/:$SPARK_HOME/python/lib/py4j-0.10.3-src.zip:$SPARK_HOME/python/lib/pyspark.zip:$PYTHONPATH 
export PATH=/usr/local/anaconda/bin:$PATH
jupyter notebook --no-browser --ip 0.0.0.0 --port 8888
