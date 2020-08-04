Launch Hive:

    hive

This should show something like this:

<pre>
[sandeepgiri9034@cxln4 ~]$ hive
log4j:WARN No such property [maxFileSize] in org.apache.log4j.DailyRollingFileAppender.

Logging initialized using configuration in file:/etc/hive/2.6.2.0-205/0/hive-log4j.properties
hive>

</pre>

On the console, run the following commands.

Show the list of databases:

    show databases

Create database of your own choice.
  
    create database sandeepgiri9034;

Know more about your database
  
    describe database sandeepgiri9034;

Delete your database (Don't really need it.)
  
    drop database sandeepgiri9034;

Use your database
  
    use sandeepgiri9034;

Show the list of tables
  
    show tables

    CREATE TABLE x (a INT);
    describe formatted x
    --- And uploaded a file in the location of x in HDFS
    select * from x

On console, run the following command to make a copy of the daa
  
    hadoop fs -cp /data/NYSE_daily .

On hive console, run the following command to create and load table  

    CREATE TABLE nyse_hdfs(
      exchange1 STRING,
      symbol1 STRING,
      ymd STRING,
      price_open FLOAT,
      price_high FLOAT,
      price_low FLOAT,
      price_close FLOAT,
      volume INT,
      price_adj_close FLOAT
      )
      ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';


    load data inpath 'hdfs:///user/sandeepgiri9034/NYSE_daily' overwrite into table nyse_hdfs;


Movie ratings data example.

Copy data from /data/ml-100k/u.data into our hdfs home

    hadoop fs -cp /data/ml-100k/u.data .
    hadoop fs -cp /data/ml-100k/u.item .

Open Hive console and run following:

    CREATE TABLE u_data( userid INT, movieid INT, rating INT, unixtime STRING)
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY '\t'
    STORED AS TEXTFILE;

    LOAD DATA INPATH '/user/sandeepgiri9034/u.data' overwrite into table u_data;

    select * from u_data limit 5;
    select movieid, avg(rating) ar from u_data group by movieid order by ar desc


See https://cloudxlab.com/assessment/slide/10/hive/326/hive-movielens-assignment?course_id=1

