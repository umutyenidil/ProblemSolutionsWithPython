# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def isPrime(number):
    if(number <= 1):
        return False

    for n in range(number - 1, 1, -1):
        if number % n == 0:
            return False
    return True


primeNumbers = list()

temp = primeLen = 10001
counter = 0

while True:
    counter += 1
    if isPrime(counter):
        primeNumbers.append(counter)
        temp -= 1
    if temp == 0:
        break


print('{}th prime number is {}'.format(primeLen, primeNumbers[-1]))
    


