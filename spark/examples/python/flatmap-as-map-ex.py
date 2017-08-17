arr = range(1,10000)
nums = sc.parallelize(arr)
def multiplyByTwo(x):
    return [x*2]

dbls = nums.flatMap(multiplyByTwo);
dbls.take(5)
