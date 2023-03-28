import itertools
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = list(itertools.chain(list1, list2))
print(combined)

# combined = [1, 2, 3, 'a', 'b', 'c']