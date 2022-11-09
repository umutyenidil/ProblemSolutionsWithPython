# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def ekok(number1, number2):
    bigNumber = 0
    smallNumber = 0
    if (number1 > number2):
        bigNumber = number1
        smallNumber = number2
    else:
        bigNumber = number2
        smallNumber = number1

    ebob = 1
    for i in range(1, smallNumber + 1):
        if (bigNumber % i == 0) and (smallNumber % i == 0):
            ebob = i

    temp = int((bigNumber * smallNumber) / ebob) 
    return temp

     

lowerLimit = 1
upperLimit = 20

result = 1
for i in range(lowerLimit, upperLimit + 1):
    result = ekok(result, i)

print(result)