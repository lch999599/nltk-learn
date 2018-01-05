#coding=utf8

from splinter import Browser

'''
http://splinter.readthedocs.io/en/latest/drivers/chrome.html

余票查询接口：
https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2018-02-03&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=CDW&purpose_codes=ADULT
{"data":{"flag":"1","map":{"AOH":"上海虹桥","CDW":"成都","ICW":"成都东","SHH":"上海","SNH":"上海南"},"result":
    ["|预订|5l0000D35271|D352|AOH|ICW|AOH|ICW|06:04|20:27|14:23|N|Dl3cPlJfDg2qYoAjpyL26fG8w0T1ZkyniDfYhSNEZmLjfBBg|20180203|3|H2|01|20|0|0|||||||无||||无|无|||O0O0M0|OOM|0",
    "|预订|5l0000D63633|D636|AOH|ICW|AOH|ICW|06:12|22:03|15:51|N|dcFJmimL4zGC%2BR0eTv3hte3Q53Uzzt29BeVVuKNM4e9MfNnl|20180203|3|H2|01|25|0|0|||||||无||||无|无|||O0M0O0|OMO|0","|预订|5l000D220663|D2206|AOH|CDW|AOH|CDW|06:38|22:01|15:23|N|InSNvMNoL8Obk0BFds616xmjwsxugWcPcf%2FJ7JQLt0g3crFW|20180203|3|H3|01|25|0|0|||||||无||||无|无|||O0M0O0|OMO|0","|预订|550000D95200|D952|SHH|ICW|SHH|ICW|08:30|21:28|12:58|N|q0Om8SHvzCz7CJKVWjceygu%2FmU%2B42%2FqHkNZurtbWy7GTcBe0TVqfzw%2BT640%3D|20180203|3|H6|01|09|1|0||无|无||||无||||无|||无|O0F0A0O0|OFAO|0","|预订|550000K29058|K290|SHH|CDW|SHH|CDW|08:51|21:35|36:44|N|wnegli2OAQSv7MJDP33j7d9VoVzJrjzhoJZ7uqqAY8AsR5gGv%2BBEJvjt4JE%3D|20180203|3|H2|01|25|0|0||||无|||无||无|无|||||10401030|1413|0","|预订|55000K115650|K1156|SHH|CDW|SHH|CDW|11:16|15:30|28:14|N|zYYMZ18%2F%2FDgejR5y4TvI6aDhnLw6b%2BRkJw6P608nVBPtAGa3gapIzATd3ys%3D|20180203|3|H6|01|21|0|0||||无|||无||无|无|||||10401030|1413|0","|预订|550000321640|3216|SHH|CDW|SHH|CDW|13:03|00:28|35:25|N|2RNBWesfnH38egdBRxkowF%2FoaYR1PUNI|20180203|0|HZ|01|19|0|0|||||||无|||无|||||1010|11|0","|预订|55000K413840|K4138|SHH|CDW|SHH|CDW|15:39|09:59|42:20|N|j6Fm%2FBa5wEW%2FpCznan1yeUYSfHdeLKFI|20180203|3|H1|01|16|0|0|||||||无|||无|||||1010|11|0","jPfDlXBXgoCW5nmzelCo%2BEDDI3U3u0VZ9knquwfXxBIYa3DVvWXGWfHQodQP0siZvOu8ggCvVi8n%0A0Pyg21ttwNcJ%2FprC7mrNBctImmphDuOcEMPdkGsDA4d0LpQhMND6RQmjVohVqnnzLn2YzCdVDjsu%0AU5kMHuK9E6VOEU2vXKO0zhHzBaeVoIEeI%2BWQXE14NWMLEoGw%2Bmi3xKbTFd6ODFcmt0FQ2nucT9k%2F%0ArvTk3SbCai8b3GbnOl3dxrSiwK19%2FzkayHUGdhM%3D|预订|550000K35101|K351|SNH|CDW|SNH|CDW|15:43|04:49|37:06|Y|sxbJevlDO3c1vQ3xKVKiSdj32GBGVeSH4lGIsuoXckyo5dgyROEENm7d7aI%3D|20180203|3|H3|01|32|0|0||||无|||有||无|无|||||10401030|1413|0","|预订|550000325651|3256|SHH|CDW|SHH|CDW|17:13|15:50|46:37|N|hcEXXbS6xWRPyfZ6g3oesloU%2FEvWMTxURwGYeIlzXe3y8sg5|20180203|0|HZ|01|18|0|0|||||||无||无|无|||||101030|113|0","pLAaO8DyBo3m%2FQMLqEV0lqwm36QIsjRHKRJvQeHysyb2Aj0HpK1BbuG%2FZ3%2F9APjtPU8n%2BBCFjcRG%0AgqINQTeM9ceuHFVzqsUWOALWdzFOgW5H5yopT0ClL%2FUcKfNN0eV9a2rlfEgub2Ft7Wqc%2BV4SQKgE%0AbLf4cWXp9wYocT9peU1SbsbMd2szSqvpZeitbxPokvd7X1IhCNY8xbSOGl7E7XHNQmD4J7U4DMas%0AFIDNycPMrzNgGMy891euMK6izpa8p%2F2zZg%3D%3D|预订|550000K282B4|K282|SHH|CDW|SHH|CDW|20:46|11:18|38:32|Y|5tlj831HuDuWOki78oGRPwuzN0e931rXToqiQQoRn5U6MfKL%2BKenmwtlfuE%3D|20180203|3|H3|01|26|0|0||||无|||有||无|无|||||10401030|1413|0","|预订|55000K463610|K4636|SHH|ICW|SHH|ICW|21:13|04:40|31:27|N|y9niPmqx1W8P59Zu4%2BGzhf4EBCadt2rWQxfP85B1QLF1Qa4RHHb4x0Ytgu4%3D|20180203|3|H1|01|17|1|0||||无|||无||无|无|||||10401030|1413|0"]},"httpstatus":200,"messages":"","status":true}


https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2018-02-03&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=CDW&purpose_codes=ADULT


'''

class qiangpiao():
    def __init__(self):
        self.login_url = "https://kyfw.12306.cn/otn/login/init"
        self.driver = Browser(driver_name='chrome', executable_path="C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
        # self.login()

    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill("loginUserDTO.user_name", "wordgod")
        self.driver.fill("userDTO.password", "wordgod")

qiangpiao()