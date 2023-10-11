############################
#########  TASK A  #########
############################

elements = [1, 5, 2, 7, 9, 20, 11]

# Temporary variable to store the value of the largest element seen so far in the list
largest = elements[0]

for i in range(1, len(elements)):
    if elements[i] > largest:
        largest = elements[i]
    
print(largest)


############################
#########  TASK B  #########
############################

elements = [1, 5, 2, 7, 9, 20, 11]

largest = elements[0]
largest_index = 0
smallest = elements[0]
smallest_index = 0

for i in range(1, len(elements)):
    if elements[i] > largest:
        largest = elements[i]
        largest_index = i
    elif elements[i] < smallest:
        smallest = elements[i]
        smallest_index = i
    
print(f"{smallest}, {smallest_index}")
print(f"{largest}, {largest_index}")