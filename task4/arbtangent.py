import decimal

def factorial(x):
    if x == 2:
        return x
    elif x < 2:
        return 1 
    else:
        return factorial(x-1)*x

a, e = input(), int(input())
decimal.getcontext().prec = e+10
a = decimal.Decimal(a)

prevpi = decimal.Decimal(10)
pi = decimal.Decimal(0)
k = 0
num = decimal.Decimal(640320*640320*640320).sqrt()/12
while prevpi != pi:
    prevpi = pi
    pi = prevpi + decimal.Decimal(factorial(6*k)*(13591409 + 545140134*k))/decimal.Decimal(factorial(3*k)*(factorial(k)**3)*(-262537412640768000)**k)
    k += 1
pi = num/pi

a *= pi / 200


addsin = a
addcos = 1
k = 1
prevsin = 10
sin = decimal.Decimal(0)
prevcos = 10
cos = decimal.Decimal(0)

while prevsin != sin or prevcos != cos:
    prevsin = sin
    sin = prevsin + addsin
    addsin *= -a*a/((k+1)*(k+2))

    prevcos = cos
    cos = prevcos + addcos
    addcos *= -a*a/((k)*(k+1))
    k += 2

decimal.getcontext().prec = e
print(sin/cos)
