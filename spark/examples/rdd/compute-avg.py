rdd = sc.parallelize([1.0,2,3, 4, 5 , 6, 7], 3);
rdd_count = rdd.map(lambda x: (x, 1))
(sum, count) = rdd_count.reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]))
print sum / count
