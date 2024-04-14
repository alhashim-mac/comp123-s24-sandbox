"""
Inspirational Tutorial: https://www.youtube.com/watch?v=qxj7EXYeNls

Required Packages:
- httpx: alternatives: requests
- selectolax: HTML parser, alternatives: Beautiful Soup
"""

import requests

fall2024_class_schedule_url = 'https://macadmsys.macalester.edu/macssb/internalPb/virtualDomains.classScheduleClasses?MzY%3DcGFybV9zdWJq=NjY%3DJQ%3D%3D&NTE%3DbWF4=MTg%3DNTAwMA%3D%3D&NTE%3DcGFybV90ZXJt=ODc%3DMjAyNTEw&NzE%3Db2Zmc2V0=NzM%3DMA%3D%3D&encoded=true'
classes = requests.get(fall2024_class_schedule_url)
print(type(classes.json()))

for c in classes.json():
    if c["SUBJ_CODE"] != "COMP":
        continue
    print(c)
    # print(f"{c['CRSE_NUMB']} \t {c['SUBJ_CODE']}")
