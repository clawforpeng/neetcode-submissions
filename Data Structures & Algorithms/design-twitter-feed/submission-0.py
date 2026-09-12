class Twitter:

    def __init__(self):
        self.followers = {}
        self.newsFeed = {}
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.newsFeed:
            self.newsFeed[userId] = []

        index = len(self.newsFeed[userId])

        self.newsFeed[userId].append(
            (-self.time, tweetId, userId, index)
        )

        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        sols = []

        # Include user's own tweets
        followees = self.followers.get(userId, set()) | {userId}

        for followee in followees:
            if followee in self.newsFeed and self.newsFeed[followee]:
                heapq.heappush(
                    minHeap,
                    self.newsFeed[followee][-1]
                )

        while minHeap and len(sols) < 10:
            record = heapq.heappop(minHeap)

            _time, tweetId, author, index = record

            sols.append(tweetId)

            if index > 0:
                heapq.heappush(
                    minHeap,
                    self.newsFeed[author][index - 1]
                )

        return sols

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()

        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)