from multiprocessing.connection import wait
from fastapi import FastAPI

from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}



@app.get("/getTimeStories")
def getStories():
    url_of_website='https://time.com/'

    html_test = requests.get(url_of_website).text

    soup = BeautifulSoup(html_test,'lxml')
    to_send = []
    dict = {}


    latest_stories = soup.find_all('li' ,class_='latest-stories__item' )
    for latest_story in latest_stories:
        headline = latest_story.find('h3',class_='latest-stories__item-headline').text
        link = latest_story.find('a').text
        title_key='title'
        title_link = 'link'
        dict[title_key] = headline
        dict[title_link] = link
        to_send.append(dict)

    return to_send





