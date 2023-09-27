"""
x**2 === a (mod n)

x is Quadratic Residue

// we can use "Tonelli-Shanks algorithm" in modular square root.

https://rkm0959.tistory.com/20
https://sean9892.tistory.com/27
"""


def main():
    p = 29
    ints = [14, 6, 11]
    for i in ints:
        for j in range(10000):
            j = j * j
            if j % p == i and i != j:
                print(f"{i=} {j=}")
                break



if __name__ == '__main__':
    main()

