import errors
import sys

class XOR():
    
    """
    Bitwise XOR cipher.
    """

    def __init__(self, key = "key"): # sets key and useful variables
        try:
            self.__key = str(key)
            self.__keySize = len(self.__key)
        except TypeError:
            print("[XOR Cipher Error] Key should be a string (or convertible).")
            sys.exit(1)
        

    def encrypt(self, string, results=True):
        try:
            self.__plaintext = str(string)
            self.__ciphertext = ""
        except TypeError:
            print("[XOR Cipher Error]: Plaintext must be a string (or convertible).")
            sys.exit(1)
        for i in range(len(self.__plaintext)):
            idx = i % self.__keySize
            p = self.__plaintext[i]
            k = self.__key[idx]
            ch = chr(ord(p) ^ ord(k))
            self.__ciphertext = self.__ciphertext + ch
        if results:
            self.__cipherPrint()
        return self.__ciphertext

    def decrypt(self, string, results=True):
        try:
            self.__ciphertext = str(string)
            self.__plaintext = ""
        except TypeError:
            print("[XOR Cipher Error]: Plaintext must be a string (or convertible).")
            sys.exit(1)
        for i in range(len(self.__ciphertext)):
            idx = i % self.__keySize
            p = self.__ciphertext[i]
            k = self.__key[idx]
            ch = chr(ord(p) ^ ord(k))
            self.__plaintext = self.__plaintext + ch
        if results:
            self.__cipherPrint()
        return self.__plaintext
    
    def __cipherPrint(self):
        print("+--------------------+")
        print("| XOR Cipher Results |")
        print("+--------------------+")
        print("Ciphertext: " + self.__ciphertext)
        print("Plaintext: " + self.__plaintext)
        return
        
#c = XOR()
#s = "testsentencewithoutspaces"
#c.decrypt(c.encrypt(s))
# This cipher does not bypass chars since it is usually done this way. However, it can be easily implemented a set of bypass chars like in Caesar Cipher.