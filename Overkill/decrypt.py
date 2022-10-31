from encrypt import convertToShift, getShiftedNumber


def isEven(num):
    return not bool(num % 2)


def decryptMessage(plainText, key):
    inputText = convertToShift(plainText)
    keyList = convertToShift(key)
    output = []

    for i in range(0, len(inputText)):
        output.append(getShiftedNumber(keyList[i], inputText[i], False))
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

    decryptedKey = "".join([str(i) for i in decryptMessage(''.join(parsedEncryptedText[0]), ''.join(parsedEncryptedText[1]))])
    decryptedText = "".join([str(i) for i in decryptMessage(decryptedKey, ''.join(parsedEncryptedText[0]))])
    
    print("decrypted message: " + decryptedText.replace("€", " "), end="\n\n") 