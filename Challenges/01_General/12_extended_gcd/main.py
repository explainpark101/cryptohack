from math import prod

def extended_gcd(a:int, b:int) -> tuple[int, int, int]:
    """
    @returns gcd, s, t
    """
    if b == 0:
        return a, 0, 1
    q, r = divmod(a, b)
    gcd, s, t = extended_gcd(b, r)
    s, t = t - q*s, s ### <<<< needed to be understood
    print(f"({r=:5}) = ({a=:5}) - ({b=:5}) * ({q=:5}) | {s=:6} {t=:6}")
    return gcd, s, t
    
    
def gcd_default(a:int, b:int, _print=False) -> int:
    if b == 0:
        return a
    q, r = divmod(a, b)
    if _print: print(f"({r=:5}) = ({a=:5}) - ({b=:5}) * ({q=:5})")
    return gcd_default(b, r)
# a_n - a_n-1 * q_n = a_n-2
# a_n-1 - a_n-2 * q_n-1 = a_n-3

# a_n = b_n-1 = r_n-2


def main():
    p = 26513
    q = 32321
    p, q = q, p
    print(gcd_default(p, q))
    print(f"{p=:5} {q=:4}")
    gcd, s, t = extended_gcd(p, q)
    print(f"{gcd=:3} {s=:4} {t=:4} | {p*t + q*s}")

    print(min(s, t))
    
    # p * u + q * v = gcd(p, q)

if __name__ == '__main__':
    main()