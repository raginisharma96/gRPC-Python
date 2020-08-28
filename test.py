from src.primeNumber import validatePrime

def test_validatePrime():
    number1 = 13
    output1 = True

    number2 = 20
    output2 = False

    assert(validatePrime(number1) == output1)
    assert(validatePrime(number2) == output2)

    