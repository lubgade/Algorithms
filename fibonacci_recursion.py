# find the fibonacci series for n nos without duplicates

def fib_m(n):
    # using a dictionary to remember previously calculated values to avoid
    # duplicates
    memo = {0:0, 1:1}
    if not n in memo:
        memo[n] = fib_m(n-1) + fib_m(n-2)

    return memo[n]

for i in range(1, 11):
    print fib_m(i)
