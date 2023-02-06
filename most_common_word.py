class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        import collections
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        frequency = collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
        return frequency