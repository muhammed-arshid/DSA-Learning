
'''
You are given a number ’n’.



Find the number of digits of ‘n’ that evenly divide ‘n’.



Note:
A digit evenly divides ‘n’ if it leaves no remainder when dividing ‘n’.


Example:
Input: ‘n’ = 336

Output: 3

Explanation:
336 is divisible by both ‘3’ and ‘6’. Since ‘3’ occurs twice it is counted two times.
'''

#my solution

def countDigits(n: int) -> int:
    digit = 0
    y = n
    while n > 0:
        r = n%10
        if r != 0:
            if y%r == 0:
                digit = digit + 1
        n = n//10
    return digit

# print(countDigits(373))



# Count digits in a number
'''
Example 1:
Input:N = 12345
Output:5
Explanation:  The number 12345 has 5 digits.
Example 2:
Input:N = 7789
Output: 4
Explanation: The number 7789 has 4 digits.

'''

def count_digits(n: int) -> int:
    digit = 0 
    while n > 0:
        n = n//10
        digit = digit+1
    return digit


'''
TC  LogN
'''

# OPTIMUM SOLUTION

# import math 
# def count_digits_opt(n: int) -> int:
#     return int(math.log10(n)+1)

# #TC O(1)

# print(count_digits_opt())
        

'''
Example 1:
Input:N = 12345
Output:54321
Explanation: The reverse of 12345 is 54321.
Example 2:
Input:N = 7789
Output: 9877
Explanation: The reverse of number 7789 is 9877.

'''


# def reverseNumber(n):
#     rev = 0
#     while n>0:
#         r = n%10
#         rev = rev*10 + r
#         n = n//10
#     return int(rev)

# print(reverseNumber(10400))

#palindrome
# n=int(input())  
# # taking n as a input 

# rev = 0
# t = n
# while n>0:
#     r = n%10
#     rev = rev*10 + r
#     n = n//10
# if t == rev:
#     print("true")
# else:
#     print("false")


# import math
# def checkArmstrong(n):
#     rev = 0
#     temp = n
#     dig = int(math.log10(n)+1)
#     while n >0:
#         r = n%10
#         rev = rev+math.pow(r,dig)
#         n = n//10 
#     if rev == temp:
#         return True
#     else:
#         return False
    

# print(checkArmstrong(371))


#all divisor of n
# from typing import List
# import math
# def printDivisors(n: int) -> List[int]:
#     list_arr = []
#     for i in range(1,int(math.sqrt(n))+1):
#         if n%i == 0:
#             list_arr.append(int(i))
#             if n/i != i:
#                 list_arr.append(int(n/i))
#     list_arr.sort()
#     return list_arr

# print(printDivisors(10))
from typing import List

 

# def printDivisors(n: int) -> List[int]:
#     divisors = set()
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             divisors.add(i)
#             divisors.add(n // i)
#     return sorted(divisors)

 
# print(printDivisors(10))

# def sumOfAllDivisors(n: int) -> int:
#     total = 0
#     for i in range(0,n):
#         ans = 0
#         for j in range(1, int(i**0.5) + 1):
#             if i % j == 0:
#                 ans = ans + j
#                 if i != i//j:
#                     ans = ans + i//j
#         total = total + ans
#     return total


# print(sumOfAllDivisors(5))



#prime number check

# from math import *
# from collections import *
# from sys import *
# from os import *

# ## Read input as specified in the question.
# ## Print output as specified in the question.
# n = int(input())
# i = 1 
# count = 0
# while i*i <= n:
#     if n%i==0:
#         count = count +1
#         if (int(n/i)) != i:
#             count = count + 1
#     i = i +1

# if count == 2:
#     print('YES')
# else:
#     print("NO")


## HCF and GCD

# def gcd_or_hcf(a,b):
#     MAX = 1
#     i = 1
#     while i <= min(a,b):
#         if a%i==0 and b%i==0:
#             if MAX < i:
#                 MAX = i
#         i = i +1
#     print(MAX)

# gcd_or_hcf(7,11)


#equlatral algorithm
'''
ie,
The Euclidean Algorithm is a method for finding the greatest common divisor of two numbers. It operates on the principle that the GCD of two numbers remains the same even if the smaller number is subtracted from the larger number.

To find the GCD of n1 and n2 where n1 > n2:

Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
Once one of them becomes 0, the other number is the GCD of the original numbers.
Eg, n1 = 20, n2 = 15:

gcd(20, 15) = gcd(20-15, 15) = gcd(5, 15)

gcd(5, 15) = gcd(15-5, 5) = gcd(10, 5)

gcd(10, 5) = gcd(10-5, 5) = gcd(5, 5)

gcd(5, 5) = gcd(5-5, 5) = gcd(0, 5)

Hence, return 5 as the gcd.


    better 
    gcd(a,b) == gcd(a%b,b)---> othen of then 0

'''
def gcd_or_hcf(a,b):
    while a>0 and b>0:
        if(a>b):
            a = a%b
        else:
            b=b%a
    if a==0:
        return b
    else:
        return a
print(gcd_or_hcf(7,11))

