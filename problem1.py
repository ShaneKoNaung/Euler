'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def SumOfMultiOf3And5(n):
    '''
    return the sum of multiples of 3 and 5 below n
    args:
        n : int
    ret:
        int
    '''
    n = n - 1    # the sum is below n
    n3 = n // 3  # number of multiples of 3 below n
    n5 = n // 5  # number of multiples of 5 below n
    n15 = n // 15   # number of multiples of 15 below n
    i = 1
    sum3, sum5, sum15 = 0, 0, 0
    while n3 >= i:
        sum3 += i * 3
        i += 1
    i = 1
    while n5 >= i:
        sum5 += i * 5
        i += 1
    i = 1
    while n15 >= i:
        sum15 += i * 15
        i += 1
    print(sum3, sum5, sum15)
    return sum3 + sum5 - sum15


print(SumOfMultiOf3And5(int(input())))
