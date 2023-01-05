def reverseWords(s):
    s = s.strip()
    s = s.split()
    return " ".join(s[::-1])