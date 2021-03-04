import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
import threading

# LINEに通知させる関数
def line_notify(message):
    line_notify_token = 'トークン'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)

#なにかが起こって強制終了するとき用
def thread():
    # driver.quit()
    line_notify("エラーが発生しています")
    exit()

#Headless
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--start-maximized')
options.add_argument('--headless')

#図書館の検索部分にアクセス
url = "url"
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(3)

class_name = []
#専門図書館指定
#資料種別指定 全て→図書→雑誌
class_name = ['~~']

#checkboxのクリック
for c_name in class_name:
    driver.execute_script("arguments[0].click();",driver.find_element_by_class_name(c_name))
    time.sleep(1)

#出版年の指定
year_from = driver.find_element_by_id("~")
year_from.send_keys(2020)
time.sleep(1)

#言語指定
lang = driver.find_element_by_id("~")
lang.send_keys("~")
time.sleep(1)

#新着の指定
arrived_within = driver.find_element_by_id("~")
arrived_within.send_keys(1)

#検索
driver.find_element_by_name("~").click()
time.sleep(5)

#一覧が複数ページのときの処理
first_page = driver.find_element_by_class_name("~").get_attribute("~")
end_page = driver.find_element_by_class_name("~").get_attribute("~")
page_count = int(end_page) - int(first_page)


#現在時刻を取得
dt_now = datetime.datetime.now()
# page_count = 0
# book_url_list = []

#取得した日時を最初につけておく
title = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')

#念の為5分で強制終了するようにする
t = threading.Timer(300, thread)
t.start()

while True:
    #一覧ページのaタグの情報
    # listElements = driver.find_elements_by_xpath("//div[@class='informationArea c_information_area l_informationArea']/h3/a")
    
    #タイトル取得
    soup = BeautifulSoup(driver.page_source,"html.parser")
    result = soup.find("~", attrs={"~": "~"})
    h_tag = result.find_all("~")
    for h in h_tag:
        title += '\n' + '・' + h.find("~").get_text() + '\n'

    if page_count == 0:
        break
    page_count -= 1
    
    driver.execute_script("arguments[0].click();",driver.find_element_by_class_name("~"))
    time.sleep(10)


#LINEに通知する
line_notify(title)

time.sleep(3)

driver.quit()

exit()