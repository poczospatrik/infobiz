from random import randint
from fractions import Fraction

def titkosit(a, S, n):
    shares = []
    for i in range(1, n + 1):
        summa = S
        for j in range(len(a)):
            summa += a[j] * (i ** (j + 1))
        shares.append((i, summa))
    return shares

def lagrange_interpolacio(x, y, t):
    def L(j, x_i):
        lj = Fraction(1)
        for m in range(t):
            if m != j:
                lj *= Fraction(x_i - x[m], x[j] - x[m])
        return lj
    
    summa = Fraction(0)
    for j in range(t):
        lj = L(j, 0)
        summa += y[j] * lj
    return summa

def visszafejt(shares, h, t):
    x = h
    y = [shares[i-1][1] for i in h]
    return lagrange_interpolacio(x, y, t)


if __name__ == "__main__":
    n = 10
    S = randint(1000, 9999)
    t = 6
    holders = [1,4,5,7,8,9]

    a = [randint(2, 10) for i in range(t - 1)]

    print("Titok:", S)

    shares = titkosit(a, S, n)
    print("Reszesedesek:", shares)

    visszafejtett_titok = visszafejt(shares, holders, t)
    print("Visszafejtett titok:", round(visszafejtett_titok))
