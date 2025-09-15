class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=0
        w=text.split(" ")
        w1=set(brokenLetters)
        for i in range(len(w)):
            
            
                if not any(ch in w1 for ch in w[i]):
                
                  c+=1
        return c

        