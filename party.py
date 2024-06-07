import requests
import pandas as pd

LEGISLATOR_HISTORIAL = "https://theunitedstates.io/congress-legislators/legislators-historical.json"
historical_response = requests.get(LEGISLATOR_HISTORIAL, timeout=20)
social_result = historical_response.json()

# # query the twitter hanlder of the congress ppl from 2008 - 2017
# result = []
# for count, value in enumerate(social_result):

#     start_year = value["terms"][0]["start"]
#     print(start_year)
#     break

PATH = "dataset/twitter_handles.csv"
df = pd.read_csv(PATH)

# Convert the DataFrame to a NumPy array
array = df.to_numpy()
RULER = len("http://t.co/xghfyYg3oC")

results = []

for i in array:
    stripped = i[0].strip()
    if len(stripped) < RULER and stripped[:4] != "http" and stripped != "---":
        results.append(i[0])

print(len(results))
