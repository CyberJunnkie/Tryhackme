#!/usr/bin/python3

import requests

host = '10.10.117.17'
url = 'http://{}/th1s_1s_h1dd3n/?secret={}'

for i in range(100):
    r = requests.get(url.format(host, i))
    if not 'That is wrong!' in r.text:
        print("Found secret: {}".format(i))
        print(r.text)
