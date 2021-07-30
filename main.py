class Solution:
    def nextLargerElement(self, arr, n):
        s = []
        ans = []
        for i in reversed(arr):
            if len(s) == 0:
                ans.append(-1)
            elif len(s) > 0 and i < s[-1]:

                ans.append(s[-1])
            elif len(s) > 0 and s[-1] <= i:
                while len(s) > 0 and s[-1] <= i:
                    s.pop()
                if len(s) == 0:
                    ans.append(-1)
                else:
                    ans.append(s[-1])

            s.append(i)
        return (ans[::-1])
