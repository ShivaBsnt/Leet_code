class Solution(object):
    def countDigits(self, num):
        if len(str(num)) == 1:
            return 1
        
        else:
            count = 0
            digits = [int(x) for x in str(num)]
            for i in digits:
                if num%i == 0:
                    count+=1
            return count
                         
