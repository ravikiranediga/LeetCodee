class Solution:
    def countServers(self, n, logs, x, queries):

        # Step 1: Sort logs by time
        logs.sort(key=lambda log: log[1])

        # Step 2: Sort queries with original indices
        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        # Step 3: Initialize variables
        freq = {}
        answer = [0] * len(queries)

        left = 0
        right = 0

        # Step 4: Process queries in sorted order
        for q, idx in sorted_queries:

            start = q - x

            # Add logs entering the window
            while right < len(logs) and logs[right][1] <= q:

                server = logs[right][0]

                freq[server] = freq.get(server, 0) + 1

                right += 1

            # Remove logs leaving the window
            while left < right and logs[left][1] < start:

                server = logs[left][0]

                freq[server] -= 1

                if freq[server] == 0:
                    del freq[server]

                left += 1

            # Calculate servers with zero requests
            answer[idx] = n - len(freq)

        return answer