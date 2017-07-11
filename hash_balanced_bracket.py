def balanced(_str):
    closers = {'}': '{', ')': '(', ']': '[', '>':'<'}
    openers = set(closers.values())

    openers_seen = []

    for char in _str:
        if openers_seen == []:
            return False
        elif char in closers:
            if char == openers_seen[-1]:
                openers_seen.pop()
            else:
                return False

    return openers_seen == []