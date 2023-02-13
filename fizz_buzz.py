class Solution(object):
    def fizzBuzz(self, n):
        lst = list(range(1, n+1))
        lst_length = len(lst)
        new_lst = []
        for i in range(1,lst_length+1):
            if i%3==0 and i%5==0:
                new_lst.append("FizzBuzz") 
            elif i%3 == 0:
                new_lst.append("Fizz")
            elif i%5 == 0:
                new_lst.append("Buzz")
            else:
                new_lst.append(str(i))
        print(new_lst)
        return new_lst