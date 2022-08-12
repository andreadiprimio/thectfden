# The CTF Den

A collection of CTF resources in ever growing shape (Python and C++ only). May not be _fully_ optimized...bear with me.

## The `ntUtils` folder
The `ntUtils` folder contains the following subroutines:
- `ExtendedEuclid` solves any linear 2-variable diophantine equation.
- `CRT` solves any system of modular equations by means of the CRT theorem.
- `MillerRabin` is a stochastic test for primality.

## The `symCipher` folder
The `symCipher` folder contains some symmetric ciphers:
- `CaesarCipher` implements a shift cipher for any alphabet.
    - Contains a simple bruteforce attack.
- `VigenereCipher` implements a shift cipher with multiple keys.
    - (WIP) Contains the Kariski attack.
- `XOR` implements a XOR cipher.
- `MonoalphabeticCipher` implements a permutation cipher.
    - (WIP) Contains a frequency analysis tool and the Hart attack.

