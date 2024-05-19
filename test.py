import tweepy
import keys


status = 'Hello again'


Client = tweepy.Client(
    consumer_key = keys.consumer_key,
    consumer_secret = keys.consumer_secret,
    bearer_token = keys.bearer_token,
    access_token = keys.access_token,
    access_token_secret = keys.access_token_secret
)
if __name__ == "__main__":
    Client.create_tweet(text=status)
    print('Successfully Tweeted!')
    

