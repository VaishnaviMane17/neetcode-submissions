class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        for ele in t:
            if ele not in s:
                return False

        s1 = defaultdict(int)
        s2 = defaultdict(int)

        for ele in s:
            s1[ele]+=1
        for ele in t:
            s2[ele]+=1

        for key in s1:
            if s1[key] != s2 [key]:
                return False

        return True
            


        