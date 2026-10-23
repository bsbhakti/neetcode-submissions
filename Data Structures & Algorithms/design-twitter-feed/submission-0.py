class Twitter(object):

    def __init__(self):
        self.feed = {}
        self.followers = {}
        self.time = 1
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId in self.feed:
            self.feed[userId].append((tweetId,self.time))

        else:
            self.feed[userId] = [(tweetId, self.time)]

        if userId not in self.followers:
            self.followers[userId] = set()
        self.followers[userId].add(userId)


        #print("posting", self.feed)
        self.time +=1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        ret = []
        i = 0
        heap = []
        if userId in self.followers:
            for following in self.followers[userId]:
                if following in self.feed:
                    last = self.feed[following][-1]
                    heapq.heappush(heap, (-last[1], last[0], -1, following))
        #print(heap)


        while len(ret) < 10 and len(heap):
            popped = heapq.heappop(heap)
            #print("popped", popped)
            ret.append(popped[1])
            ind = popped[2]
            following = popped[3]
            if ind > -len(self.feed[following]):
                new = self.feed[following][ind-1]
                heapq.heappush(heap, (-new[1], new[0], ind-1, following))
                #print("pushed",(new[1], new[0], ind-1, following) )
        return ret
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.followers:
            self.followers[followerId].add(followeeId)
        else:
            self.followers[followerId] = set()
            self.followers[followerId].add(followeeId)
        ##print("followers",self.followers)
        
    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        ##print("unfollow", self.followers)
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)