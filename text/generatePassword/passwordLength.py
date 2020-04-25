import random

DEFAULT_LENGTH = 12
MIN_MAX_LENGTH = (12, 15)

def getPasswordLength():
    return random.randint(*MIN_MAX_LENGTH)
