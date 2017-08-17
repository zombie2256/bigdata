import random

rdd = sc.parallelize(range(1, 1000));
fraction = 0.1
def cointoss(x):
    return random.random() <= fraction
myrdd = rdd.filter(cointoss)
localsample = myrdd.collect()
len(localsample)
