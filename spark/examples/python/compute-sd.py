rdd = sc.parallelize([2, 3, 5, 6])
#Mean or average of numbers is μ 

rdd_count = rdd.map(lambda x: (x, 1))
(sum, count) = rdd_count.reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]))
avg = sum / count

# (xi - μ)2
sqdiff = rdd.map(lambda x: x - avg).map(lambda x: x*x)

# ∑(xi - μ)2
sum_sqdiff = sqdiff.reduce(lambda x, y: x + y)
#√1/N ∑(xi - μ)2

import math;
sd = math.sqrt(sum_sqdiff*1.0/count)
print sd
