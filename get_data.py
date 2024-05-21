import requests

SOCIAL_MEDIA_URL = "https://theunitedstates.io/congress-legislators/legislators-social-media.json"
CURRENT_LEGISLATOR_URL = "https://theunitedstates.io/congress-legislators/legislators-current.json"

sm_response = requests.get(SOCIAL_MEDIA_URL)
social_result = sm_response.json()

cl_response = requests.get(CURRENT_LEGISLATOR_URL)
cl_result = cl_response.json()

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

print("----------")
print(new_data)
