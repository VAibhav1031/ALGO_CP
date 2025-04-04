from collections import Counter

def findvaluePair(s:str):
    freq = Counter(s) 
    # there was one thing we forget at that moment  that was the  the  pair  you gonna  show up will have different  
    for i,c  in enumerate(s):
        if i == 0: continue
        if s[i] != s[i-1] and freq[s[i]] == int(s[i]) and freq[s[i-1]] == int(s[i-1]):
            return s[i-1:i+1]

    return ""
print(findvaluePair("15122"))
