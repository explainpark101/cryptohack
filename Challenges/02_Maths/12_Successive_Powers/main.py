def gcd(a:int, b:int, printing=False) -> int:
    if b == 0:
        return a
    q, r = divmod(a, b)
    if printing: print(f"({r=:5}) = ({a=:5}) - ({b=:5}) * ({q=:5})")
    return gcd(b, r)

ints = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
x:int
p:int
"""
ints are [x**(n+i) (mod p) for i in range(1, 13)]


We know that max(ints) = 851 < p;
because of modulo arithmetic.

588 = x**(n   ) (mod p)
665 = x**(n+1 ) (mod p)
216 = x**(n+2 ) (mod p)
113 = x**(n+3 ) (mod p)
642 = x**(n+4 ) (mod p)
  4 = x**(n+5 ) (mod p)
836 = x**(n+6 ) (mod p)
114 = x**(n+7 ) (mod p)
851 = x**(n+8 ) (mod p)
492 = x**(n+9 ) (mod p)
819 = x**(n+10) (mod p)
237 = x**(n+11) (mod p)

4 * x === 836 (mod p)
=> x === 209 (mod p)

Now, we kwow that x is 209, 
    we can change the equation by
114 === 836 * 209 (mod p)
851 === 114 * 209 (mod p)
then, (836 * 209 - 114 === 0 (mod p)) and (114 * 209 - 851 === 0 (mod p))
so, gcd of  (836 * 209 - 114) and (114 * 209 - 851) could be p's multiple
=> gcd(174610, 22975) = 4595 = 5 * 919
Since 919 is prime number and 3-digit integer, p is 919

then, x=209, p=919

flag would be "crypto{919,209}"


"""
for i in range(len(ints)-1):
    print(f"ints[{i+1}] % ints[{i}] = {ints[i+1] % ints[i]} ")