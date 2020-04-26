from text.cipherMessage.algorithm import (
    keycodeAddition,
)

def getAllAlgorithms():
    return [
        keycodeAddition.KeycodeAddition(),
    ]

def getChosenAlgorithm():
    return keycodeAddition.KeycodeAddition()
