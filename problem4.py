# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):
    temp = str(number)
    for i in range(int(len(temp) / 2)):
        if(temp[i] != temp[-(i + 1)]):
            return False
    return True

number = 0
factory1 = 0
factory2 = 0

digitCount = 2

for num1 in range(pow(10, digitCount) - 1, pow(10, digitCount - 1) - 1, -1):
    factory1 = num1
    for num2 in range(pow(10, digitCount) - 1, pow(10, digitCount - 1) - 1, -1):
        factory2 = num2
        number = factory1 * factory2
        if(isPalindrome(number)):
            break
    if(isPalindrome(number)):
        break

print('{} x {} = {}'.format(factory1, factory2, number))