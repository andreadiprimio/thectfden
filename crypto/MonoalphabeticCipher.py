from . import errors
import sys
from ..tools.FrequencyAnalyzer import FrequencyAnalyzer

class MonoalphabeticCipher():

    """
    Monoalphabetic Cipher.
    By default, it works with the standard lowercase English alphabet, bypassing numbers and whitespaces.
    """

    def __init__(self, key = [i for i in range(26)]): # sets key and useful variables
        self.__alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.__bypassSet = {' ','0','1','2','3','4','5','6','7','8','9'}
        self.__alphabetSize = 26
        self.__key = self.setKey(key)

    def setKey(self, key): # sets key
        try:
            if isinstance(key, list):
                if all(isinstance(element, int) for element in key):
                    if all(element >= 0 for element in key):
                        pass
                    else:
                        raise TypeError
                else:
                    raise TypeError
            else:
                raise TypeError
        except TypeError:
            print("[Monoalphabetic Cipher Error]: Key must be a list of nonnegative integers.")
            sys.exit(1)
        s = set()
        for n in key:
            s.add(n)
        l = len(s)
        m = max(s)
        if l != m+1 or l != self.__alphabetSize:
            raise errors.InvalidPermutationError("Key is not a permutation array fitting the current alphabet.")
        else:
            return key

    def setAlphabet(self, alphabet): # sets alphabet
        try:
            self.__alphabet = str(alphabet)
            print("Alphabet set to " + self.__alphabet + ".")
        except ValueError:
            print("[Monoalphabetic Cipher Error]: Alphabet must be a string (or convertible).")
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
                raise errors.InvalidLengthError("[Monoalphabetic Cipher Error] The string (or convertible) should consist of a single character.")
        except ValueError:
            print("[Monoalphabetic Cipher Error] The argument should be a string (or convertible).")
            sys.exit(1)
    
    def removeBypass(self, ch):
        try:
            if (len(ch) == 1):
                self.__bypassSet.remove(str(ch))
            else:
                raise errors.InvalidLengthError("[Monoalphabetic Cipher Error] The string (or convertible) should consist of a single character.")
        except ValueError:
            print("[Monoalphabetic Cipher Error] The argument should be a string (or convertible).")
            sys.exit(1)

    def encrypt(self, string, results=True):
        try:
            self.__plaintext = str(string)
            self.__ciphertext = ""
        except ValueError:
            print("[Monoalphabetic Cipher Error]: Plaintext must be a string (or convertible).")
            sys.exit(1)
        for ch in self.__plaintext:
            new_ch = ch
            if ch not in self.__bypassSet:
                bln = ch.isupper()
                ch = ch.lower()
                try:
                    idx = self.__alphabet.index(ch)
                    if bln:
                        new_ch = self.__alphabet[self.__key[idx]].upper()
                    else: 
                        new_ch = self.__alphabet[self.__key[idx]]
                except ValueError:
                    new_ch = ch 
                    print("[Monoalphabetic Cipher Warning] Bypassed character ", ch, " not in alphabet.")                
            else:
                new_ch = ch
            self.__ciphertext = self.__ciphertext + new_ch
        if results:
            self.__cipherPrint()
        return self.__ciphertext

    def decrypt(self, string, results=True):
        try:
            self.__ciphertext = str(string)
            self.__plaintext = ""
        except ValueError:
            print("[Monoalphabetic Cipher Error]: Ciphertext must be a string (or convertible).")
            sys.exit(1)
        for ch in self.__ciphertext:
            new_ch = ''
            if ch not in self.__bypassSet:
                bln = ch.isupper()
                ch = ch.lower()
                try:
                    id = self.__alphabet.index(ch)
                    idx = self.__key.index(id)
                    if bln:
                        new_ch = self.__alphabet[idx].upper()
                    else: 
                        new_ch = self.__alphabet[idx]
                except:
                    new_ch = ch 
                    print("[Monoalphabetic Cipher Warning] Bypassed character ", ch, " not in alphabet.")                  
            else:
                new_ch = ch
            self.__plaintext = self.__plaintext + new_ch
        if results:
            self.__cipherPrint()
        return self.__plaintext

    def __cipherPrint(self):
        print("+-------------------------------+")
        print("| Monoalphabetic Cipher Results |")
        print("+-------------------------------+")
        print("Ciphertext: " + self.__ciphertext)
        print("Plaintext: " + self.__plaintext)
        return

    def frequencyAttack(self, string):
        res = FrequencyAnalyzer(string)
        return res

    def guessKey(self, guess, string):
        if not (isinstance(guess, (list, str)) and isinstance(string, str) and len(guess) == len(self.__alphabet)):
            raise TypeError('[Monoalphabetic Cipher Error] Inappropriate parameter choice.')
        else:
            guessSol = ""
            for ch in string:
                if ch == '_' or ch == ' ' or ch in self.__bypassSet:
                    guessSol = guessSol + ch
                elif ch in self.__alphabet:
                    idx = self.__alphabet.index(ch)
                    guessSol = guessSol + guess[idx]
                else:
                    guessSol = guessSol + ch 
                    print("[Monoalphabetic Cipher Warning] Bypassed character ", ch, " not in alphabet.")       
            return guessSol
