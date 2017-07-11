def is_palindrome(str1):
    check = ''
    idx = len(str1) - 1

    while idx > -1:
        check = check + str1[idx]
        idx -= 1 

    return str1 == check
