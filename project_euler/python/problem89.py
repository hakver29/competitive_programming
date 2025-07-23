def readInputFile():
    filename = 'p089_roman.txt'
    with open(filename, 'r') as file:
        data_list = file.read().splitlines()

    return data_list


def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


def romanToDecimal(str):
    res = 0
    i = 0

    while (i < len(str)):

        # Getting value of symbol s[i]
        s1 = value(str[i])

        if (i + 1 < len(str)):

            # Getting value of symbol s[i + 1]
            s2 = value(str[i + 1])

            # Comparing both values
            if (s1 >= s2):

                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:

                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res

def reduceRoman(roman):
    roman = roman.replace("DCCCC", "CM")
    roman = roman.replace("LXXXX", "XC")
    roman = roman.replace("VIIII", "IX")

    roman = roman.replace("CCCC", "CD")
    roman = roman.replace("XXXX", "XL")
    roman = roman.replace("IIII", "VI")

    return roman

def main():
    data_list = readInputFile()
    S = 0
    for i in data_list:

        s0 = i
        s1 = reduceRoman(i)

        while len(s0) != len(s1):
            s0 = s1
            s1 = reduceRoman(s1)

        S += len(i) - len(s1)
    return S

print(main())