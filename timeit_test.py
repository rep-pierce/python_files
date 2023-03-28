import timeit
print(timeit.timeit('output = [x**2 for x in range(10)]', number=1000))

# output = 0.0005423860002338188