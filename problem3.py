# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

ourNumber = 600851475143

primeFactors = list()



def isPrime(number):
    if(number <= 1):
        return False

    for n in range(number - 1, 1, -1):
        if number % n == 0:
            return False
    return True



for number in range(ourNumber, 0, -1):
    if 13195 % number == 0:
        if isPrime(number):
            primeFactors.append(number)
print(*primeFactors)
print('{} is largest prime factory of the number {}'.format(primeFactors[0], ourNumber))

