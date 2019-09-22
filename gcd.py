def gcd(a,b):

    """
    returns the gcd of a and b

    """

    while b > 0:
        a, b = b, a % b

    return a
print(gcd(20,50))
print(gcd(120,80))
