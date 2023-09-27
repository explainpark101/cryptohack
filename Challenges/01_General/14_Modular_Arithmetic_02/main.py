def main():
    p = 65537
    calc = "273246787654 ** 65536"
    """
    # Fermat's little theorem
    
    if gcd(a, p) == 1:
        a**(p-1) === 1 (mod p)


    # Euler's Theorem
    
    if gcd(a, n) === 1:
        a ** ( phi(n) ) === 1 (mod n)
    // phi(n) <== euler's totient function
    """

    
    
    
    print(p - 65537) # this is 1. So, answer must be 1
    
if __name__ == "__main__":
    main()