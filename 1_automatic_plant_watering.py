water = input("Water sensor: ")
light = input("Light sensor: ")
temp = input("Temp sensor: ")

if water == "LOW":
    if light == "LOW" or temp == "LOW":
        print("MEDIUM")
    elif light == "HIGH" and temp == "HIGH":
        print("HIGH")
elif water == "HIGH": 
    print("LOW")
    
    
    
    
# note - assuming the only possible values for the inputs are "LOW" or "HIGH" we could simplify two of the conditions like so 

if water == "LOW":
    if light == "LOW" or temp == "LOW":
        print("MEDIUM")
    else:
        print("HIGH")
else: 
    print("LOW")