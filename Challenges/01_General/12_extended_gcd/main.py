def gcd(a, b):
    while a >= b:
        a -= b
    if a == 0: return b
    return gcd(b, a)


def main():
    p = 26513
    q = 32321
    # p * u + q * v = gcd(p, q)
    print(gcd(p, q))
    ...

if __name__ == '__main__':
    main()