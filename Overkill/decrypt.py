from enum import Enum
from tokenize import String
from dict import alphabet
  
def isEven(num):
    return not bool(num %2)
  
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
    inputText = convertToShift(plainText, False)
    keyList = convertToShift(key, False)
    output = []
    
    for i in range(0, len(inputText)):
        output.append(getShiftedNumber(keyList[i], inputText[i], "left"))
    return output

def parseCipherText(cipherText):
    text = []
    key = []
    for i in range(0, len(cipherText)):
        if isEven(i):
            text.append(cipherText[i])
        else:
            key.append(cipherText[i])
    return [text, key]

encryptedText = "mrgiaptbbokyicmhszsh"
parsedEncryptedText = parseCipherText(encryptedText)

decryptedKey = "".join([str(i) for i in decryptMessage(parsedEncryptedText[1], parsedEncryptedText[0])])
decryptedText = "".join([str(i) for i in decryptMessage(parsedEncryptedText[0], decryptedKey)])
print(decryptedText)

        