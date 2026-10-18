class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = defaultdict(int)

        for ele in strs:
            if tuple(sorted(ele)) in dic:
                dic[tuple(sorted(ele))].append(ele)
            else:
                dic[tuple(sorted(ele))] = [ele]

        return list(dic.values()) 

        
         
             

            
        