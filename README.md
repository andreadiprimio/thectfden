# The CTF Den

A collection of CTF resources in ever growing shape (Python and C++ only). May not be _fully_ optimized...bear with me.

## The `tools` folder
The `tools` folder contains the following subroutines:
- `ExtendedEuclid` solves any linear 2-variable diophantine equation.
- `CRT` solves any system of modular equations by means of the CRT theorem.
- `MillerRabin` is a stochastic test for primality.
- `FrequencyAnalyzer` analyzes character frequency of a string.

## The `crypto` folder
The `crypto` folder contains the following ciphers:
- `CaesarCipher` implements a shift cipher for any alphabet.
    - Contains a simple bruteforce attack.
- `VigenereCipher` implements a shift cipher with multiple keys.
    - Contains setup for the Kariski attack.
- `XOR` implements a XOR cipher.
- `MonoalphabeticCipher` implements a permutation cipher.
    - Contains interface for attacks via frequency analysis and the Hart attack.
- ``

## The `test` folder
The `test` folder contains some examples of driver code for using this library. Run the examples as follows:

`python3 -m thectfden.test.filename`

from outside the project.

