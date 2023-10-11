############################
#########  TASK A  #########
############################

import math

number = int(input())

primes = [2,3]

# generate primes up to the square root of the number input 
# we don't need to generate primes larger than this
for i in range(4, int(math.pow(number, 1/2))):
    is_prime = True
    for prime in primes:
        if i % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i) 

# Flag to keep track 
number_prime = True

#Iterate through primes, print any prime that is a factor
for prime in primes:
    if number % prime == 0:
        print(prime)
        number_prime = False

# If no primes were factors, the number is prime and so the number itself if the only prime factor
if number_prime:
    print(number)



############################
#########  TASK B  #########
############################

##### FOR TASK B, THE CODE TO GENERATE PRIMES REMAINS THE SAME, only the outputting of factors is different
 
# index for which prime in the list of primes we are looking at
prime_index = 0
# Keep dividing the number by primes that are factors of it until the number reaches 1.
while number != 1: 
    if number % primes[prime_index] == 0:
        number = number // primes[prime_index] 
        print(primes[prime_index])
    # If the number is not divisible by the prime at prime_index, move further on 
    else:
        prime_index += 1

        # If we 'run out' of primes, then the number must be prime
        if prime_index >= len(primes):
            print(number)
            break
