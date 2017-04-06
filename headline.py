import os
import requests

headlines = ['Headline 1', 'Headline 2']
GUARDIAN_KEY = os.environ['GUARDIAN_KEY']

def generate():
    # return a fixed head line
    return 'Fixed Head Line'

def get_guardian_news_headlines():
    guardian_url = 'https://content.guardianapis.com/search?api-key={0}'.format(GUARDIAN_KEY)
    print guardian_url
    r = requests.get(guardian_url)
    assert r.status_code == 200
    r = r.json()
    headlines = [result['webTitle'] for result in r['response']['results']]
    return headlines
