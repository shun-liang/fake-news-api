import requests
import headline
import random
from bs4 import BeautifulSoup

headlines = headline.get_guardian_news_headlines()

def replace_headlines():
  web_page = "http://www.dailymail.co.uk/home/index.html"
  response = requests.get(web_page)
  soup = BeautifulSoup(response.content, "html.parser")

  text = soup.select("h2,.pufftext")

  for item in text:
   # child = list(item.children)
   # child[1].string = "New text"
    item.string = random.choice(headlines)
  return(soup.prettify())


from sanic import Sanic
from sanic import response

app = Sanic()

@app.route("/")
async def test(request):
  return response.html(replace_headlines())

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)
