# empty range
print(list(range(0)))

# using range(stop)
print(list(range(10)))

# using range(start, stop)
print(list(range(1, 10)))

# using range(start, stop, step)
print(list(range(1,20,5)))

# Create a list of even number between the given numbers using range()
start = 2
stop = 14
step = 2

print(list(range(start, stop, step)))

# range() works with negative step
print(list(range(2,-20,-2)))