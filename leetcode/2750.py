def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 1e9 + 7
        ones = []
        for i, val in enumerate(nums):
            if val == 1:
                ones.append(i)
        
        if len(ones) == 0:
            return 0
        
        answer = 1
        for i in range(1, len(ones)):
            answer *= ones[i]-ones[i-1]
            answer %= MOD

        return int(answer)
