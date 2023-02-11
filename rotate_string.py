class Solution(object):
    def rotateString(self, s, goal):
        if s==goal:
            return True
        string_list = list(s)
        goal_list = list(goal)
        for i in range(len(s)):
            poped_item = string_list.pop(0)
            string_list.append(poped_item)
            if string_list == goal_list:
                return True
        return False