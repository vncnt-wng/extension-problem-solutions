number = int(input())

new_number = 0
while number > 0:
    # 'Shift' new number one place to the left
    new_number = new_number * 10
    # Get a single digit from number, add in units column of new_number
    new_number += number % 10
    # 'Shift' old number one place to the right
    number = number // 10

print(new_number)