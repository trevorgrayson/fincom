from StringIO import StringIO
from io import BytesIO
from lxml import etree
import requests


WORLD_NEWS = 'http://www.wsj.com/xml/rss/3_7085.xml'
TECH = 'http://www.wsj.com/xml/rss/3_7455.xml'
MAIN_NEWS = 'https://feeds.a.dj.com/rss/RSSMarketsMain.xml'


response = requests.get(MAIN_NEWS)

if response.status_code == 200:
    root = etree.parse(BytesIO(response.content))

    for item in root.xpath('//item'):
        title = item.xpath('title')[0]
        desc = item.xpath('description')[0]
        # description, link
        print title.text  # + ' = ' + desc.text
