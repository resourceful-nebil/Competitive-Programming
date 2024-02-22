class RecentCounter:
    def __init__(self):
        self.pings = deque()

    def ping(self, t):
        # Add the current timestamp to the queue
        self.pings.append(t)

        # Remove the outdated pings from the queue
        while self.pings and self.pings[0] < t - 3000:
            self.pings.popleft()

        # Return the size of the queue, which represents the number of recent pings
        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)