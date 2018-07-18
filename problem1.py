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
    # ideal solution
    n = n - 1
    n3 = n // 3     # number of multiples of 3 under n
    n5 = n // 5     # number of multiples of 5 under n
    n15 = n // 15   # number of multiples of 15 under n
    # 1 + 2 + 3 ... n = (n * n - 1) // 2
    sum3 = 3 * (n3 * (n3 + 1)) // 2
    sum5 = 5 * (n5 * (n5 + 1)) // 2
    sum15 = 15 * (n15 * (n15 + 1)) // 2
    return sum3 + sum5 - sum15


print(SumOfMultiOf3And5(int(input())))
