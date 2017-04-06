import os
import random
import requests

headlines = ['Headline 1', 'Headline 2']
GUARDIAN_KEY = os.environ['GUARDIAN_KEY']

def generate():
    headline = random.choice(get_guardian_news_headlines())
    return headline

def get_guardian_news_headlines():
    guardian_url = 'https://content.guardianapis.com/search?api-key={0}'.format(GUARDIAN_KEY)
    r = requests.get(guardian_url)
    assert r.status_code == 200
    r = r.json()
    headlines = [result['webTitle'] for result in r['response']['results']]
    return headlines
