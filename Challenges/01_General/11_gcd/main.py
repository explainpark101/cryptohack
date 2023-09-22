def gcd(a, b):
    while a >= b:
        a -= b
    print(f"{a=} {b=}")
    if a == 0: return b
    return gcd(b, a)

def main():
    a = 66528
    b = 52920
    print(gcd(a, b))

if __name__ == "__main__":
    main()