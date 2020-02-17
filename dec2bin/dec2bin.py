def dec2bin(n: int):
    output = ''

    while n > 0:
        output = str(n % 2) + output
        n = n // 2

    return output


# print(dec2bin(88))


def bin2dec(s: str):
    output = 0
    i = len(s) - 1
    while i >= 0:
        output = output * 2
        output = output + int(s[i])
        i = i - 1

    return output


# print(bin2dec('10101010'))

def dec2hex(n: int):
    char = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
    output = ''

    while n > 0:
        output = str(char[n % 16]) + output
        n = n // 16

    return output


print(dec2hex(255))
