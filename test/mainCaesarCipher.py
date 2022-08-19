from ..crypto.CaesarCipher import CaesarCipher

s = "tlla tl hmaly Aol Avnh Whyaf1234"
CC = CaesarCipher(7)
CC.setAlphabet(6)
CC.decrypt(s)
l = CC.bruteforceAttack(s)
print(l)