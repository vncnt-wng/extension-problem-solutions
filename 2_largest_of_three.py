############################
#########  TASK A  #########
############################

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2:
    # num1 is larger than num2 
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    # num2 is larger than num1
    if num2 > num3:
        print(num2)
    else:
        print(num3)

    
#############################
#########  TASK B  ##########
#############################

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2:
    # num1 is larger than num2 
    if num1 > num3:
        # num1 is larger than both num2 and num3, we now need to order num2 and num3 with each other
        if num2 > num3:
            print(num1, num2, num3)
        else:
            print(num1, num3, num2)
    else:
        # num3 > num1, num1 > num2 
        print(num3, num2, num1)
else:
    # num2 is larger than num1
    if num2 > num3:
        # num3 is larger than both num1 and num3, we now need to order num1 and num3 with each other
        if num1 > num3:
            print(num2, num1, num3)
        else:
            print(num2, num3, num1)
    else:
        # num3 > num2, num2 > num1 
        print(num3, num2, num1)
    
    
