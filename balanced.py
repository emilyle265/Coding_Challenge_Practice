def balance(_str):
    closers = {'}':'{', ')':'(', ']':'[', '>':'<'}
    openers = set(closers.values())

    openers_seen = []

    for char in _str:
        if char in openers:
            openers_seen.append(char)
        elif char in closers:
            if openers_seen == []:
                return False
            elif closers.get(char) == openers_seen[-1]:
                openers_seen.pop()
            else:
                return False

    return openers_seen == []
