from . import errors
import sys 
import re

class VigenereCipher():

    """
    Vigenere Cipher.
    By default, it works with the standard lowercase English alphabet, bypassing numbers and whitespaces.
    """

    def __init__(self, key = "key", autokey = False): # sets key and useful variables
        try:
            key = str(key)
            autokey = bool(autokey)
        except ValueError:
            print("[Vigenere Cipher Error] Key should be a string and autokey a boolean.")
            sys.exit(1)
        self.__bypassSet = {' ','0','1','2','3','4','5','6','7','8','9'}
        self.__alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.__alphabetSize = 26  
        self.__keySize = int()  
        self.__key = self.__getKeyData(key)
        self.__autokey = autokey
        
    def __getKeyData(self, key):
        if key == "":
            raise errors.InvalidLengthError("Key should be at least one character long.")
        else:
            keyList = []
            for ch in key:
                if ch not in self.__bypassSet:
                    try:
                        keyList.append(self.__alphabet.index(ch))
                    except ValueError:
                        print("[Vigenere Cipher Error] Cannot build key. Character", ch, "does not appear in alphabet.")
                        sys.exit(1)
            self.__keySize = len(keyList)
            return keyList

    def setKey(self, key): # sets key
        try:
            self.__key = self.__getKeyData(key) 
        except ValueError:
            print("[Vigenere Cipher Error] Key must be a string.")
            sys.exit(1)

    def setAlphabet(self, alphabet): # sets alphabet
        try:
            self.__alphabet = str(alphabet)
            print("Alphabet set to " + self.__alphabet + ".")
        except ValueError:
            print("[Vigenere Cipher Error]: Alphabet must be a string (or convertible).")
            sys.exit(1)
        self.__alphabet = ""
        s = set()
        for ch in str(alphabet):
            s.add(ch)
        self.__alphabetSize = len(self.__alphabet)
        for ch in s:
            self.__alphabet = self.__alphabet + ch
        
    def insertBypass(self, ch):
        try:
            if (len(ch) == 1):
                self.__bypassSet.add(str(ch))
            else:
                raise errors.InvalidLengthError("[Vigenere Cipher Error] The string (or convertible) should consist of a single character.")
        except ValueError:
            print("[Vigenere Cipher Error] The argument should be a string (or convertible).")
            sys.exit(1)
    
    def removeBypass(self, ch):
        try:
            if (len(ch) == 1):
                self.__bypassSet.remove(str(ch))
            else:
                raise errors.InvalidLengthError("[Vigenere Cipher Error] The string (or convertible) should consist of a single character.")
        except ValueError:
            print("[Vigenere Cipher Error] The argument should be a string (or convertible).")

    def encrypt(self, string, results=True):
        try:
            self.__plaintext = str(string)
            self.__ciphertext = ""
        except ValueError:
            print("[Vigenere Cipher Error]: Plaintext must be a string (or convertible).")
            sys.exit(1)
        if self.__autokey:
            apdx = self.__getKeyData(self.__plaintext)
            self.__key = self.__key + apdx
            self.__keySize = len(self.__key)
        bypassCtr = 0
        for i in range(len(self.__plaintext)):
            ch = self.__plaintext[i]
            new_ch = ''
            if ch not in self.__bypassSet:
                bln = ch.isupper()
                ch = ch.lower()
                try:
                    idx = self.__alphabet.index(ch)
                    if self.__autokey:
                        idx2 = (i - bypassCtr)
                    else:
                        idx2 = (i - bypassCtr) % self.__keySize
                    if bln:
                        new_ch = self.__alphabet[(idx + self.__key[idx2]) % self.__alphabetSize].upper()
                    else: 
                        new_ch = self.__alphabet[(idx + self.__key[idx2]) % self.__alphabetSize]
                except ValueError:
                    new_ch = ch 
                    print("[Vigenere Cipher Warning] Bypassed character ", ch, " not in alphabet.")
            else:
                new_ch = ch
                bypassCtr = bypassCtr + 1
            self.__ciphertext = self.__ciphertext + new_ch
        if results:
            self.__cipherPrint()
        return self.__ciphertext

    def decrypt(self, string, results=True):
        try:
            self.__ciphertext = str(string)
            self.__plaintext = ""
        except ValueError:
            print("[Vigenere Cipher Error]: Ciphertext must be a string (or convertible).")
            sys.exit(1)
        bypassCtr = 0
        for i in range(len(self.__ciphertext)):
            ch = self.__ciphertext[i]
            new_ch = ''
            if ch not in self.__bypassSet:
                bln = ch.isupper()
                ch = ch.lower()
                try:
                    idx = self.__alphabet.index(ch)
                    if self.__autokey:
                        idx2 = (i - bypassCtr)
                    else:
                        idx2 = (i - bypassCtr) % self.__keySize
                    if bln:
                        new_ch = self.__alphabet[(idx - self.__key[idx2]) % self.__alphabetSize].upper()
                    else: 
                        new_ch = self.__alphabet[(idx - self.__key[idx2]) % self.__alphabetSize]
                    if self.__autokey:
                        self.__key.append((idx - self.__key[idx2]) % self.__alphabetSize)
                except ValueError:
                    new_ch = ch 
                    bypassCtr = bypassCtr + 1
                    print("[Vigenere Cipher Warning] Bypassed character ", ch, " not in alphabet.")                  
            else:
                new_ch = ch
                bypassCtr = bypassCtr + 1
            self.__plaintext = self.__plaintext + new_ch
        if results:
            self.__cipherPrint()
        return self.__plaintext

    def __cipherPrint(self):
        print("+-------------------------+")
        print("| Vigenere Cipher Results |")
        print("+-------------------------+")
        print("Ciphertext: " + self.__ciphertext)
        print("Plaintext: " + self.__plaintext)
        return

    def kasiskiAttack(self, string, n, filename = ""):
        try:
            n = int(n)
            if n < 2:
                raise TypeError
            self.__ciphertext = str(string)
            self.__plaintext = ""
        except ValueError:
            print("[Vigenere Cipher Error] Ciphertext should be a string (or convertible) and length a positive integer.") 
            sys.exit(1)
        pattern = r'(?=(.{' + str(n) + r'})(.*?)\1)'
        match = re.findall(pattern, string)
        if filename != "":
            f = open(filename, 'a')  
        for i in range(len(match)):
            match[i] = [match[i][0], len(match[i][1]) + 1]
            if filename != "":
                f.write(match[i])
                f.write('\n')
            else:
                print(match[i])
        return match

        



#p = "isvf yi eyfir yai khne ioxtn1234"
#s = "Isvf is rrpsi fds Kaco Gmnhp1234"
#CC = VigenereCipher("worm", autokey=True)
#CC.kasiskiAttack("eiwemc kj rwx gjfpi ht eiwemciiyeam", 6)
#CC.decrypt(p)