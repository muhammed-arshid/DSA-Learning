''' 1 - 
        *****
        *****
        *****
        *****
        *****
 
 '''
# #logic 1
# # O(N^2)
# num_of_steps = int(input())
# for i in range  (0,num_of_steps):
#     for j in range(0,num_of_steps):
#         print('*', end = " ")
#     print()


# #logic 2
# #O(N)
# row  = '* '*num_of_steps
# for _ in range(num_of_steps):
#     print(row)


'''
    2 - 
    N = 4
    *
    **
    ***
    ****

'''
# # logic 1
# # O(N^2)
# n = int(input())
# for i in range(0,n):
#     for j in range(0,i+1):
#         print('*',end='')
#     print()

# #O(N)   
# def printTriangle (N):
#     for i in range(0,N):
#         print('* '*(i+1))

'''
    3 - 
    N = 4

    1
    1 2
    1 2 3 
    1 2 3 4

'''
# TC  = O(N^2)
# def nTriangle(n:int) ->None:
#     for i in range(0,n):
#         for j in range(1,i+2):
#             print(j, end=' ')
#         print()


'''
    4 - 
    N = 4

    1
    2 2
    3 3 3
    4 4 4 4

'''

# #TC = O(N^2)
# def triangle( n:int) ->None:
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(i, end=' ')
#         print()

# #TC  = O(N)
# def triangle( n:int) ->None:
#     for i in range(1,n+1):
#         print((str(i)+' ')*i)


'''
    5 - 
    N = 3

    * * *
    * *
    *

'''

# #TC = O(N^2)
# def seeding(n: int) -> None:
#     for i in range(0,n+1):
#         for j in range(0,n-i):
#             print('*',end= ' ')
#         print()

# #TC  = O(N)
# def seeding(n: int) -> None:
#     for i in range(0,n+1):
#         print('* '*(n-i))

# seeding(3)

# def nNumberTriangle(n: int) -> None:
#     for i in range(0,n+1):
#         for j in range(1,n-i+1):
#             print(j,end=' ')
#         print()

# nNumberTriangle(3)


#       * 
#     * * *
#   * * * * *



# def nStarTriangle(n: int) -> None:
#     for i in range(0,n):
#         for j in range(1,n-i):
#             print(' ',end='')
#         for k in range(0,2*i+1):
#             print('*',end='')
#         for j in range(1,n-i):
#             print(' ',end='')
#         print()

# nStarTriangle(3)

'''
    Time Complexity - O( N * N )
    Space Complexity - O( 1 )

    where N is the given input.
'''


# def nStarTriangle(n: int) -> None:

#     # Initialise 'gap' and 'stars'.
#     gap = n - 1
#     stars = 1
#     for i in range(n):
#         for j in range(gap):
#             print(' ', end="")
#         for j in range(gap, gap+stars):
#             print('*', end="")

#         # End the current row of the pattern.
#         print()

#         gap -= 1
#         stars += 2

# nStarTriangle(3)

'''
  * * * * *
    * * *
      *
'''

# def nStarTriangle(n: int) -> None:
#     for i in range(0,n):
#         for j in range(0,i):
#             print(' ',end='')
#         for j in range(0,2*(n-i)-1):
#             print('*',end='')
#         print()


# nStarTriangle(3)

'''
      *
    * * *
  * * * * *
  * * * * *
    * * *
      * 

'''
# def nStarDiamond(n: int) -> None:
#     for i in range(0,n):
#         for j in range(1,n-i):
#             print(' ',end='')
#         for k in range(0,2*i+1):
#             print('*',end='')
#         print()
#     for i in range(0,n):
#         for j in range(0,i):
#             print(' ',end='')
#         for k in range(0,2*(n-i)-1):
#             print('*',end='')
#         print()

# nStarDiamond(3)


'''

* 
* * 
* * *
* * 
*

'''

# def nStarTriangle(n: int) -> None:
#     for i in range(0,2*n):
#         if i<=n:
#             for j in range(0,i):
#                 print("* ",end='')
#         else:
#             for j in range(0,2*n-i):
#                 print("* ",end='')
#         print()


# nStarTriangle(3)


'''
N = 4

1
0 1
1 0 1
0 1 0 1


'''

# def nBinaryTriangle(n: int) -> None:
#     start  = 1
#     for i in range(0,n+1):
#         if start == 1:
#             for j in range(0,i):
#                 print(j%2,end=' ')
#             start = 0
#             print()
#         else:
#             for j in range(0,i):
#                 print((j+1)%2,end=' ')
#             print()
#             start= 1



        

# nBinaryTriangle(5)


'''
N = 3

1         1
1 2     2 1
1 2 3 3 2 1 

'''

# def numberCrown(n: int) -> None:
#     for i in range(1,n+1):
#         for j in range(0,i):
#             print(j+1,end='')
#         for k in range(0,2*(n-i)):
#             print(' ',end='')
#         for m in range(i,0,-1):
#             print(m,end='')
#         print()

# numberCrown(5)

'''
1 
2 3
4 5 6 
7 8 9 10

'''

# def nNumberTriangle(n: int) -> None:
#     num = 1
#     for i in range(1,n+1):
#         for j in range(0,i):
#             print(num,end=' ')
#             num += 1
#         print()

# nNumberTriangle(3)


'''
N = 4
A
AB
ABC
ABCD


'''

# def nLetterTriangle(n: int) -> None:
#     for i in range(1,n+1):
#         for j in range(65,65+i):
#             print(chr(j),end=' ')
#         print()

# nLetterTriangle(3)
'''
N = 3
ABC
AB
A

'''

# def nLetterTriangle(n: int):
#     for i in range(0,n+1):
#         for j in range(65,65+(n-i)):
#             print(chr(j),end=' ')
#         print()

# nLetterTriangle(4)
'''
N = 4

A
B B
C C C
D D D D

'''

# def alphaRamp(n: int) -> None:
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print(chr(65+i),end='')
#         print()

# alphaRamp(4)

'''
N = 3
     A
   A B A
  A B C B A


'''

# def alphaHill(n: int):
#     for i in range(1,n+1):
#         for j in range(0,n-i):
#             print(' ',end=' ')
#         for k in range(0,i):
#             print(chr(65+k),end=' ')
#         for k in range(i-1,0,-1):
#             print(chr(64+k),end=' ')
#         print()
# alphaHill(3)       

'''


'''