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
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


print(SumOfMultiOf3And5(int(input())))
