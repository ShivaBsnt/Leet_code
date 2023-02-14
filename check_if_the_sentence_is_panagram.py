class Solution(object):
    def checkIfPangram(self, sentence):
        alphabets = {'a', 'b','c', 'd', 'e', 'f', 'g',
        'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        sentence_list = set(list(sentence))
        if alphabets - sentence_list:
            return False
        return True
