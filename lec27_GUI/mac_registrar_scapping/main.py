"""
Inspirational Tutorial: https://www.youtube.com/watch?v=1PCWwK0AsE0&t=12s

Required Packages:
- httpx: alternatives: requests
- selectolax: HTML parser, alternatives: Beautiful Soup
"""

import httpx
from selectolax.parser import HTMLParser

url = 'https://macadmsys.macalester.edu/macssb/customPage/page/classSchedule'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

resp = httpx.get(url, headers=headers, follow_redirects=True)
html = HTMLParser(resp.text)

classes = html.css("div#TableCRN30183")
print(classes)

