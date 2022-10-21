from ast import Mod
from enum import Enum
from operator import index
import string
import random
from tokenize import String
class Letters(Enum):
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    k = 11
    l = 12
    m = 13
    n = 14
    o = 15
    p = 16
    q = 17
    r = 18
    s = 19
    t = 20
    u = 21
    v = 22
    w = 23
    x = 24
    y = 25
    z = 26
  
def isEven(num):
    return not bool(num %2)
  
def convertToShift(text):
    inputText = list(text)
    output = []
    for char in inputText:
        for letter in Letters:
            if char == letter.name:
                output.append(letter.value)
                break

    return output

def convertShiftToText(shiftList):
    output = []
    for num in shiftList:
        for letter in Letters:
            if num == letter.value:
                output.append(letter.name)
                break

    return output
    
def getShiftedNumber(shiftCount, startingIndex, direction):
    index = startingIndex - 1
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if direction == "right":
        while shiftCount!=0:
            if(index!=25):
                index = index+1
                shiftCount = shiftCount-1
            else:
                index=0
                shiftCount = shiftCount-1
    else:
        while shiftCount!=0:
            if(index!=0):
                index = index-1
                shiftCount = shiftCount-1
            else:
                index=25
                shiftCount = shiftCount-1
    return alphabet[index]


def decryptMessage(plainText, key):
    inputText = convertToShift(plainText)
    keyList = convertToShift(key)
    output = []
    
    for i in range(0, len(inputText)):
        output.append(getShiftedNumber(keyList[i], inputText[i], "left"))
    return output

def decryptCipherText(cipherText):
    text = []
    key = []
    for i in range(0, len(cipherText)):
        if isEven(i):
            text.append(cipherText[i])
        else:
            key.append(cipherText[i])
    return [text, key]

encryptedText = "yhooamdr"
parsedEncryptedText = decryptCipherText(encryptedText)

decryptedKey = "".join([str(i) for i in decryptMessage(parsedEncryptedText[1], parsedEncryptedText[0])])
decryptedText = "".join([str(i) for i in decryptMessage(parsedEncryptedText[0], decryptedKey)])
print(decryptedText)

        