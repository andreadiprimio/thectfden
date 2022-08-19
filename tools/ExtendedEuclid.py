def ExtendedEuclid(a, b):
    """
    Solves the equation ax + by = gcd(a,b) for integer a, b, x, y.
    If a and b are coprime, solves ax + by = 1, and jointly ax + by = l for any integer l, just by refactoring.
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Coefficients should be integers.")
    else:
        if a == 0:
            return b, 0, 1        
        gcd, x1, y1 = ExtendedEuclid(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
