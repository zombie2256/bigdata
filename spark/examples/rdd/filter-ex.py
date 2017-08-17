arr = range(1, 1000)
nums = sc.parallelize(arr)
def isEven(x):
    return  x%2 == 0

evens = nums.filter(isEven)
evens.take(3)
#Result: [2, 4, 6]
