def getShiftedNumber(startLetter, shiftCount, direction):
    if direction == "right":
        return ''.join(chr((ord(char) - 97 + shiftCount) % 26 + 97) for char in startLetter)
    else:
        return ''.join(chr((ord(char) - 97 - shiftCount) % 26 + 97) for char in startLetter)