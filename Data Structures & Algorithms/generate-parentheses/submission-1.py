class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(op,cl,perm):
            if cl > op or op > n:
                return
            if (op == cl and op == n):
                res.append("".join(perm))
                return
            perm.append(')')
            backtrack(op,cl+1,perm)
            perm.pop()
            perm.append('(')
            backtrack(op+1,cl,perm)
            perm.pop()

        backtrack(0,0,[])
        return res
