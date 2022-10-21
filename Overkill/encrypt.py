from enum import Enum
from dict import alphabet
from operator import index
import string
import random
from tokenize import String
    
def getRandomNumber():
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

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
        for letter in alphabet:
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

def encryptMessage(plainText, key):
    inputText = convertToShift(plainText)
    keyList = convertToShift(key)
    output = []
    
    for i in range(0, len(inputText)):
        output.append(getShiftedNumber(keyList[i], inputText[i], "right"))
    return output

def generateRandomKey(plainText):
    keyLength = len(plainText)
    shiftList = []
    for i in range(0, keyLength):
        shiftList.append(getRandomNumber())
    key = convertShiftToText(shiftList)
    
    return key

def combineTextAndKey(plainText, key):
    output = []
    text = list(plainText)
    keyList = list(key)
    for i in range(0, len(text)):
        output.append(text[i])
        output.append(keyList[i])
    return output


plainText = input("Enter plaintext:\n")
plainText = plainText.replace(" ", "").lower()
key = generateRandomKey(plainText) 
encryptedText = "".join([str(i) for i in encryptMessage(plainText, key)])
encryptedKey = "".join([str(i) for i in encryptMessage(key, encryptedText)])
cipherOutput  = "".join([str(i) for i in combineTextAndKey(encryptedText, encryptedKey)])
print(cipherOutput)
