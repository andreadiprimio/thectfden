from ExtendedEuclid import ExtendedEuclid
from math import lcm

def CRT(rhsList, remsList):
    """
    Solves a system of modular equations, given the rhs and the moduli.
    Moduli have to be pairwise coprime.
    """
    if len(rhsList) != len(remsList):
        raise ValueError("Lists should have the same length.")
    remProd = 1
    remLCM = 1
    solution = 0
    for i in range(len(remsList)):
        remProd = remProd * remsList[i]
        remLCM = lcm(remLCM, remsList[i])
    if remLCM != remProd:
        raise ValueError("Moduli have to be pairwise coprime.")
    for j in range(len(remsList)):
        partialProd = remProd // remsList[j]
        _, x, _ = ExtendedEuclid(partialProd, remsList[j])
        solution = solution + rhsList[j]*partialProd*x
    return solution % remProd

# print(CRT([0,3,4], [3,4,5]))
# Extension to fix non pairwise moduli and reduce equations -> locate non-unitary gcds may be expensive.
