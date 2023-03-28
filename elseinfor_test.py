numbers = [2, 4, 6, 8, 10]
target = 5

for number in numbers:
    if number == target:
        print(f"Found {target} in the list.")
        break
else:
    print(f"{target} was not found in the list.")

# output = 5 was not found in the list.