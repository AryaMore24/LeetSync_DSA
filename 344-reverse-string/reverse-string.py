class Solution(object):
    def reverseString(self, s):
        
        i = 0
        j = len(s)-1

        while i<j:
            
            #swap position
            s[i], s[j] = s[j], s[i]

            #move pointer
            i+=1
            j-=1