#coding=utf8

import requests
import numpy as np
import json

req = requests.get("https://kyfw.12306.cn/otn/resources/js/framework/station_name.js")
name = {}
if req.status_code == 200:
    content = req.content.decode("utf-8")
    # print(content)
    content = content.split("=", 1)[1]
    content = content.rstrip(";")
    content = content.strip("'")
    c = content.split("|")
    total_len = len(c)
    record = total_len // 5
    c = c[0:record*5]
    c = np.array(c)
    c = c.reshape(-1, 5)
    for i in c:
        name[i[1]] = i[2]
        # print(i[1])

# print(json.dumps(name, indent=4))
with open("station.txt", "w") as f:
    f.write(json.dumps(name))