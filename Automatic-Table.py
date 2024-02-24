import tweepy
import pandas as pd
import time

api_key = "wETcURH9TaqCgsXsy9TSEchWn"
api_key_secret = "7Tk6vNgE1Hzk9XuUOjLRMULRUlWVxKcwZoH1048iryGgWa6Nzi"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAFVerQEAAAAAvn5lJbSAqRdNSpje2WuffcZ2lpU%3D9yi9KTVBdltLdkYGCYsK9HDEXv4CmG12n6PZY2r3hv60sFlzyy"
access_token = "1113228432257814530-z1aPqlEfzRQZXso7ktWqrupAyz53sv"
access_token_secret = "1qGqyUX34mGC9JDZDBgmbkS0Byn1MlJMUz2D17V3uPkNe"

client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

df = pd.read_excel('Tabela do Campeonato Brasileiro.xlsx')


def postar_tweet():
        tweet_texto = "Tabela Atualizada do campeonato Brasileiro!:\n"
        partes_do_tweet = []
        partes_atual = ""
        for index, row in df.iterrows():
            parte_tweet = f'{row["Posição"]}. {row["Time"]} - Pontos: {row["Pontos"]}\n'

            if len(partes_atual) + len(parte_tweet) <=280:
                partes_atual += parte_tweet
            else:
                partes_do_tweet.append(partes_atual)
                partes_atual = parte_tweet

        partes_do_tweet.append(partes_atual)
        return partes_do_tweet

for parte in postar_tweet():
        client.create_tweet(text=parte)
        print("tweet postado com sucesso")
        time.sleep(5)