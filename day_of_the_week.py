class Solution(object):
    
    def dayOfTheWeek(self, day, month, year):
        return date(year, month, day).strftime("%A")