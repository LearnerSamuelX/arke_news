import requests

SOCIAL_MEDIA_URL = "https://theunitedstates.io/congress-legislators/legislators-social-media.json"

response = requests.get(SOCIAL_MEDIA_URL)

social_result = response.json()

print("----------------")

for i in social_result:

    bioguide = i["id"]["bioguide"]
