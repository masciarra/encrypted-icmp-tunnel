
"""Takes input as following:

examples: python substitution_encryption.py encrypt input.txt output.txt"""

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

import sys

foPath = ""
output = ""


foPath = sys.argv[3]
fi = open(sys.argv[2], "r")
fileContents = fi.read()

if sys.argv[1] == "encrypt":
    output = output + substitutionEncrypt(fileContents)
else:
    output = output + substitutionDecrypt(fileContents)

#output to file

fo = open(foPath, "w+")
fo.write(output)
fo.close

