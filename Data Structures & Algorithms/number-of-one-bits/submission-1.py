class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        n_str = str(bin(n))
        for i in range(len(n_str)):
            if n_str[i] == '1':
                num = num + 1
        return num