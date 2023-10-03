############################
#########  TASK A  #########
############################

n = int(input())

prevprev = 1 
prev = 2 

curr = prevprev + prev

for i in range(0, n - 3):
    prevprev = prev 
    prev = curr 
    curr = prevprev + prev

print(curr)


############################
#########  TASK B  #########
############################

max_fib = int(input())

prevprev = 1 
prev = 2 
total = 3

while prevprev + prev < max_fib:
    curr = prevprev + prev
    total += curr
    prevprev = prev 
    prev = curr 

print(total)