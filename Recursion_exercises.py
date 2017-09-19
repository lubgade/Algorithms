# Multiples of 3 f(n) = 3 * n
def mult_3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    else:
        return mult_3(n-1) + 3

print "Multiples of 3"
for i in range(1, 11):
    print mult_3(i)


# sum of first n integers
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)

print "\n\nSum of first n integers"
for i in range(1, 11):
    print sum_n(i)


# Pascal's triangle
def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        print "current previous_line at: %s" % previous_line
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

print "\nPascal triangle"
for i in range(1, 7):
    print(pascal(i))


# Pascal's triangle - list comprehension
def pascal2(n):
    if n == 1:
        return [1]
    else:
        p_line = pascal2(n-1)
        line = [p_line[i]+p_line[i+1] for i in range(len(p_line)-1)]
        line.insert(0,1)
        line.append(1)

    return line

print "\nPascal triangle - line comprehension"
for i in range(1, 7):
    print(pascal2(i))


def f(x):
    print "x is: %s" % x

    def g(y):
        print "y is: %s" % y
        return y + x + 3
    return g

nf1 = f(3)
#nf2 = f(3)

print(nf1(1))
#print(nf2(1))


def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x ** 2 + b * x + c

    return polynomial


p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

print p1(1)
print p2(1)


def polynomial_creator(*coefficients):
    """ coefficients are in the form a_0, a_1, ... a_n
    """

    def polynomial(x):
        res = 0
        for index, coeff in enumerate(coefficients):
            res += coeff * x ** index
        return res

    return polynomial


p1 = polynomial_creator(4)
p2 = polynomial_creator(2, 4)
p3 = polynomial_creator(2, 3, -1, 8, 1)
p4 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x), p3(x), p4(x))