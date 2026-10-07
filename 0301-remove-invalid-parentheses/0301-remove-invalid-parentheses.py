from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):

        def isValid(string):

            bal = 0

            for ch in string:

                if ch == '(':
                    bal += 1

                elif ch == ')':

                    bal -= 1

                    if bal < 0:
                        return False

            return bal == 0

        q = deque([s])
        visited = {s}

        ans = []
        found = False

        while q:

            curr = q.popleft()

            if isValid(curr):
                ans.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):

                if curr[i] not in "()":
                    continue

                nxt = curr[:i] + curr[i+1:]

                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return ans