from ..crypto.MonoalphabeticCipher import MonoalphabeticCipher

permArray = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
MC = MonoalphabeticCipher(permArray)
MC.decrypt("zzzzzzzzzzzabccccwwywxzx")
MC.frequencyAttack("zzzzzzzzzzzabccccwwywxzx")
guess = "_________________________a"
print(MC.guessKey(guess, "zzzzzzzzzzzabccccwwywxzx"))