palindrome = input()

valid = True 

for i in range(0, len(palindrome)//2):
    if palindrome[i] != palindrome[len(palindrome) - i - 1]:
        valid = False 
        break

if valid:
    print("Valid palindrome")
else:
    print("Not valid")