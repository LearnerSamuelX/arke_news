import os
from datetime import datetime, timedelta
from newsapi import NewsApiClient
from dotenv import load_dotenv

load_dotenv()

news_api_key = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key=news_api_key)

# Get the current date
current_date = datetime.now()

# Calculate the date 20 days before today
date_20_days_ago = current_date - timedelta(days=20)

formatted_current_date = current_date.strftime("%Y-%m-%d")
formatted_20_days_ago = date_20_days_ago.strftime("%Y-%m-%d")

keywords_bank = [
    "inflation",
    "border",
    "immigration",
    "environment",
    "tax",
    "fauci",
    "debt",
    "abortion",
    "vote",
]

popular_topics = ""
for count, value in enumerate(keywords_bank):
    if count < len(keywords_bank) - 1:
        popular_topics = popular_topics + keywords_bank[count] + " OR "
    else:
        popular_topics = popular_topics + keywords_bank[count]

# retrieve data volume
all_articles = newsapi.get_everything(
    q=popular_topics,
    sources="bbc-news, cnn, associated-press, bloomberg, business-insider",
    domains="www.bbc.co.uk/news, us.cnn.com, apnews.com, www.bloomberg.com, www.businessinsider.com",
    from_param=formatted_20_days_ago,
    to=formatted_current_date,
    language="en",
    sort_by="relevancy",
    page=1,
)

total_result = all_articles["totalResults"]

pages = total_result // 100 + (1 if total_result % 100 != 0 else 0)

retrieved_result = []

for i in range(pages):

    page_num = i + 1

    all_articles = newsapi.get_everything(
        q=popular_topics,
        sources="bbc-news, cnn, associated-press, bloomberg, business-insider",
        domains="www.bbc.co.uk/news, us.cnn.com, apnews.com, www.bloomberg.com, www.businessinsider.com",
        from_param=formatted_20_days_ago,
        to=formatted_current_date,
        language="en",
        sort_by="relevancy",
        page=page_num,
    )

    for article in all_articles["articles"]:
        title = article["title"]
        description = article["description"]
        article_info = {
            "title": title,
            "description": description,
        }
        retrieved_result.append(article_info)


print(retrieved_result)
print("---------- END OF RUN ----------")
