def reverse(x):
    num = abs(x)
    ans = int(str(num)[::-1])
    if x<0:
        ans = ans * -1
    mi = 2 ** 31 * (-1)
    mx = 2 ** 31 -1
    
    if ans > mx or ans < mi:
        return 0
    return ans
