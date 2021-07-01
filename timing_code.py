'''
We know that for any program there are many ways avialabe.
suppose we want to print a list of n number in string. We can do this by 2 methods, and it's important to understand which code runs fast
to do this there a 2 ways avialabe in python
'''
def func_one(n):
    return [str(num) for num in range(n)]
func_one(100)
#print(func_one(100))

def func_two(n):
    return list(map(str,range(n)))
func_two(100)
#print(func_two(100))
'''
Lets check which function run fast, method 1 taking difference between statring and ending tie of code
'''
import time
# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_one(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time
print(end_time)

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_two(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time
print(end_time)

'''
Method 2 using timeit module
'''
import timeit
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
stmt = 'func_one(100)'
print(timeit.timeit(stmt,setup,number=100000))

setup2 = '''
def func_two(n):
    return [str(num) for num in range(n)]
'''
stmt2 = 'func_two(100)'
print(timeit.timeit(stmt2,setup2,number=100000))
