class Solution(object):
    def capitalizeTitle(self, title):
          return ' '.join([word.title() if len(word)>2 else word for word in title.lower().split()])
