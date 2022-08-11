from random import randint

def MillerRabin(n, rounds):
    """
    Tests n for primality with a number of Miller-Rabin rounds.
    Probability of declaring prime a composite number: 0.
    Upper bound on probability of declaring composite a prime number: (1/4)**rounds.
    """
    if not (n > 3 and n % 2 == 1 and isinstance(rounds, int) and rounds > 0):
        if isinstance(round, int):
            raise TypeError("Number of rounds should be a positive integer.")
        else:
            raise ValueError("Invalid values of the parameters.")
    else:
        p = n - 1
        p1 = p
        k = 0
        while p1 % 2 == 0:
            k = k + 1
            p1 = p1 // 2
        print(p1, k)    
        for i in range(rounds):
            val = randint(2, p-1)
            c1 = pow(val, p1, n)
            if c1 != 1:
                for j in range(k):
                    c = pow(val, 2**j*p1, n)
                    if c == n - 1:
                        break
                    else:
                        if j == k - 1:
                            print("The number", n, "is composite.")
                            return
        print("The number\n", n, "\nis a prime with accuracy ", 1-(0.25)**rounds)
        return

MillerRabin(170141183460469231731687303715884105727,11)

