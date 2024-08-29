
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

import math 
def count_digits_opt(n: int) -> int:
    return int(math.log10(n)+1)

#TC O(1)

print(count_digits_opt())
        
