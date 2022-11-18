from encrypt import convertToShift, getShiftedNumber, getNumberOrIndexFromDict


# determines if a number is even or odd
def isEven(num):
    return not bool(num % 2)


# decrypts a plaintext from a key
def decryptMessage(plainText, key):
    inputText = convertToShift(plainText)
    keyList = convertToShift(key)

    return [getShiftedNumber(keyList[i], inputText[i], False) for i in range(0, len(inputText))]


# parses the cipherText into a cipher and key
def parseCipherText(cipherText):
    length = getNumberOrIndexFromDict(cipherText[-1])
    cipher = cipherText[0:-1]
    text = []
    key = []

    [text.append(cipher[i]) if isEven(i) else key.append(cipher[i]) for i in range(0, len(cipher))]
    return [text, key, length]

def decryptPlainText(cipherText: str):
    print(cipherText)
    parsedCipherText = parseCipherText(cipherText)
    decryptedKey = "".join(
        [str(i) for i in decryptMessage(''.join(parsedCipherText[0]), ''.join(parsedCipherText[1]))])
    decryptedText = "".join([str(i) for i in decryptMessage(decryptedKey, ''.join(parsedCipherText[0]))])
    return decryptedText.replace("|", " ")[0:-parsedCipherText[2]]


# main decrypt function for terminal
def decrypt():
    print("decrypted message: " + decryptPlainText(input("Enter ciphertext: ")), end="\n\n")
