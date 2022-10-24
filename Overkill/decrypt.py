from encrypt import convertToShift
  
def isEven(num):
    return not bool(num % 2)
    
def getShiftedNumber(shiftCount, startingIndex, direction):
    index = startingIndex - 1
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if direction == "right":
        while shiftCount != 0:
            if index != 25:
                index += 1
                shiftCount -= 1
            else:
                index = 0
                shiftCount -= 1
    else:
        while shiftCount != 0:
            if index != 0:
                index -= 1
                shiftCount -= 1
            else:
                index = 25
                shiftCount -= 1
    return alphabet[index]


def decryptMessage(plainText, key):
    inputText = convertToShift(plainText)
    keyList = convertToShift(key)
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


def decrypt():
    parsedEncryptedText = parseCipherText(input("Enter ciphertext: "))

    decryptedKey = "".join([str(i) for i in decryptMessage(parsedEncryptedText[1], parsedEncryptedText[0])])
    decryptedText = "".join([str(i) for i in decryptMessage(parsedEncryptedText[0], decryptedKey)])
    print("decrypted message: " + decryptedText, end="\n\n")

        