from requests_html import HTMLSession


session = HTMLSession()
url='https://time.com/'

r = session.get(url)

r.html.render(sleep=1,scrolldown=4)

top_stories = r.html.find('div',class_='latest-stories' )

print(top_stories)