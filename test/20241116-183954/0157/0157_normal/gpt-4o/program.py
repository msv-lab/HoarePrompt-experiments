# Read input values
a = int(input())
b = int(input())
c = int(input())

# Calculate the maximum number of lemons that can be used
# It must satisfy the condition that there are 2 apples for each lemon
# and 4 pears for each lemon.
max_lemons = min(a, b // 2, c // 4)

# Calculate the total number of fruits used in the compote
total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4

# Print the result
print(total_fruits)
