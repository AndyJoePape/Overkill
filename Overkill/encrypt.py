from dict import alphabet
import random


# Returns a random alphanumeric value from our created alphabet
def getRandomNumber():
    return random.choice(list(alphabet.values()))


# Converts a list of input alphanumeric letters into shift numbers
def convertToShift(input):
    return [getNumberOrIndexFromDict(char) for char in list(input)]


# Returns the number associated with an alphanumeric value when given an alphanumeric value
# Returns the alphanumeric value when given a number
def getNumberOrIndexFromDict(letterOrIndex):
    return [item for item in alphabet.items() if item.__contains__(letterOrIndex)][0][
        0 if str(letterOrIndex).isnumeric() else 1]


# Performs the shift on a letter or number, increments by shiftCount, Encrypts determines left or right
def getShiftedNumber(startLetter, shiftCount, encrypts):
    if encrypts:
        finalIndex = getNumberOrIndexFromDict(startLetter)
        finalIndex += shiftCount

        while finalIndex > len(alphabet):
            finalIndex -= len(alphabet)
    else:
        finalIndex = startLetter
        finalIndex -= shiftCount

        while finalIndex <= 0:
            finalIndex += len(alphabet)

    return getNumberOrIndexFromDict(finalIndex)


# Encrypys a plainText and a key, shifts the plain text by the converted to numbers key
def encryptMessage(plainText, key):
    return [getShiftedNumber(plainText[i], convertToShift(key)[i], True) for i in
            range(0, len(convertToShift(plainText)))]


# Generates a random number based on the length of the plainText
def generateRandomKey(plainText):
    return convertToShift([getRandomNumber() for i in range(0, len(plainText))])


# combines the plainText and key by doing every other
def combineTextAndKey(plainText, key):
    return ''.join(''.join(f for f in tup) for tup in zip(plainText, key))


def countBlocks(plainText):
    return int(len(plainText) / 32) + 1


def getBlock(value, blockNum):
    return value[blockNum * 31:(blockNum + 1) * 31]


def buildBlocks(plainText):
    numBloc = countBlocks(plainText)
    paddedPlaintext = plainText.ljust(numBloc * 31, 'a')

    return [(getBlock(paddedPlaintext, i), generateRandomKey(getBlock(paddedPlaintext, i))) for i in range(0, numBloc)]


def getLengthOfFinalBlock(plainText):
    return 31 - (len(plainText) % 31)

def encryptPlainText(plainText: str):
    blocks = buildBlocks(plainText.replace(" ", "æ"))
    cipherText = ""

    for i in range(0, len(blocks)):
        encryptedText = "".join(str(i) for i in encryptMessage(blocks[i][0], blocks[i][1]))
        encryptedKey = "".join([str(i) for i in encryptMessage(blocks[i][1], encryptedText)])
        cipher = "".join([str(i) for i in combineTextAndKey(encryptedText, encryptedKey)])
        cipherText += cipher
        if i == len(blocks) - 1:
            cipherText += getNumberOrIndexFromDict(getLengthOfFinalBlock(plainText))

    return "".join(cipherText)



# main encrypt function for terminal
def encrypt():
    print("Encrypted Message: " + "".join(encryptPlainText(input("Enter plaintext: "))), end="\n\n")
