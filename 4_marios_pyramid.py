############################
#########  TASK A  #########
############################

### SOLUTION 1 - two for loops

height = int(input("Height: "))

for i in range(0, height):
    for j in range(i, height - 1):
        print(" ", end="")
    for j in range(0, i + 1):
        print("#", end="")
    print()
    
    
### SOLUTION 2 - conditional 
    
for i in range(0, height):
    for j in range(0, height):
        if j < height - i - 1:
            print(" ", end="")
        else:
            print("#", end="")
    print()
    
    
### SOLUTION 3 - python string shortcuts

for i in range(0, height):
    print(" " * (height - i - 1), end="")
    print("#" * (i + 1), end="")
    print()
    


############################
#########  TASK B  #########
############################


### SOLUTION 1 - for loops 

for i in range(0, height):
    # Left side of pyramid 
    for j in range(i, height - 1):
        print(" ", end="")
    for j in range(0, i + 1):
        print("#", end="")
    
    # Gap in the middle         
    for j in range(0, 2):
        print(" ", end="")
        
    # Right side of pyramid 
    for j in range(0, i + 1):
        print("#", end="")
    for j in range(i, height - 1):
        print(" ", end="")
    print()
    


### SOLUTION 2 - python string shortcuts

for i in range(0, height):
    # Left side of pyramid 
    print(" " * (height - i - 1), end="")
    print("#" * (i + 1), end="")
    
    # Gap in the middle         
    print(" " * 2, end="")
        
    # Right side of pyramid 
    print("#" * (i + 1), end="")
    print(" " * (height - i - 1), end="")
    
    print()
    