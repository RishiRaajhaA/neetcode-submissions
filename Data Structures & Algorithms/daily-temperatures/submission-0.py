class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, index = stack.pop()
                days = i - index
                result[index] = days
            stack.append((temperatures[i], i))
        return result