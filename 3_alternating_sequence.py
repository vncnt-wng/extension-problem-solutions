############################
#########  TASK A  #########
############################

num1 = int(input())
num2 = int(input())
num3 = int(input())

# Store the value of the current highest number we have reached in the sequence
curr = num3

# Calculate the two differences 
diff1 = num2 - num1
diff2 = num3 - num2 

for i in range(0, 3):
    curr = curr + diff1
    print(curr)
    curr = curr + diff2
    print(curr)
    
    
############################
#########  TASK B  #########
############################

num1 = int(input())
num2 = int(input())
num3 = int(input())

# The difference between all the odd terms of the sequence
step = num3 - num1

# The 101st term in the sequence is the 51st odd term of the sequence 
# We can get the 101st term by adding 50 "steps" to num1

term = num1 + step * 50
print(term)
