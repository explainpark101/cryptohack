import math
def get_prime_factors(n) -> dict:
    s = dict()
    while (not(n&0x01)):
        s[2] = s.get(2, 0) + 1 
        n >>= 1
    for i in range(3, math.isqrt(n), 2):
        while (n % i == 0) :
            s[i] = s.get(i, 0) + 1 
            n //= i 
    if (n > 2):
        s[n] = s.get(n, 0) + 1 
    return s

# print(get_prime_factors(134179342789232421234123434123434))
print(get_prime_factors(180834693786027521878872552727))