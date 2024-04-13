"""
Inspirational Tutorial: https://www.youtube.com/watch?v=1PCWwK0AsE0&t=12s

Required Packages:
- httpx: alternatives: requests
- selectolax: HTML parser, alternatives: Beautiful Soup
"""

import httpx
from selectolax.parser import HTMLParser

# url = 'https://macadmsys.macalester.edu/macssb/customPage/page/classSchedule'
url = 'https://macadmsys.macalester.edu/macssb/internalPb/virtualDomains.classScheduleClasses?MzY%3DcGFybV9zdWJq=NjY%3DJQ%3D%3D&NTE%3DbWF4=MTg%3DNTAwMA%3D%3D&NTE%3DcGFybV90ZXJt=ODc%3DMjAyNTEw&NzE%3Db2Zmc2V0=NzM%3DMA%3D%3D&encoded=true'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

resp = httpx.get(url, headers=headers, follow_redirects=True)
html = HTMLParser(resp.text)

# classes = html.css("div#TableCRN30183")
# print(resp.json())

for c in resp.json():
    print(type(c))
