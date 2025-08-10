# Step 1 —  empty list
my_list = []

print("Step 1:", my_list)   # Output: []
# It's an empty box.

# Step 2 — add 10, 20, 30, 40 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("Step 2:", my_list)   # Output: [10, 20, 30, 40]
# append() puts a value at the end.


# Step 3 — insert 15 at the second position (index 1)
my_list.insert(1, 15)

print("Step 3:", my_list)   # Output: [10, 15, 20, 30, 40]
# insert(index, value) puts the value at that spot and shifts the rest right.

# Step 4 — add several items at once
my_list.extend([50, 60, 70])

print("Step 4:", my_list)   # Output: [10, 15, 20, 30, 40, 50, 60, 70]
# extend() takes another list and adds its items one by one.

# Step 5 — remove the last item
my_list.pop()

print("Step 5:", my_list)   # Output: [10, 15, 20, 30, 40, 50, 60]
# pop() with no arguments removes and returns the last item.

# Step 6 — sort the list smallest → largest
my_list.sort()
print("Step 6:", my_list)   # Output: [10, 15, 20, 30, 40, 50, 60]
# sort() arranges numbers (or strings) in order.

# Step 7 — find where 30 is in the list
index_of_30 = my_list.index(30)
print("Step 7: Index of 30:", index_of_30)  # Output: 3
# index() returns the position; counting starts at 0, so 3 means the 4th spot.
