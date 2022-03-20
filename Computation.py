import re


def computation():
    while True:
        # tmpList = ['0'] * 2
        # print(tmpList)
        tmpList = input("Please input two big numbers and split them with white space:").strip().split()
        # print(tmpList, sys._getframe().f_lineno)
        if len(tmpList) != 2:
            print("The number of the input is not two, please input again. ")
            continue
            # if not tmpList[0]
        elif (not re.match("^[0-9]+$", tmpList[0]) and not re.match("^\d+\.\d+$", tmpList[0])) or (not re.match(
                "^[0-9]+$", tmpList[1]) and not re.match("^\d+\.\d+$", tmpList[1])):
            # if not tmpList[0].isdigit() or not tmpList[1].isdigit():
            # print("QQQQ")
            print("The input is invalid, please input again.")
            continue
        else:
            # two numbers both integer numbers but not big numbers
            if (len(tmpList[0]) < 20 or len(tmpList[1]) < 20) and (
                    re.match("^[0-9]+$", tmpList[0]) and re.match("^[0-9]+$", tmpList[1])):
                print("The input is not big number.")
                a = tmpList[0]
                b = tmpList[1]
                c = addition(a, b)
                d = subtraction(a, b)
                print("%s+%s=%s" % (a, b, c))
                print("%s-%s=%s" % (a, b, d))
                continue
            elif (len(tmpList[0]) < 20 or len(tmpList[1]) < 20) and (
                    re.match("^\d+\.\d+$", tmpList[0]) or re.match("^\d+\.\d+$", tmpList[1])):
                log1 = tmpList[0].find('.')
                log2 = tmpList[1].find('.')
                # first one is integer number, second one has a decimal point
                if log1 == -1:
                    # print("11111111")
                    subStr2 = tmpList[1].split('.')
                    subStr2First = subStr2[0]
                    subStr2Second = subStr2[1]
                    subStr1First = tmpList[0]
                    subStr1Second = ''
                    N = len(subStr2Second) - len(subStr1Second)
                    # print(N)
                    subStr1Second += "0" * N
                    firstPart = addition(subStr1First, subStr2First)
                    secondPart = addition(subStr1Second, subStr2Second)
                    sum = firstPart + "." + secondPart
                    print("%s+%s=%s" % (tmpList[0], tmpList[1], sum))

                    first = subStr1First + subStr1Second
                    second = subStr2First + subStr2Second
                    # print("first " + first)
                    # print("second " + second)
                    diff = subtraction(first, second)
                    # print("diff" + diff)
                    p = len(subStr1Second)
                    # print("p " + str(p))
                    diffList = list(diff)
                    diffList.insert(-p, '.')
                    finalDiff = "".join(diffList)
                    # print(finalDiff)
                    print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))
                # first one a decimal point, second one is integer number
                elif log2 == -1:
                    # print("22222222")
                    # print(tmpList[0])
                    # log = tmpList[0].find('.')
                    # print("log" + str(log))
                    subStr1 = tmpList[0].split('.')
                    subStr1First = subStr1[0]
                    subStr1Second = subStr1[1]
                    subStr2First = tmpList[1]
                    subStr2Second = ''

                    N = len(subStr1Second) - len(subStr2Second)
                    subStr2Second += "0" * N
                    firstPart = addition(subStr1First, subStr2First)
                    secondPart = addition(subStr1Second, subStr2Second)
                    sum = firstPart + "." + secondPart
                    print("%s+%s=%s" % (tmpList[0], tmpList[1], sum))

                    first = subStr1First + subStr1Second
                    second = subStr2First + subStr2Second
                    # print("first " + first)
                    # print("second " + second)
                    diff = subtraction(first, second)
                    # print("diff" + diff)
                    p = len(subStr1Second)
                    # print("p " + str(p))
                    diffList = list(diff)
                    diffList.insert(-p, '.')
                    finalDiff = "".join(diffList)
                    # print(finalDiff)
                    print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))
                # both with decimal points
                else:
                    # print("333333333")
                    subStr1 = tmpList[0].split('.')
                    subStr2 = tmpList[1].split('.')
                    subStr1First = subStr1[0]
                    subStr1Second = subStr1[1]
                    subStr2First = subStr2[0]
                    subStr2Second = subStr2[1]
                    if len(subStr1Second) > len(subStr2Second):
                        N = len(subStr1Second) - len(subStr2Second)
                        subStr2Second += "0" * N
                    else:
                        N = len(subStr2Second) - len(subStr1Second)
                        subStr1Second += "0" * N
                    first = subStr1First + subStr1Second
                    second = subStr2First + subStr2Second
                    # print("first " + first)
                    # print("second " + second)
                    p = len(subStr1Second)
                    # print("p " + str(p))

                    sum = addition(first, second)
                    sumList = list(sum)
                    sumList.insert(-p, '.')
                    finalSum = "".join(sumList)
                    print("%s+%s=%s" % (tmpList[0], tmpList[1], finalSum))

                    diff = subtraction(first, second)
                    diffList = list(diff)
                    diffList.insert(-p, '.')
                    finalDiff = "".join(diffList)
                    # print(finalDiff)
                    print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))
            else:
                # print("XXXXXX")
                a = tmpList[0]
                b = tmpList[1]
                c = addition(a, b)
                d = subtraction(a, b)
                print("%s+%s=%s" % (a, b, c))
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
    # print("num1 " + str(num1))
    num2 = b[::-1]
    # print("num2 " + str(num2))
    borrow = 0
    result = ''
    minLen = min(len(num1), len(num2))
    # num1 is longer than num2
    if len(num1) > len(num2):
        # print("DDDDD")
        for i in range(minLen):
            if num1[i] >= num2[i]:
                temp = int(num1[i]) - int(num2[i]) - borrow
                borrow = 0
                result = result + str(temp)
            else:
                temp = int(num1[i]) + 10 - borrow - int(num2[i])
                # num1[i+1] = num1[i+1] - 1
                borrow = 1
                result = result + str(temp)

        if len(num1) > len(num2):
            for i in range(len(num2), len(num1)):
                temp = int(num1[i]) - borrow
                borrow = 0
                result = result + str(temp)
        finalResult = result[::-1]
    # num2 is longer than num1
    elif len(num1) < len(num2):
        # print("EEEEE")
        for i in range(minLen):
            if num2[i] >= num1[i]:
                # print("IIIII")
                # print("num2[i]" + num2[i])
                # print("num1[i]" + num1[i])
                temp = int(num2[i]) - int(num1[i]) - borrow
                borrow = 0
                # print("temp " + str(temp))
                result = result + str(temp)
            else:
                # print("PPPPP")
                temp = int(num2[i]) + 10 - borrow - int(num1[i])
                # num1[i+1] = num1[i+1] - 1
                borrow = 1
                result = result + str(temp)
                # print("result" + result)
        # 长度多出来的那部分
        if len(num2) > len(num1):
            for i in range(len(num1), len(num2)):
                temp = int(num2[i]) - borrow
                borrow = 0
                result = result + str(temp)
        # print("result: " + result)
        finalResult = '-' + result[::-1]
    # num1 has same length with num2
    else:
        # print("FFFF")
        # print(num1[-1])
        # a is greater than b
        if a >= b:
            for i in range(minLen):
                if num1[i] >= num2[i]:
                    # print("IIIII")
                    # print("num2[i]" + num2[i])
                    # print("num1[i]" + num1[i])
                    temp = int(num1[i]) - int(num2[i]) - borrow
                    borrow = 0
                    result = result + str(temp)
                else:
                    # print("PPPPP")
                    temp = int(num1[i]) + 10 - borrow - int(num2[i])
                    # num1[i+1] = num1[i+1] - 1
                    borrow = 1
                    result = result + str(temp)
                    # print("result" + result)
            # print("result: " + result)
            finalResult = result[::-1]
        # a is smaller than b
        else:
            for i in range(minLen):
                if num2[i] >= num1[i]:
                    temp = int(num2[i]) - int(num1[i]) - borrow
                    borrow = 0
                    result = result + str(temp)
                else:
                    # print("PPPPP")
                    temp = int(num2[i]) + 10 - borrow - int(num1[i])
                    # num1[i+1] = num1[i+1] - 1
                    borrow = 1
                    result = result + str(temp)
                    # print("result" + result)
            finalResult = "-" + result[::-1]
    return finalResult


if __name__ == '__main__':
    computation()
