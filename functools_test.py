from functools import partial

def add(x, y):
    return x - y

add_five = partial(add, 5)
result = add_five(10)
print(result)

# result = 15