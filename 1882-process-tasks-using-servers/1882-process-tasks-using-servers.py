import heapq

class Solution:
    def assignTasks(self, servers, tasks):

        n = len(servers)
        m = len(tasks)

        available = [(servers[i], i) for i in range(n)]
        heapq.heapify(available)

        busy = []

        ans = []

        time = 0

        for i in range(m):

            time = max(time, i)

            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)

            ans.append(index)

            finish_time = time + tasks[i]

            heapq.heappush(busy, (finish_time, weight, index))

        return ans