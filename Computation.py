import sys


def computation():
    while True:
        # tmpList = ['0'] * 2
        # print(tmpList)
        tmpList = input("Please input two big numbers and split them with white space:").strip().split()
        # print(tmpList, sys._getframe().f_lineno)
        if len(tmpList) != 2:
            print("The number of the input is not two, please input again. ")
            continue
        else:
            if not tmpList[0].isdigit() or not tmpList[1].isdigit():
                print("The input is valid, just allow to input positive integer numbers, please input again.")
                continue
            else:
                if len(tmpList[0]) < 20 or len(tmpList[1]) < 20:
                    print("The input is not big number.")
                    a = tmpList[0]
                    b = tmpList[1]
                    c = addition(a, b)
                    d = subtraction(a, b)
                    # print("%s+%s=%s" % (a, b, c))
                    print("%s-%s=%s" % (a, b, d))
                    # print(len(tmpList[0]))
                    # print(tmpList[0].isdigit())
                    continue
                else:
                    a = tmpList[0]
                    b = tmpList[1]
                    c = addition(a, b)
                    d = subtraction(a, b)
                    # print("%s+%s=%s" % (a, b, c))
                    print("%s-%s=%s" % (a, b, d))
                    # print(len(tmpList[0]))
                    # print(tmpList[0].isdigit())
                    continue


def addition(a, b):
    num1 = a[::-1]
    # print(num1)
    num2 = b[::-1]
    # print(num2)
    carry = 0
    result = ''
    minLen = min(len(num1), len(num2))
    # the part of comment length
    for i in range(minLen):
        # print("AAAAA")
        temp = int(num1[i]) + int(num2[i]) + carry
        carry = temp // 10
        result = result + str(temp % 10)
    # print("result：" + result)
    # print("carry: " + str(carry))

    if len(num1) < len(num2):
        for i in range(len(num1), len(num2)):
            # print("BBBBBB")
            temp = int(num2[i]) + carry
            carry = temp // 10
            result = result + str(temp % 10)
    else:
        for i in range(len(num2), len(num1)):
            # print("CCCCC")
            temp = int(num1[i]) + carry
            carry = temp // 10
            result = result + str(temp % 10)
    # print("carry1: " + str(carry))
    if carry > 0:
        result = result + str(carry)
    # print("result：" + result)
    finalResult = result[::-1]
    # print("final result：" + finalResult)
    return finalResult


def subtraction(a, b):
    num1 = a[::-1]
    print("num1 " + str(num1))
    num2 = b[::-1]
    print("num2 " + str(num2))
    borrow = 0
    result = ''
    minLen = min(len(num1), len(num2))

    for i in range(minLen):
        if num1[i] >= num2[i]:
            temp = int(num1[i]) - int(num2[i])
            result = result + str(temp)
        else:
            temp = int(num1[i]) + 10 - borrow - int(num2[i])
            # num1[i+1] = num1[i+1] - 1
            borrow = 1
            result = result + str(temp)

    if len(num1) > len(num2):
        for i in range(len(num2), len(num1)):
            temp = int(num1[i]) - borrow
            result = result + str(temp)
    else:
        for i in range(len(num1), len(num2)):
            temp = int(num2[i]) - borrow
            result = result + str(temp)
    # print("result: " + result)
    finalResult = result[::-1]
    return finalResult


if __name__ == '__main__':
    computation()
