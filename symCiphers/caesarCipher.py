class CaesarCipher():

    """
    Caesar Cipher.
    By default, it works with the standard English alphabet, bypassing numbers and whitespaces.
    """

    def __init__(self, key = 0): # sets key and useful variables
        self.key = key 
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.bypassSet = {' ','0','1','2','3','4','5','6','7','8','9'}
        self.alphabetSize = 26
        
    def setKey(self, key): # sets key
        try:
            key = int(key)
        except ValueError:
            print("[Caesar Cipher Error]: Key must be a positive or negative integer (or convertible).")

    def setAlphabet(self, alphabet): # sets alphabet
        try:
            self.alphabet = str(alphabet)
            self.alphabetSize = len(self.alphabet)
            print("Alphabet set to " + self.alphabet + ".")
        except:
            print("[Caesar Cipher Error]: Alphabet must be a string (or convertible).")

    def insertBypass(self, ch):
        try:
            if (len(ch) == 1):
                self.bypassSet.add(str(ch))
            else:
                raise errors.InvalidLengthError("[Caesar Cipher Error] The string (or convertible) should consist of a single character.")
        except ValueError:
            print("[Caesar Cipher Error] The argument should be a string (or convertible).")
    
    def removeBypass(self, ch):
        try:
            if (len(ch) == 1):
                self.bypassSet.remove(str(ch))
            else:
                raise errors.InvalidLengthError("[Caesar Cipher Error] The string (or convertible) should consist of a single character.")
        except ValueError:
            print("[Caesar Cipher Error] The argument should be a string (or convertible).")

    def encrypt(self, string):
        try:
            self.plaintext = str(string)
            self.ciphertext = ""
        except ValueError:
            print("[Caesar Cipher Error]: Plaintext must be a string (or convertible).")
        for ch in self.plaintext:
            new_ch = ''
            if ch not in self.bypassSet:
                ch = ch.lower()
                try:
                    idx = self.alphabet.index(ch)
                except:
                    new_ch = ch 
                if ch.isupper():
                    new_ch = self.alphabet[(idx + self.key) % self.alphabetSize].upper()
                else: 
                    new_ch = self.alphabet[(idx + self.key) % self.alphabetSize]                  
            else:
                new_ch = ch
            self.ciphertext = self.ciphertext + new_ch
        self.__print()

    def decrypt(self, string):
        try:
            self.ciphertext = str(string)
            self.plaintext = ""
        except ValueError:
            print("[Caesar Cipher Error]: Ciphertext must be a string (or convertible).")
        for ch in self.ciphertext:
            new_ch = ''
            if ch not in self.bypassSet:
                ch = ch.lower()
                try:
                    idx = self.alphabet.index(ch)
                except:
                    new_ch = ch 
                if ch.isupper():
                    new_ch = self.alphabet[(idx - self.key) % self.alphabetSize].upper()
                else: 
                    new_ch = self.alphabet[(idx - self.key) % self.alphabetSize]                  
            else:
                new_ch = ch
            self.plaintext = self.plaintext + new_ch
        self.__print()

    def __print(self):
        print(self.name)
        print("Ciphertext: " + self.ciphertext)
        print("Plaintext: " + self.plaintext)
        pass

    def bruteforceAttack(self, filename=""):
        if filename != "":
            f = open(filename, 'a')
        for k in range(1, self.alphabetSize):
            self.setKey(k)
            self.decrypt(self.ciphertext)
        if filename != "":
            f.write(str(self.plaintext))
            f.write('\n')
        else:
            print(str(self.plaintext))
    


