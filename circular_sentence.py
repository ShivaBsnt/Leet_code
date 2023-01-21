class Solution(object):
    def isCircularSentence(self, sentence):
        word_list = sentence.split(" ")
        word_list_length = len(word_list)
        if len(word_list) == 1:
            if word_list[0][0] == word_list[0][-1]:
                return True
        for i in range(word_list_length-1):
            if word_list[i][-1] != word_list[i+1][0]:
                return False
        if word_list[0][0] != word_list[word_list_length-1][-1]:
            return False
        return True

        