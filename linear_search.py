############################
#########  TASK A  #########
############################

### Task A with while loop 

search_list = [1, 8, 2, 7, 10, 9]
search_elem = int(input())

index = 0 
flag = False

while index < len(search_list):
    if search_list[index] == search_elem:
        flag = True
        break
    index += 1

if flag == False:
    print("-1")
else:
    print(index)


### Task A with for loop 


search_list = [1, 8, 2, 7, 10, 9]
search_elem = int(input())

for i in range(0, len(search_list)):
    if search_list[i] == search_elem:
        print(i)
        break

if flag == False: 
    print("-1")

############################
#########  TASK B  #########
############################


search_list = []

# Fist line of input is length of list
search_list_length = int(input())

# get each element as input, append to the list
for i in range(search_list_length):
    search_list.append(int(input()))

print(search_list)

# get the search term
search_elem = int(input())

index = 0 

while index < len(search_list):
    if search_list[index] == search_elem:
        flag = True
        break
    index += 1

if flag == False:
    print("-1")
else:
    print(index)
