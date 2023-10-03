bracket_string = input()
bracket_depth = 0

for bracket in bracket_string:
    if bracket == "(":
        bracket_depth += 1
    elif bracket == ")":
        bracket_depth -= 1
        
    if bracket_depth < 0:
        # if bracket_depth is less than 0, it means we have encountered an unopened close bracket
        break
    
if bracket_depth == 0:
    print("balanced")
else:
    # if bracket_depth is not 0 at this point, either we have broken out of the loop and it is negative, 
    # or we have finished the loop it is positive and it is positive (we have unclosed open brackets)
    print("not balanced")