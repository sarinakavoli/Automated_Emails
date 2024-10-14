#b7f5e0d63e864ebc883e2f47248310fd

import requests
from pprint import pprint

class NewsFeed:
    """representing multiple news titles and links as a single string"""
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "b7f5e0d63e864ebc883e2f47248310fd"
    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.to_date = to_date
        self.language = language
        self.from_date = from_date


    def get(self):
        url = self._build_url()

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"sortBy=publishedAt&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url

# news_feed = NewsFeed(interest = 'nasa', from_date='2024-09-04', to_date='2024-09-05', language='en')
# print(news_feed.get())

