import math

minSqrt = 1020304050607080900
maxSqrt = 1929394959697989990

minNumber = int(math.sqrt(minSqrt))
maxNumber = int(math.sqrt(maxSqrt))

def checkNumber(num):
    num = str(num)
    if num[0] == "1" and num[2] == "2" and num[4] == "3" and num[6] == "4" and num[8] == "5" and num[10] == "6" and num[12] == "7" and num[14] == "8" and num[16] == "9":
        return True
    return False

def main():
    print(minNumber, maxNumber)

    for i in range(minNumber, maxNumber, 10):
        if checkNumber(i**2):
            print(i)
            break
    print("Done")

main()