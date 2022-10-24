from dict import alphabet
import random


def getRandomNumber():
    return random.choice(list(alphabet.values()))


def convertToShift(input):
    return [getNumberOrIndexFromDict(char) for char in list(input)]


def getNumberOrIndexFromDict(letterOrIndex):
    return [item for item in alphabet.items() if item.__contains__(letterOrIndex)][0][
        0 if str(letterOrIndex).isnumeric() else 1]


def getShiftedNumber(startLetter, shiftCount, direction):
    finalIndex = getNumberOrIndexFromDict(startLetter)

    if direction == "right":
        finalIndex += shiftCount
    else:
        finalIndex -= shiftCount

    while finalIndex > len(alphabet):
        finalIndex -= len(alphabet)
    return getNumberOrIndexFromDict(finalIndex)


def encryptMessage(plainText, key):
    return [getShiftedNumber(plainText[i], convertToShift(key)[i], "right") for i in
            range(0, len(convertToShift(plainText)))]


def generateRandomKey(plainText):
    return convertToShift([getRandomNumber() for i in range(0, len(plainText))])


def combineTextAndKey(plainText, key):
    return ''.join(''.join(f for f in tup) for tup in zip(plainText, key))


plainText = input("Enter plaintext:\n").replace(" ", "").lower()
key = generateRandomKey(plainText)
encryptedText = "".join([str(i) for i in encryptMessage(plainText, key)])
encryptedKey = "".join([str(i) for i in encryptMessage(key, encryptedText)])
cipherOutput = "".join([str(i) for i in combineTextAndKey(encryptedText, encryptedKey)])
print(cipherOutput)
