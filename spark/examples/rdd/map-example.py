
# Create a local array
arr = range(1, 10000)

#Load this array
nums = sc.parallelize(arr)

# Define the function
def multiplyByTwo(x):
    return x*2

# This should print 10
multiplyByTwo(5)

dbls = nums.map(multiplyByTwo);

#This should print [2, 4, 6, 8, 10]
dbls.take(5)
