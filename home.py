import tweepy, time

# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview
consumer_key = "D03T2ecjTxDSTbBiteLy1T66N"
consumer_secret = "pOZf8FOnb8m22q3hMaTqM3ql2FEd8fD6uyZT90BmnJoqE15cHp"
access_key = "915585146245525504-TmCSh9nD12LuwVpn1R0U2aVGRUycbEe"
access_secret = "FpH7gYP5U5iPuPeboueNNqnOlXDDROrKiGoJwLqBDi5Pq"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"

    return user_profile

userName = "CitronResearch"
user = api.get_user(userName)
allTweets = api.user_timeline(userName, count=200)


#iterate, finding max tweets
maxCount=0
for x in allTweets:
    if x.retweet_count>maxCount:
        maxCount = x.retweet_count
        maxTweet = x.text
        print(x.text)
        print(x.retweet_count)

print(maxTweet)
