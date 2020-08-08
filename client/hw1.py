"""Library of functions to encrypt and decrypt lowercase, alphabetic strings

Takes input as following:

examples: python hw1.py caesar encrypt 3 helloworld.txt output.txt
          python hw1.py substitution encrypt input.txt output.txt
          python hw1.py polyalphabetic encrypt test input.txt output.txt
          python hw1.py transposition encrypt input.txt output.txt"""
def caesarEncrypt(int, str):
    """Encrypts string by advancing each character by a specificed key"""

    str = str.lower()
    new = ""
    for c in str:
        num = (ord(c) + int)
        if num > 122:
            num -= 122
            num += 96
        new += chr(num)

    return new

def caesarDecrypt(key = -1, message = ""):
    """Decrypts string by retreating each character by a specificed key"""
    print("GETTING HERE")
    print(message)
    message = message.lower()
    new = ""
    for c in message:
        num = ord(c) - key

        if num < 97:
            num = 123 - (97 - num)
        new += chr(num)
    return new

def substitutionEncrypt(str):
    """Encrypts string by substituting each character with the ordinal inverse:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ZYXWVUTSRQPONMLKJIHGFEDCBA
    """
    
    str = str.lower()
    new = ""
    for c in str:
        num = 123 - (ord(c) - 96)
        new += chr(num)

    return new

def substitutionDecrypt(message = ""):
    """Decrypts string by substituting each character with the ordinal inverse:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ZYXWVUTSRQPONMLKJIHGFEDCBA
    """

    message = message.lower()
    new = ""

    for c in message:
        num = 123 - ord(c) + 96
        new += chr(num)

    return new

def polyalphabeticEncrypt(key = "", message = ""):
    """Encrypts string by overlaying a key, then advancing characters by overlayed ordinal value.
    Referenced https://www.youtube.com/watch?v=BgFJD7oCmDE"""
    
    key = key.lower()
    message = message.lower()
    new = ""
    mindex = 0
    keyLength = len(key)
    for c in message:
        keyIndex = ((mindex + 1) % keyLength)
        keyIndex -= 1
        newCNum = ord(c) + ord(key[keyIndex]) - 96
        if newCNum > 122:
            newCNum -= 122
            newCNum += 96
        newC = chr(newCNum)
        new += newC
        mindex += 1

    return new

def polyalphabeticDecrypt(key = "", message = ""):
    """Decrypts string in the same manner a string is encrypted polyalphabetically"""
    key = key.lower()
    message = message.lower()
    new = ""
    mindex = 0
    keyLength = len(key)
    for c in message:
        keyIndex = ((mindex + 1) % keyLength)
        keyIndex -= 1
        newCNum = ord(c) - (ord(key[keyIndex]) - 96)
        if newCNum < 97:
            newCNum = 123 - (97 - newCNum)

        new += chr(newCNum)
        mindex += 1

    return new
    
def transposition(message = ""):
    """Both encrypts and decrypts a string by reversing the string - a form of transposition.
    Referenced http://crypto.interactive-maths.com/simple-transposition-ciphers.html"""
    message = message.lower()
    new = ""
    for c in reversed(message):
        new = new + c

    return new


import sys

foPath = ""
output = ""
if sys.argv[1] == "caesar":

    foPath = sys.argv[5]
    fi = open(sys.argv[4], "r")
    fileContents = fi.read()
    if sys.argv[2] == "encrypt":
        output = output + caesarEncrypt(int(sys.argv[3]), fileContents)
    else:
        output = output + caesarDecrypt(int(sys.argv[3]), fileContents)

elif sys.argv[1] == "substitution":

    foPath = sys.argv[4]
    fi = open(sys.argv[3], "r")
    fileContents = fi.read()

    if sys.argv[2] == "encrypt":
        output = output + substitutionEncrypt(fileContents)
    else:
        output = output + substitutionDecrypt(fileContents)

elif sys.argv[1] == "polyalphabetic":

    foPath = sys.argv[5]
    fi = open(sys.argv[4], "r")
    fileContents = fi.read()

    if sys.argv[2] == "encrypt":
        output = output + polyalphabeticEncrypt(sys.argv[3], fileContents)
    else:
        output = output + polyalphabeticDecrypt(sys.argv[3], fileContents)

elif sys.argv[1] == "transposition":

    foPath = sys.argv[4]
    fi = open(sys.argv[3], "r")
    fileContents = fi.read()
    
    output = output + transposition(fileContents)

#output to file

fo = open(foPath, "w+")
fo.write(output)
fo.close

