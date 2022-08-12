import errors

class CaesarCipher():

    """
    Caesar Cipher.
    By default, it works with the standard lowercase English alphabet, bypassing numbers and whitespaces.
    """

    def __init__(self, key = 0): # sets key and useful variables
        self.__key = key 
        self.__alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.__bypassSet = {' ','0','1','2','3','4','5','6','7','8','9'}
        self.__alphabetSize = 26
        self.__bfAttack = dict.fromkeys(range(1, self.__alphabetSize))

    def setKey(self, key): # sets key
        try:
            self.__key = int(key)
        except TypeError:
            print("[Caesar Cipher Error]: Key must be a positive or negative integer (or convertible).")

    def setAlphabet(self, alphabet): # sets alphabet
        try:
            self.__alphabet = str(alphabet)
            self.__alphabetSize = len(self.__alphabet)
            print("Alphabet set to " + self.__alphabet + ".")
            self.__bfAttack = dict.fromkeys(range(1, self.__alphabetSize))
        except TypeError:
            print("[Caesar Cipher Error]: Alphabet must be a string (or convertible).")

    def insertBypass(self, ch):
        try:
            if (len(ch) == 1):
                self.__bypassSet.add(str(ch))
            else:
                raise errors.InvalidLengthError("[Caesar Cipher Error] The string (or convertible) should consist of a single character.")
        except TypeError:
            print("[Caesar Cipher Error] The argument should be a string (or convertible).")
    
    def removeBypass(self, ch):
        try:
            if (len(ch) == 1):
                self.__bypassSet.remove(str(ch))
            else:
                raise errors.InvalidLengthError("[Caesar Cipher Error] The string (or convertible) should consist of a single character.")
        except TypeError:
            print("[Caesar Cipher Error] The argument should be a string (or convertible).")

    def encrypt(self, string, results=True):
        try:
            self.__plaintext = str(string)
            self.__ciphertext = ""
        except TypeError:
            print("[Caesar Cipher Error]: Plaintext must be a string (or convertible).")
        for ch in self.__plaintext:
            new_ch = ''
            if ch not in self.__bypassSet:
                bln = ch.isupper()
                ch = ch.lower()
                try:
                    idx = self.__alphabet.index(ch)
                except ValueError:
                    new_ch = ch 
                    print("[Caesar Cipher Warning] Bypassed character ", ch, " not in alphabet.")
                if bln:
                    new_ch = self.__alphabet[(idx + self.__key) % self.__alphabetSize].upper()
                else: 
                    new_ch = self.__alphabet[(idx + self.__key) % self.__alphabetSize]                  
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
        except TypeError:
            print("[Caesar Cipher Error]: Ciphertext must be a string (or convertible).")
        for ch in self.__ciphertext:
            new_ch = ''
            if ch not in self.__bypassSet:
                bln = ch.isupper()
                ch = ch.lower()
                try:
                    idx = self.__alphabet.index(ch)
                    if bln:
                        new_ch = self.__alphabet[(idx - self.__key) % self.__alphabetSize].upper()
                    else: 
                        new_ch = self.__alphabet[(idx - self.__key) % self.__alphabetSize]
                except:
                    new_ch = ch 
                    print("[Caesar Cipher Warning] Bypassed character ", ch, " not in alphabet.")                  
            else:
                new_ch = ch
            self.__plaintext = self.__plaintext + new_ch
        if results:
            self.__cipherPrint()
        return self.__plaintext

    def __cipherPrint(self):
        print("+-----------------------+")
        print("| Caesar Cipher Results |")
        print("+-----------------------+")
        print("Ciphertext: " + self.__ciphertext)
        print("Plaintext: " + self.__plaintext)
        return

    def bruteforceAttack(self, string, filename=""):
        try:
            self.__ciphertext = str(string)
            self.__plaintext = ""
        except TypeError:
            print("[Caesar Cipher Error]: Ciphertext must be a string (or convertible).")
        if filename != "":
            f = open(filename, 'w')
        for k in range(1, self.__alphabetSize):
            self.setKey(k)
            dec = self.decrypt(self.__ciphertext, results=False)
            if filename != "":
                f.write("key: "+str(k)+"  "+str(dec))
                f.write('\n')
            else:
                self.__bfAttack[k] = str(dec)
        f.close()
        return self.__bfAttack

#s = "tlla tl hmaly Aol Avnh Whyaf1234"
#CC = CaesarCipher(7)
#CC.decrypt(s)
#l = CC.bruteforceAttack(s, 'test.txt')
#print(l)