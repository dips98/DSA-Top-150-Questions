class Solution:
    def romanToInt(self, strs: List[str]) -> str:
        romanMap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        val=0
        for i in range(len(strs)-1):
            if romanMap[strs[i]]<romanMap[strs[i+1]]:
                val = val - romanMap[strs[i]]
            else:
                val = val + romanMap[strs[i]]
        return val+romanMap[strs[-1]]