# -*- coding: utf-8 -*-
def isCorrect(city):
    """
    Checking input for correct type
    """
    if city is None:
        return False
    else:
        firstChar = ord(city[0])
        if 1040 <= firstChar <= 1103 or firstChar == 1025:
            return True
        else:
            return False


def isItThanks(thnx):
    if 'спасибо' in thnx or 'благодарю' in thnx or 'от души' in thnx:
        return True
    else:
        return False
