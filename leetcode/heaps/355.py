from collections import defaultdict
import heapq

List = list 

class Twitter:
    # Initialize the Twitter class with data structures to store tweets and follower relationships
    def __init__(self):
        # Counter for maintaining the order of tweets
        self.count = 0
        # Map to store tweets for each user: userId -> list of [count, tweetIds]
        self.tweetMap = defaultdict(list)
        # Map to store followers for each user: userId -> set of followeeId
        self.followMap = defaultdict(set)

    # Method for a user to post a tweet
    def postTweet(self, userId: int, tweetId: int) -> None:
        # Store the tweet's information in the tweetMap along with count for ordering
        self.tweetMap[userId].append([self.count, tweetId])
        # Decrease the count to ensure newer tweets have lower counts
        self.count -= 1

    # Method to retrieve a user's news feed
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []  # List to store the resulting tweet IDs
        minHeap = []  # Min-heap to store tweets based on their counts (for recent tweets)

        # Add the user itself to its own followers (news feed includes own tweets)
        self.followMap[userId].add(userId)
        # Loop through all followees of the user
        for followeeId in self.followMap[userId]:
            # Check if the followee has posted tweets
            if followeeId in self.tweetMap:
                # Get the index of the latest tweet for this followee
                index = len(self.tweetMap[followeeId]) - 1
                # Get the count and tweet ID of the latest tweet from this followee
                count, tweetId = self.tweetMap[followeeId][index]
                # Push the tweet's information into the min-heap with count as key
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Process the min-heap until it's empty or 10 tweets have been collected
        while minHeap and len(res) < 10:
            # Get the tweet with the smallest count from the heap
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            # Add the tweet ID to the result list
            res.append(tweetId)
            # If there are more tweets from the same followee, add them back to the heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Return the list of recent tweet IDs
        return res

    # Method for a user to follow another user
    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followee to the follower's set of followees
        self.followMap[followerId].add(followeeId)

    # Method for a user to unfollow another user
    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Check if the follower is actually following the followee before unfollowing
        if followeeId in self.followMap[followerId]:
            # Remove the followee from the follower's set of followees
            self.followMap[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)