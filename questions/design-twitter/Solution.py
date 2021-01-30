"""

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:


postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.


Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);


"""


import heapq

class User(object):
    def __init__(self, user_id):
        self.user_id = user_id
        self.tweets = []
        self.followees = set()
    
    def postTweet(self, tweet_id, ts):
        self.tweets.append((-ts, tweet_id))
        if len(self.tweets) > 10:
            self.tweets.pop(0)
    
    def follow(self, uid):
        self.followees.add(uid)
    
    def unfollow(self, uid):
        if uid in self.followees:
            self.followees.remove(uid)


class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ts = 0
        self.users = {}
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.add_users([userId])
        self.users[userId].postTweet(tweetId, self.ts)
        self.ts += 1
    
    def add_users(self, user_ids):
        for uid in user_ids:
            if uid not in self.users:
                self.users[uid] = User(uid)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.users:
            return []
        user = self.users[userId]
        track = dict()
        for fid in user.followees:
            track[fid] = [-2, self.users[fid].tweets]
        track[userId] = [-2, user.tweets]
        pq = [(el[1][-1], fid) for fid, el in track.iteritems() if el[1]]
        heapq.heapify(pq)
        news = []
        num = 10
        while num > 0 and len(pq) > 0:
            num -= 1
            tweet, fid = heapq.heappop(pq)
            news.append(tweet[1])
            idx, tweets = track[fid]
            if idx >= -len(tweets):
                track[fid][0] = idx - 1
                heapq.heappush(pq, (tweets[idx], fid))
        return news

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.add_users([followerId, followeeId])
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.add_users([followerId, followeeId])
        self.users[followerId].unfollow(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)