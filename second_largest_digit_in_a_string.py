class Solution(object):
    def secondHighest(self, s):
        filter_string = sorted(list(set(filter(lambda x: x.isdigit(), s))))
        if len(filter_string) >=2:
            return int(filter_string[-2])
        return -1
