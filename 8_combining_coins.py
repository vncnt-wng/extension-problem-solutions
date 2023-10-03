pence = int(input())

# variable keeping track of the number of coins used 
count = 0 

while pence > 0:
    if pence >= 50:
        pence -= 50
    elif pence >= 20:
        pence -= 20
    elif pence >= 10:
        pence -= 10
    elif pence >= 5:
        pence -= 5
    elif pence >= 2:
        pence -= 2
    else:
        pence -= 1
    count += 1

print(count)