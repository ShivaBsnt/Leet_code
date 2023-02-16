class Solution(object):
    def sortPeople(self, names, heights):
        zipped = zip(names, heights)
        sort_zip = sorted(zipped, key=lambda x:x[1], reverse=True)
        name, height = zip(*sort_zip)
        return list(name)