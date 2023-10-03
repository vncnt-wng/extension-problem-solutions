initial_value = int(input())
prev = initial_value
current_value = int(input())

while current_value > prev:
    prev = current_value
    current_value = int(input())
    
print(current_value - initial_value)