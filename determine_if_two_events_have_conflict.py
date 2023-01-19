class Solution(object):
    def haveConflict(self, event1, event2):
        START, END = 0, 1
        
        #  event1 starts before event2                  # event2 starts before event1
        if event1[START]<=event2[START]<=event1[END] or event2[START]<=event1[START]<=event2[END]:
            return True
        return False
        

        
        