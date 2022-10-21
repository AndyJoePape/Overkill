from dict import alphabet

def test(keyCheck):
    print([item for item in alphabet.items() if item.__contains__(keyCheck)][0])
        
test('b')