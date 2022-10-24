from pydoc import plain
from dict import alphabet
from operator import index
import random
from tokenize import String
    
def getRandomNumber():
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

def convertToShift(input, isNumber):
    output = []
    input = list(input)
    for char in input:
        shiftCount = [item for item in alphabet.items() if item.__contains__(char)][0]
        if isNumber==False:
            output.append(shiftCount[1])
        else:
            output.append(shiftCount[0])
    return output 
    
def getShiftedNumber(startLetter, shiftCount, direction):
    if direction == "right":
        return ''.join(chr((ord(char) - 97 + shiftCount) % 26 + 97) for char in startLetter)
    else:
        return ''.join(chr((ord(char) - 97 - shiftCount) % 26 + 97) for char in startLetter)


def encryptMessage(plainText, key):
    inputText = convertToShift(plainText, False)
    keyList = convertToShift(key, False)
    output = []
    for i in range(0, len(inputText)):
        output.append(getShiftedNumber(plainText[i], keyList[i], "right"))
    return output

def generateRandomKey(plainText):
    keyLength = len(plainText)
    shiftList = []
    for i in range(0, keyLength):
        shiftList.append(getRandomNumber())
    print(shiftList)
    test = convertToShift(shiftList, True)
    return test

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
