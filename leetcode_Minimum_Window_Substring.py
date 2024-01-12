class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # basic returns
        if t == s: 
            return t
        if len(s) < len(t) or t == '':
            return ''
    
        # init the vars
        hash_have, hash_need = {}, {char : t.count(char) for char in set(t)}
        l, have, need = 0, 0, len(hash_need)
        res, res_len = tuple(), float('infinity')

        # main loop
        for r in range(len(s)):
            char = s[r]
            if char in t:
                hash_have[char] = hash_have.get(char, 0) + 1
                if hash_have[char] == hash_need[char]:
                    have += 1
                
                # secondary loop
                while have == need:
                    # write the result
                    if r - l + 1 < res_len:
                        res, res_len = (l, r), r - l + 1
                    # delete the left char
                    left_char = s[l]
                    if left_char in hash_need:
                        hash_have[left_char] -= 1
                        if hash_have[left_char] < hash_need[left_char]:
                            have -= 1
                    l += 1
        l, r = res
        return s[l:r + 1] if res_len != float('infinity') else ''
        

a = Solution()
print(a.minWindow(s = "bbaa", t = "aba"))