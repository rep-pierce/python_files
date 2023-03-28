from collections import Counter, OrderedDict, defaultdict
text = "apple banana apple orange banana apple"
word_count = Counter(text.split())
print(word_count)

# output = Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Creating an OrderedDict
ordered_dict = OrderedDict()

# Adding items
ordered_dict['one'] = 1
ordered_dict['two'] = 2
ordered_dict['three'] = 3
ordered_dict['four'] = 4

# Iterating through the OrderedDict
for key, value in ordered_dict.items():
    print(f"{key}: {value}")

# output =  one: 1
#           two: 2
#           three: 3
#           four: 4


word_list = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']

# Creating a defaultdict with int as the default factory function
word_count = defaultdict(int)

# Counting the occurrences of words
for word in word_list:
    word_count[word] += 1

# Printing the word counts
for word, count in word_count.items():
    print(f"{word}: {count}")

# output =  apple: 3
#           banana: 2
#           orange: 1