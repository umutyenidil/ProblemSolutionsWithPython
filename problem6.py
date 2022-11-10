theSumOfTheSquares = 0
theSquareOfTheSum = 0

for item in range(100):
    theSumOfTheSquares += pow(item + 1, 2)

for item in range(100):
    theSquareOfTheSum += item + 1

theSquareOfTheSum = pow(theSquareOfTheSum, 2)

# print(theSumOfTheSquares)
# print(theSquareOfTheSum)

print('{} - {} = {}'.format(theSquareOfTheSum, theSumOfTheSquares, theSquareOfTheSum - theSumOfTheSquares))