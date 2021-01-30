import tweepy
import hashlib
import os

class TwitterScrap:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def set_env(self, date_since):
        files_cwd = os.listdir()

        if 'datasets' not in files_cwd:
            os.mkdir('./datasets')

        filename = "./datasets/datasset_" + date_since + ".csv"

        dataset = open(filename, 'w')
        dataset.write("Time,Tweet_Text,Likes,Re_tweet")
        dataset.close()

        return filename


    def generateAPI(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)

        return api

    def scrapTweet(self, keywords, date_since, rqd_data_count, filename):
        data_hash_lst = []

        api = self.generateAPI()
        tweets = tweepy.Cursor(api.search, q=keywords, lang="en", since=date_since, tweet_mode='extended').items(rqd_data_count)

        for data in tweets:
            try:
                dataset = open(filename, 'a')

                json_datas = data._json

                tweet_time = str(json_datas["created_at"])
                tweet_text = str(' '.join(json_datas["full_text"].split(',')))
                likes = str(json_datas["retweeted_status"]["favorite_count"])
                retweet = str(json_datas["retweet_count"])

                data = tweet_time + ',' + tweet_text + ',' + likes + ',' + retweet

                hash = hashlib.md5(data.encode()).hexdigest()

                if hash not in data_hash_lst:
                    data_hash_lst.append(hash)
                    dataset.write('\n' + data)

                    print("Time :", tweet_time, "Tweet text :", tweet_text, "Likes :", likes, "Retweet :", retweet)

                dataset.close()


            except KeyError:
                pass
            except UnicodeEncodeError:
                pass


if __name__ == '__main__':
    consumer_key = input("Enter Consumer Secret API Key :")
    consumer_secret = input("Enter Consumer Secret API Key :")
    access_token = input("Enter Access Token :")
    access_token_secret = input("Enter Access Secret Token :")

    keywords = "#covid19"
    date_since = input("Enter date since when you want the scrap data [yyyy-mm-dd]:")
    rqd_data_count = int(input("Enter no. of datas you want : "))


    twitter_scrap = TwitterScrap(consumer_key, consumer_secret, access_token, access_token_secret)
    filename = twitter_scrap.set_env(date_since)
    twitter_scrap.scrapTweet(keywords, date_since, rqd_data_count, filename)