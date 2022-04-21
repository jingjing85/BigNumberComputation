import re


def computation():
    while True:
        # tmpList = ['0'] * 2
        # print(tmpList)
        tmpList = input("Please input two big numbers and split them with one white space:").strip().split()
        # print(tmpList, sys._getframe().f_lineno)
        if len(tmpList) != 2:
            print("The number of the input is not two, please input again. ")
            continue
            # check the input, if they match the format(integer big numbers or big number with one decimal point)
            # if not match
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
                print("%s + %s = %s" % (a, b, c))
                print("%s - %s = %s" % (a, b, d))
                continue
            # at least one of the numbers with a decimal point but both of them are not big numbers
            elif (len(tmpList[0]) < 20 and len(tmpList[1]) < 20) and (
                    re.match("^\d+\.\d+$", tmpList[0]) or re.match("^\d+\.\d+$", tmpList[1])):
                print("The input is not big number.")
                # find the index of decimal point
                log1 = tmpList[0].find('.')
                # print(log1)
                log2 = tmpList[1].find('.')
                # first number is integer number, second one has a decimal point
                if log1 == -1:
                    # print("11111111")
                    # split the numbers into two parts with .
                    # xxxFirst is the first part of numbers that before .
                    # xxxFirst is the second part of numbers that after .
                    subStr2 = tmpList[1].split('.')
                    subStr2First = subStr2[0]
                    subStr2Second = subStr2[1]
                    subStr1First = tmpList[0]
                    subStr1Second = ''

                    # Adding 0 in the behind of  the two numbers to make sure that second parts have the same length
                    N = len(subStr2Second) - len(subStr1Second)
                    # print(N)
                    subStr1Second += "0" * N

                    # calculate the sum
                    firstPart = addition(subStr1First, subStr2First)
                    secondPart = addition(subStr1Second, subStr2Second)
                    sum = firstPart + "." + secondPart
                    print("%s + %s = %s" % (tmpList[0], tmpList[1], sum))

                    # calculate the diff
                    # just calculate skip . as if they are integer numbers, then at last add . in the result
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
                    # print(diffList)
                    finalDiff = "".join(diffList)
                    # print("finalDiff" + finalDiff)
                    # print(finalDiff[0])
                    if finalDiff[0] == '-':
                        middleDiff = finalDiff[1:]
                        # print(middleDiff)
                        middle = middleDiff.split(".")
                        before = middle[0]
                        if len(before) == 0:
                            finalDiff = "-0" + middleDiff
                        # print(finalDiff)
                        print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                    else:
                        middle = finalDiff.split(".")
                        before = middle[0]
                        if len(before) == 0:
                            finalDiff = "0" + finalDiff
                        # print(finalDiff)
                        print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))

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
                    print("%s + %s = %s" % (tmpList[0], tmpList[1], sum))

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
                    finalDiff = "".join(diffList).lstrip("0")
                    # print("diffList1 " + str(diffList))
                    # print("finalDiff1" + str(finalDiff))
                    # if len(before) == 0:
                    #     finalDiff = "0" + finalDiff
                    # # d = "".join(finalDiff[::-1]).lstrip("0")
                    # # print(d)
                    # print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))

                    if finalDiff[0] == '-':
                        middleDiff = finalDiff[1:]
                        # print(middleDiff)
                        middle = middleDiff.split(".")
                        before = middle[0]
                        if len(before) == 0:
                            finalDiff = "-0" + middleDiff
                        # print(finalDiff)
                        print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                    else:
                        # middle = finalDiff.split(".")
                        # before = middle[0]
                        middle = finalDiff.split(".")
                        before = middle[0]
                        if len(before) == 0:
                            finalDiff = "0" + finalDiff
                        # print(finalDiff)
                        print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))

                # both with decimal points
                else:
                    # print("333333333")
                    subStr1 = tmpList[0].split('.')
                    subStr2 = tmpList[1].split('.')
                    subStr1First = subStr1[0]
                    subStr1Second = subStr1[1]
                    subStr2First = subStr2[0]
                    subStr2Second = subStr2[1]
                    big = max(len(subStr1Second), len(subStr2Second))
                    # print("big " + str(big))

                    # make sure that two numbers after decimal point have same length, then we can calculate them easier
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

                    # calculate the sum
                    sum = addition(first, second)
                    sumList = list(sum)
                    sumList.insert(-p, '.')
                    finalSum = "".join(sumList)
                    print("%s + %s = %s" % (tmpList[0], tmpList[1], finalSum))

                    # calculate the diff
                    diff = subtraction(first, second)
                    diffList = list(diff)
                    # print(diffList)
                    # diffList.insert(1, '.')
                    finalDiff = "".join(diffList)
                    # print(finalDiff)

                    # if the result is negative
                    if finalDiff[0] == '-':
                        # print("result is negative")
                        big = max(len(subStr1Second), len(subStr2Second))
                        diffList.insert(-big, '.')
                        finalDiff = "".join(diffList)
                        # print(finalDiff)
                        middleDiff = finalDiff[1:]
                        # print(middleDiff)
                        middle = middleDiff.split(".")
                        # print(middle)
                        before = middle[0]
                        after = middle[1]
                        before = "".join(before).lstrip("0")
                        # print("before " + before)
                        # print("after " + after)
                        # finalDiff = "-" + before + after
                        # print(finalDiff)
                        if len(after) < big:
                            # print("GGGGGG")
                            # print(finalDiff)
                            # print(max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1)
                            if len(before) == 0:
                                # print("case 4")
                                # print(finalDiff)
                                # before = "0."
                                # print(before)
                                # finalDiff = "-" + before + after
                                finalDiff = "-" + "0." + "0" * (
                                        max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1) + after
                                print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                                if after == "0":
                                    # print("case 5")
                                    before = "0."
                                    # print(before)
                                    finalDiff = "-" + before + after
                                    # print(finalDiff)
                                    print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                            else:
                                finalDiff = "-" + "0" * (
                                        max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1) + after
                                # print(finalDiff)
                                finalDiff = "-" + "0." + "0" * (
                                        max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1) + after
                                print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                        elif len(after) >= big:
                            # print("KKKKKKKKKK")
                            diffList = list(finalDiff)
                            # print(diffList)
                            diffMiddle = "".join(diffList)
                            # print(diffMiddle)
                            listMiddle = diffMiddle.split(".")
                            diffList = listMiddle[0] + listMiddle[1]
                            diffList = list(diffList)
                            # print(diffList)
                            if len(before) == 0 and len(after) == big:
                                # print("case 3")
                                diffList.insert(-big, '.')
                                # print(diffList)
                                finalDiff = "".join(diffList)
                                listMiddle = diffMiddle.split("-")
                                after = listMiddle[1]
                                # if before.count("0") ==
                                after = "".join(after).lstrip("0")
                                finalDiff = "-0" + after
                                print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                            else:
                                diffList.insert(-big, '.')
                                finalDiff = "".join(diffList)
                                # print("!3333")
                                # print(finalDiff)
                                listMiddle = finalDiff.split(".")
                                after = listMiddle[1]
                                # diffList = list(diffList)
                                if after.count("0") >= len(after):
                                    # print("case 2")
                                    # print(before)
                                    finalDiff = "-" + before + "." + after
                                    finalDiff = "".join(finalDiff).rstrip("0")
                                    finalDiff = finalDiff + "0"
                                else:
                                    # print("case 1")
                                    finalDiff = "".join(finalDiff).rstrip("0")
                                    middleList = finalDiff.split(".")
                                    before = middleList[0]
                                    after = middleList[1]
                                    if before.count("0") >= (len(before) - 1):
                                        before = "0."
                                        finalDiff = "-" + before + after
                                        # print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))
                                    else:
                                        finalDiff = finalDiff
                                print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                        #
                    # if the result is positive
                    else:
                        # print("SSSSSSssss")
                        diffList.insert(-p, '.')
                        finalDiff = "".join(diffList)
                        # print(finalDiff)
                        # middle = finalDiff.split(".")
                        # before = middle[0]
                        middle = finalDiff.split(".")
                        before = middle[0]
                        after = middle[1]
                        # print("before " + before)
                        # print("after " + str(after))
                        # after = middle[1]
                        # result is begin with 0.
                        if len(before) == 0:
                            # print("1111")
                            if after == "0":
                                # print("case 5")
                                finalDiff = "0." + after
                                # print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))
                            else:
                                finalDiff = "0." + "0" * (
                                        max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1) + after
                                if after.count("0") > 1:
                                    # print("case 4")
                                    finalDiff = "".join(finalDiff).rstrip("0")
                                    finalDiff = finalDiff + "0"
                                else:
                                    # print("case 3")
                                    finalDiff = "".join(finalDiff).rstrip("0")
                            print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                        # print(finalDiff)
                        # result is not begin with 0.
                        else:
                            # print("@@@@@@@@")
                            # print("after " + str(after))
                            if after == "0" and before == "0":
                                finalDiff = "0.0"
                                print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                            else:
                                # if (max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1) == 0:
                                #     finalDiff = before + ".0"
                                #     print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))
                                # else:
                                # print("case 6")
                                finalDiff = before + "." + "0" * (
                                        max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1) + after
                                if after.count("0") == len(after):
                                    finalDiff = "".join(finalDiff).rstrip("0")
                                    finalDiff = finalDiff + "0"
                                else:
                                    finalDiff = "".join(finalDiff).rstrip("0")
                                # return finalDiff
                                print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))

                    # print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))
            # at least one of the numbers is big numbers with a decimal point
            elif (len(tmpList[0]) >= 20 or len(tmpList[1]) >= 20) and (
                    re.match("^\d+\.\d+$", tmpList[0]) or re.match("^\d+\.\d+$", tmpList[1])):
                # print("LLLLL")
                # find the index of decimal point
                log1 = tmpList[0].find('.')
                # print(log1)
                log2 = tmpList[1].find('.')
                # first number is integer number, second one has a decimal point
                if log1 == -1:
                    # print("11111111")
                    # split the numbers into two parts with .
                    # xxxFirst is the first part of numbers that before .
                    # xxxFirst is the second part of numbers that after .
                    subStr2 = tmpList[1].split('.')
                    subStr2First = subStr2[0]
                    subStr2Second = subStr2[1]
                    subStr1First = tmpList[0]
                    subStr1Second = ''

                    # Adding 0 in the behind of  the two numbers to make sure that second parts have the same length
                    N = len(subStr2Second) - len(subStr1Second)
                    # print(N)
                    subStr1Second += "0" * N

                    # calculate the sum
                    firstPart = addition(subStr1First, subStr2First)
                    secondPart = addition(subStr1Second, subStr2Second)
                    sum = firstPart + "." + secondPart
                    print("%s + %s = %s" % (tmpList[0], tmpList[1], sum))

                    # calculate the diff
                    # just calculate skip . as if they are integer numbers, then at last add . in the result
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
                    # print(diffList)
                    finalDiff = "".join(diffList)
                    # print("finalDiff" + finalDiff)
                    # print(finalDiff[0])
                    if finalDiff[0] == '-':
                        middleDiff = finalDiff[1:]
                        # print(middleDiff)
                        middle = middleDiff.split(".")
                        before = middle[0]
                        if len(before) == 0:
                            finalDiff = "-0" + middleDiff
                        # print(finalDiff)
                        print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                    else:
                        middle = finalDiff.split(".")
                        before = middle[0]
                        if len(before) == 0:
                            finalDiff = "0" + finalDiff
                        # print(finalDiff)
                        print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))

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
                    print("%s + %s = %s" % (tmpList[0], tmpList[1], sum))

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
                    finalDiff = "".join(diffList).lstrip("0")
                    # print("diffList1 " + str(diffList))
                    # print("finalDiff1" + str(finalDiff))
                    # if len(before) == 0:
                    #     finalDiff = "0" + finalDiff
                    # # d = "".join(finalDiff[::-1]).lstrip("0")
                    # # print(d)
                    # print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))

                    if finalDiff[0] == '-':
                        middleDiff = finalDiff[1:]
                        # print(middleDiff)
                        middle = middleDiff.split(".")
                        before = middle[0]
                        if len(before) == 0:
                            finalDiff = "-0" + middleDiff
                        # print(finalDiff)
                        print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                    else:
                        # middle = finalDiff.split(".")
                        # before = middle[0]
                        middle = finalDiff.split(".")
                        before = middle[0]
                        if len(before) == 0:
                            finalDiff = "0" + finalDiff
                        # print(finalDiff)
                        print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))

                # both with decimal points
                else:
                    # print("333333333")

                    subStr1 = tmpList[0].split('.')
                    subStr2 = tmpList[1].split('.')
                    subStr1First = subStr1[0]
                    subStr1Second = subStr1[1]
                    subStr2First = subStr2[0]
                    subStr2Second = subStr2[1]
                    big = max(len(subStr1Second), len(subStr2Second))
                    # print("big " + str(big))

                    # make sure that two numbers after decimal point have same length, then we can calculate them easier
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

                    # calculate the sum
                    sum = addition(first, second)
                    sumList = list(sum)
                    sumList.insert(-p, '.')
                    finalSum = "".join(sumList)
                    # print("%s+%s=%s" % (tmpList[0], tmpList[1], finalSum))

                    # calculate the diff
                    diff = subtraction(first, second)
                    diffList = list(diff)
                    # print(diffList)
                    # diffList.insert(1, '.')
                    finalDiff = "".join(diffList)
                    # print(finalDiff)

                    # if the result is negative
                    if finalDiff[0] == '-':
                        # print("result is negative")
                        big = max(len(subStr1Second), len(subStr2Second))
                        diffList.insert(-big, '.')
                        finalDiff = "".join(diffList)
                        # print(finalDiff)
                        middleDiff = finalDiff[1:]
                        # print(middleDiff)
                        middle = middleDiff.split(".")
                        # print(middle)
                        before = middle[0]
                        after = middle[1]
                        before = "".join(before).lstrip("0")
                        # print("before " + before)
                        # print("after " + after)
                        # finalDiff = "-" + before + after
                        # print(finalDiff)
                        if len(after) < big:
                            # print("GGGGGG")
                            # print(finalDiff)
                            print(max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1)
                            if len(before) == 0:
                                # print("case 4")
                                # print(finalDiff)
                                # before = "0."
                                # print(before)
                                # finalDiff = "-" + before + after
                                finalDiff = "-" + "0." + "0" * (
                                        max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1) + after
                                print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                                if after == "0":
                                    # print("case 5")
                                    before = "0."
                                    # print(before)
                                    finalDiff = "-" + before + after
                                    # print(finalDiff)
                                    print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                            else:
                                # print("case 6")
                                # print(finalDiff)
                                finalDiff = "-" + "0" * (
                                        max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1) + after
                                # print(finalDiff)
                                finalDiff = "-" + "0." + "0" * (
                                        max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1) + after
                                print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                        elif len(after) >= big:
                            # print("KKKKKKKKKK")
                            diffList = list(finalDiff)
                            # print(diffList)
                            diffMiddle = "".join(diffList)
                            # print(diffMiddle)
                            listMiddle = diffMiddle.split(".")
                            diffList = listMiddle[0] + listMiddle[1]
                            diffList = list(diffList)
                            # print(diffList)
                            if len(before) == 0 and len(after) == big:
                                # print("case 3")
                                diffList.insert(-big, '.')
                                # print(diffList)
                                finalDiff = "".join(diffList)
                                listMiddle = diffMiddle.split("-")
                                after = listMiddle[1]
                                # if before.count("0") ==
                                after = "".join(after).lstrip("0")
                                finalDiff = "-0" + after
                                print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                            else:
                                diffList.insert(-big, '.')
                                finalDiff = "".join(diffList)
                                # print("!3333")
                                # print(finalDiff)
                                listMiddle = finalDiff.split(".")
                                after = listMiddle[1]
                                # diffList = list(diffList)
                                if after.count("0") >= len(after):
                                    # print("case 2")
                                    # print(before)
                                    finalDiff = "-" + before + "." + after
                                    finalDiff = "".join(finalDiff).rstrip("0")
                                    finalDiff = finalDiff + "0"
                                else:
                                    # print("case 1")
                                    finalDiff = "".join(finalDiff).rstrip("0")
                                    middleList = finalDiff.split(".")
                                    before = middleList[0]
                                    after = middleList[1]
                                    if before.count("0") >= (len(before) - 1):
                                        before = "0."
                                        finalDiff = "-" + before + after
                                        # print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))
                                    else:
                                        finalDiff = finalDiff
                                print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                        #
                    # if the result is positive
                    else:
                        # print("SSSSSSssss")
                        diffList.insert(-p, '.')
                        finalDiff = "".join(diffList)
                        # print(finalDiff)
                        # middle = finalDiff.split(".")
                        # before = middle[0]
                        middle = finalDiff.split(".")
                        before = middle[0]
                        after = middle[1]
                        # print("before " + before)
                        # print("after " + str(after))
                        # after = middle[1]
                        # result is begin with 0.
                        if len(before) == 0:
                            # print("1111")
                            if after == "0":
                                # print("case 5")
                                finalDiff = "0." + after
                                # print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))
                            else:
                                finalDiff = "0." + "0" * (
                                        max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1) + after
                                if after.count("0") > 1:
                                    # print("case 4")
                                    finalDiff = "".join(finalDiff).rstrip("0")
                                    finalDiff = finalDiff + "0"
                                else:
                                    # print("case 3")
                                    finalDiff = "".join(finalDiff).rstrip("0")
                            print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                        # print(finalDiff)
                        # result is not begin with 0.
                        else:
                            # print("@@@@@@@@")
                            # print("after " + str(after))
                            if after == "0" and before == "0":
                                finalDiff = "0.0"
                                print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))
                            else:
                                # if (max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1) == 0:
                                #     finalDiff = before + ".0"
                                #     print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))
                                # else:
                                # print("case 6")
                                finalDiff = before + "." + "0" * (
                                        max(len(subStr1Second), len(subStr2Second)) - 1 - len(after) + 1) + after
                                if after.count("0") == len(after):
                                    finalDiff = "".join(finalDiff).rstrip("0")
                                    finalDiff = finalDiff + "0"
                                else:
                                    finalDiff = "".join(finalDiff).rstrip("0")
                                # return finalDiff
                                print("%s - %s = %s" % (tmpList[0], tmpList[1], finalDiff))

                    # print("%s-%s=%s" % (tmpList[0], tmpList[1], finalDiff))
            # two numbers both integer big numbers
            else:
                a = tmpList[0]
                b = tmpList[1]
                c = addition(a, b)
                d = subtraction(a, b)
                print("%s + %s = %s" % (a, b, c))
                print("%s - %s = %s" % (a, b, d))
                continue


