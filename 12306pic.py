import requests
import os
import hashlib
import time
import random

SAVE_DIR = os.path.abspath(os.path.dirname(__file__)) + "/jpeg/"
req = requests.Session()

if not os.path.exists(SAVE_DIR):
    os.mkdir(SAVE_DIR)

def get_md5(content):
    md5 = hashlib.md5()
    md5.update(content)
    return md5.hexdigest()

FILE_LIST = os.listdir(SAVE_DIR)

while True:
    pic_get = req.get("https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand")
    if pic_get.status_code == 200:
        md5 = get_md5(pic_get.content)
        filename = md5 + ".jpeg"
        if filename not in FILE_LIST:
            with open(SAVE_DIR + filename, "wb") as f:
                f.write(pic_get.content)
            FILE_LIST.append(filename)
    time.sleep(random.randint(3,6))

