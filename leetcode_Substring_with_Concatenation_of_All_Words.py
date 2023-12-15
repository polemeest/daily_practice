from typing import List
from itertools import permutations
class Solution:
    def split_string(self, input: str, str_size: int) -> list:
        return [input[i:i + str_size] for i in range(0, len(input), str_size)]
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if not words:
            return res
        len_s, one_len = len(words) * len(words[0]), len(words[0])
        if len(s) < len_s:
            return res
        
        for index in range(len(s) - len_s + 1): 
            mut = self.split_string(s[index:index + len_s], one_len)
            if sorted(mut) == sorted(words):
                res.append(index)
        return res
        
        
a = Solution()
for i in (("wordgoodgoodgoodbestword", ["word","good","best","good"]),
          ('barfoothefoobarman', ["foo","bar"]), 
          ("wordgoodgoodgoodbestword", ["word","good","best","word"]), 
          ("barfoofoobarthefoobarman", ["bar","foo","the"])
          ):
    print(a.findSubstring(*i))
    
    
    
    
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or words==[]: return

        lenstr = len(s)
        lenword = len(words[0])
        lensubstr = lenword * len(words)

        times = {}
        # frequency 
        for word in words:
            if word in times:
                times[word] += 1 
            else:
                times[word] = 1
        ans = []
        for i in range(min(lenword, lenstr - lensubstr+1)):
            self.findAnswer(i, lenstr, lenword, lensubstr, s, times, ans)
        return ans
         


    def findAnswer(self,strstart,lenstr,lenword,lensubstr,s,times,ans):
        wordstart=strstart
        curr={}
        while strstart+lensubstr<=lenstr:
            word=s[wordstart:wordstart+lenword]
            wordstart+=lenword
            if word not in times:
                strstart=wordstart
                curr.clear()
            else:
                if word in curr:
                    curr[word]+=1
                else:
                    curr[word]=1
                while curr[word]>times[word]:
                    curr[s[strstart:strstart+lenword]]-=1
                    strstart+=lenword
                if wordstart-strstart==lensubstr:
                    ans.append(strstart)
'''