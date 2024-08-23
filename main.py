class Solution:
    def minimumSum(self, num: int) -> int:
        numl=sorted([str(i) for i in str(num)])
        return (sum(list(map(lambda x, y: int(str(x)+str(y)), numl[:len(numl)//2], numl[len(numl)//2:]))))