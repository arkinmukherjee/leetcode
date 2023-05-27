class Solution:

    def fibDynamic(self, n: int, dic):
        if n in dic:
            return dic[n]
        else:
            dic[n] = self.fibDynamic(n-1, dic) + self.fibDynamic(n-2, dic)

        return dic[n]

    def fib(self, n: int) -> int:
        dic = {}
        dic[0] = 0
        dic[1] = 1
        return self.fibDynamic(n, dic)
