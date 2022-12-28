def addDigits(self, num):
    while len(str(num)) != 1:
        rem_sum = 0
        while num:
            rem = num%10
            rem_sum = rem_sum + rem
            num = num//10
        num = rem_sum
    return num 