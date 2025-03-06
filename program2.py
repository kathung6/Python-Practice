# creates a list of 1000 elements
primes = list(range(2,1001))

# FUnction: determines if a number is a prime number by
# checking if it is divisible by 
def is_prime(n):
    # anything lower than 0 and 1 is not a prime
    if n <= 1:
        return False
    
    # loops through numbers 2 to sqrt of n
    for i in range(2, int(n **0.5) + 1):
        # returns fals if n is divisile by i
        if n % i == 0:
            return False
    # returns true if no divisors found; n is prie
    return True    

# loops through primes list testing if each number is prime
while True:
    try:
        for i in range(len(primes)):
            if not is_prime(primes[i]):
                # if i is not prime, changes element to False
                primes[i] = False
    except ZeroDivisionError:
        print("Error: cannot divide by 0s")
        
    break

#prints prime numbers
for n in primes:
    if n is not False:
        print(n)