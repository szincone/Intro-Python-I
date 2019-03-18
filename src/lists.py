# For the exercise, look up the methods and functions
# that are available for usewith Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print("add 4 to end of list:", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print("combine x w/ y:", x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.pop(4)
print("remove 8 from list:", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(-1, 99)
print("add 99 to second to last position", x)

# Print the length of list x
# YOUR CODE HERE
print("length of x", len(x))
# Print all the values in x multiplied by 1000
# YOUR CODE HER
for num in x:
    print("num multiplied by 1000:", num * 1000)
