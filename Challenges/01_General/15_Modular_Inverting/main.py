"""
e * d = 1 (mod phi(n))

d exists if gcd(e, phi(n)) = 1


phi(n) | ed-1
// we know that (e*d -1) * k = phi(n)
// k is in Integer set


ed - k * phi(n) = 1

so, u = d, v = -k
    in Extended GCD
    >>> gcd(e, phi(n)) = 1 = ed - k * phi(n)
"""


def main():
    for i in range(10000):
        if 3 * i % 13 == 1:
            print(i)
            return
    
if __name__ == "__main__":
    main()