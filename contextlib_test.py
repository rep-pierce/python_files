import time
from contextlib import contextmanager

@contextmanager
def timer(description):
    start_time = time.time()
    try:
        yield  # This is where the `with` block's code will be executed
    finally:
        elapsed_time = time.time() - start_time
        print(f"{description} took {elapsed_time:.2f} seconds")

# Usage
with timer("Sleeping for a while"):
    time.sleep(5)

# printed = Sleeping for a while took 5.00 seconds

file = open('example.txt', 'r')
content = file.read()
file.close()

with open('example.txt', 'r') as file:
    content = file.read()