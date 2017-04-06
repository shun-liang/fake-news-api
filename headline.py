import os
import random
import requests

from textblob import TextBlob

headlines = ['Headline 1', 'Headline 2']
GUARDIAN_KEY = os.environ['GUARDIAN_KEY']

def generate():
    headline = random.choice(get_guardian_news_headlines())
    return headline

def get_guardian_news_headlines():
    guardian_url = 'https://content.guardianapis.com/search?q=quinoa&api-key={0}'.format(GUARDIAN_KEY)
    r = requests.get(guardian_url)
    assert r.status_code == 200
    r = r.json()
    headlines = [result['webTitle'] for result in r['response']['results']]
    blob_headlines = [TextBlob(headline) for headline in headlines]
    return blob_headlines

def process_blob_headlines(blob_headlines):
    nouns = []
    for blob_headline in blob_headlines:
        for word, pos in blob_headline.tags:
            if pos in ('NN', 'NNS'):
                nouns.append(word)

    random.shuffle(nouns)

    fake_headlines = []
    for blob_headline in blob_headlines:
        fake_headline = []
        for word, pos in blob_headline.tags:
            if pos in ('NN', 'NNS'):
                # replace noun in place
                fake_headline.append(nouns.pop())
            else:
                fake_headline.append(word)
        fake_headlines.append(fake_headline)
    return fake_headlines
