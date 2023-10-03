primes = [2, 3]

for i in range(4, 100):
    # boolean flag to help determine 
    isPrime = True
    
    for prime in primes:
        # iterate through each prime less than i, if i is divisible by any prime, it is not prime so break
        if i % prime == 0:
            isPrime = False 
            break
    
    if isPrime:
        # if the boolean flag is still True, add i to the list of primes
        primes.append(i)
        
        
for prime in primes:
    print(prime)