# addition function is used to get the sum of two big numbers
def addition(a, b):
    # reversal the numbers
    num1 = a[::-1]
    # print(num1)
    num2 = b[::-1]
    # print(num2)
    # carry is 0, means the sum of two digits is less than 10, so we don't need to add additional 1 in higher position
    # otherwise, carry is 1, the higher position need to be added additional 1
    carry = 0
    result = ''
    minLen = min(len(num1), len(num2))
    # calculate the part with same length
    for i in range(minLen):
        # print("AAAAA")
        temp = int(num1[i]) + int(num2[i]) + carry
        carry = temp // 10
        result = result + str(temp % 10)
    # print("result：" + result)
    # print("carry: " + str(carry))
    # calculate the part with extra length
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


# subtraction function is used to get the sum of two big numbers
def subtraction(a, b):
    num1 = a[::-1]
    # print("num1 " + str(num1))
    num2 = b[::-1]
    # print("num2 " + str(num2))
    borrow = 0
    result = ''
    minLen = min(len(num1), len(num2))
    # num1 is longer than num2, that is to say a > b
    if len(num1) > len(num2):
        # print("DDDDD")
        for i in range(minLen):
            if num1[i] >= num2[i]:
                # print("OOOOOO")
                # print(num1[i])
                # print(num2[i])
                temp = int(num1[i]) - int(num2[i]) - borrow
                # print("borrow " + str(borrow))
                if temp < 0:
                    # if
                    temp = int(num1[i]) + 10 - int(num2[i]) - borrow
                    borrow = 1
                else:
                    # temp = 0
                    borrow = 0
                # print("temp " + str(temp))
                result = result + str(temp)
                # print("result1 " + str(result))
            else:
                temp = int(num1[i]) + 10 - borrow - int(num2[i])
                # print("UUUUU")
                # num1[i+1] = num1[i+1] - 1
                borrow = 1
                result = result + str(temp)
                # print("result2 " + result)

        if len(num1) > len(num2):
            # print("yyyyy")
            for i in range(len(num2), len(num1)):
                # print(num1[i])
                # print(num2[i])
                temp = int(num1[i]) - borrow
                borrow = 0
                result = result + str(temp)
                # print("result " + result)
        # result = result.rsplit("0")
        result = "".join(result).rstrip("0")
        # print("@@@@@@ " + str(result))
        finalResult = result[::-1]
        # print("finalResult " + finalResult)
    # num2 is longer than num1
    elif len(num1) < len(num2):
        # print("EEEEE")
        for i in range(minLen):
            if num2[i] >= num1[i]:
                # print("IIIII")
                # print("num2[i]" + num2[i])
                # print("num1[i]" + num1[i])
                temp = int(num2[i]) - int(num1[i]) - borrow
                if temp < 0:
                    temp = int(num1[i]) + 10 - int(num2[i]) - borrow
                    borrow = 1
                else:
                    # temp = 0
                    borrow = 0
                # borrow = 0
                # print("temp " + str(temp))
                result = result + str(temp)
            else:
                # print("PPPPP")
                temp = int(num2[i]) + 10 - borrow - int(num1[i])
                # num1[i+1] = num1[i+1] - 1
                borrow = 1
                result = result + str(temp)
                # print("result" + result)
        # calculate the part with extra length
        if len(num2) > len(num1):
            for i in range(len(num1), len(num2)):
                temp = int(num2[i]) - borrow
                borrow = 0
                result = result + str(temp)
        result = "".join(result).rstrip("0")
        # print("result: " + result)
        finalResult = '-' + result[::-1]
    # num1 has same length with num2
    else:
        # print("FFFF")
        # print(num1[-1])
        # a is greater than b, the result is positive, so do not need to deal with the result
        if a >= b:
            for i in range(minLen):
                if num1[i] >= num2[i]:
                    # print("IIIII")
                    # print("num2 " + num2[i])
                    # print("num1 " + num1[i])
                    temp = int(num1[i]) - int(num2[i]) - borrow

                    if temp < 0:
                        temp = int(num1[i]) + 10 - int(num2[i]) - borrow
                        borrow = 1
                    else:
                        # temp = 0
                        borrow = 0
                    result = result + str(temp)
                    # print("result " + result)
                else:
                    # print("PPPPP")
                    # print("num2 " + num2[i])
                    # print("num1 " + num1[i])
                    temp = int(num1[i]) + 10 - borrow - int(num2[i])
                    # num1[i+1] = num1[i+1] - 1
                    borrow = 1
                    result = result + str(temp)
                    # print("result " + result)
            # print("result: " + result)
            result = "".join(result).rstrip("0")
            if result == "":
                result = "0"
            # print("result: " + str(result))
            finalResult = result[::-1]
            # print("finalResult " + finalResult)

        # if a is smaller than b, then add - in front of the result
        else:
            # result1 = ''
            for i in range(minLen):
                if num2[i] >= num1[i]:
                    # print("fu")
                    # print("result " + result)
                    # print("num2 " + num2[i])
                    # print("num1 " + num1[i])
                    # print("borrow " + str(borrow))
                    temp = int(num2[i]) - int(num1[i]) - borrow
                    if temp < 0:
                        temp = int(num1[i]) + 10 - int(num2[i]) - borrow
                        borrow = 1
                    else:
                        # temp = 0
                        borrow = 0
                    # print("temp" + str(temp))
                    # result = ''.join(temp)
                    result = result + str(temp)
                    # print("result " + result)
                else:
                    # print("QQQQQ")
                    # print("num1 " + num1[i])
                    # print("num2 " + num2[i])
                    # print("borrow " + str(borrow))
                    temp = int(num2[i]) + 10 - borrow - int(num1[i])
                    # num1[i+1] = num1[i+1] - 1
                    borrow = 1
                    result = result + str(temp)
                    # print("result " + result)
                    # print("result" + resul）
                # result = "".join(result).rstrip("0")
                # print(result)
                finalResult = "-" + result[::-1]
            # print("finalResult " + str(finalResult))
    return finalResult


if __name__ == '__main__':
    computation()
