# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

multiplesOf3And5 = list()

for number in range(1000):
    if number % 3 == 0 and number % 5 == 0:
        multiplesOf3And5.append(number)
    elif number % 3 == 0:
        multiplesOf3And5.append(number)
    elif number % 5 == 0:
        multiplesOf3And5.append(number)

# print(*multiplesOf3And5)

sumOfMultiples = sum(multiplesOf3And5)
print('The sum of all the multiples of 3 or 5 below 1000 is {}'.format(sumOfMultiples))