'''

Recursion

'''

#print name N times
def print_name(name,n):
    if n==0:
        return
    print('Hi,',name)
    print_name(name,n-1)


# print_name('Arshid',10)

#print n to 1

def print_number(n):
    if n == 0:
        return
    print(n)
    print_number(n-1)
# print_number(4)


#print 1 to n
def print_number(n):
    if n == 0:
        return
    print_number(n-1)
    print(n)
# print_number(4)

#Sum of first N Natural Numbers


def sum_of_natural_numbers(sum,n):
    if n == 0:
        return sum
    sum = sum + n
    return sum_of_natural_numbers(sum,n-1)

print(sum_of_natural_numbers(0,6))
from typing import List

# def printNos(n: int,arr:List = None) -> List[int]: 
#     if arr is None:
#         arr = []
#     if n > 0:
#         printNos(n-1, arr)
#         arr.append(n)
#     return arr
    
# print(printNos(5))








