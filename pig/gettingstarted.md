Launch pig Console

    pig

On the pig console which is marked `grunt>`:

Load the data from HDFS. You can take a look at the file using hadoop fs -ls /data/NYSE_dividends

    divs = LOAD '/data/NYSE_dividends' AS (exchange, stock_symbol, date, dividends);
  
Group The data

    grped = GROUP divs BY stock_symbol;
  
Find the average

    avged = FOREACH grped GENERATE  group,  AVG(divs.dividends);
  
Show the records

    DUMP avged;
  
Save in the HDFS

    STORE avged INTO 'avged';
  
Check if the folder is created. Note `ls` and `cat` are the pig commands

    ls avged
  
Print the result

    cat avged/part-v001-o000-r-00000

