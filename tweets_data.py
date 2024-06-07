import requests
import os
from dotenv import load_dotenv
import tweepy

load_dotenv()

SOCIAL_MEDIA_URL = "https://theunitedstates.io/congress-legislators/legislators-social-media.json"
CURRENT_LEGISLATOR_URL = "https://theunitedstates.io/congress-legislators/legislators-current.json"

sm_response = requests.get(SOCIAL_MEDIA_URL)
social_result = sm_response.json()

cl_response = requests.get(CURRENT_LEGISLATOR_URL)
cl_result = cl_response.json()

print(f"{len(social_result)} is the number of congress people whose social media handles we know.")
print(f"{len(cl_result)} is the total number of people whose information we have.")

new_data = []

for i in social_result:

    bioguide = i["id"]["bioguide"]

    for j in cl_result:
        if bioguide == j["id"]["bioguide"]:
            if "twitter" in i["social"]:

                current_term = j["terms"][-1]
                party = current_term["party"]

                BIAS_LEVEL = 1  # libearl

                if party == "Republican":
                    BIAS_LEVEL = 0  # conservative

                result = {
                    "first_name": j["name"]["first"],
                    "last_name": j["name"]["last"],
                    "twitter_handle": i["social"]["twitter"],
                    "bias": BIAS_LEVEL,
                }

                new_data.append(result)

# instantiate tweepy authenticator instance
api_key = os.getenv("API_KEY")
api_key_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# instantiate tweepy client instance
# client = tweepy.Client(api_key, api_key_secret, access_token, access_token_secret)

# username = "FabrizioRomano"

# tweets = api.user_timeline()
# print(tweets)
