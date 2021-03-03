import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)

#図書館の検索部分にアクセス
url = "https://~~~"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

class_name = []
#専門図書館指定
#資料種別指定 
class_name = ['~~~~~']

#checkboxのクリック
for c_name in class_name:
    driver.execute_script("arguments[0].click();",driver.find_element_by_class_name(c_name))
    time.sleep(1)

#出版年の指定
year_from = driver.find_element_by_id("local_comp_search_year_from")
year_from.send_keys(2020)
time.sleep(1)

#言語指定
lang = driver.find_element_by_id("local_comp_search_lang")
lang.send_keys("jpn")
time.sleep(1)

#新着の指定
arrived_within = driver.find_element_by_id("local_comp_search_arrivedwithin")
arrived_within.send_keys(1)

#検索
driver.find_element_by_name("search").click()
time.sleep(5)

#一覧が複数ページのときの処理
first_page = driver.find_element_by_class_name("l_page_current_hidden").get_attribute("value")
end_page = driver.find_element_by_class_name("l_page_total_hidden").get_attribute("value")
page_count = int(end_page) - int(first_page)
print("@ページ数",page_count)
# page_count = 0
book_url_list = []
while True:
    #一覧ページのaタグの情報
    # listElements = driver.find_elements_by_xpath("//div[@class='informationArea c_information_area l_informationArea']/h3/a")
    
    #タイトル取得
    soup = BeautifulSoup(driver.page_source,"html.parser")
    result = soup.find("div", attrs={"id": "resultContents"})
    h_tag = result.find_all("h3")
    for h in h_tag:
        title = h.find("a").get_text()
        print(title)

    if page_count == 0:
        break
    page_count -= 1
    driver.execute_script("arguments[0].click();",driver.find_element_by_class_name("l_volume_page_next"))
    time.sleep(10)

time.sleep(3)
driver.quit()