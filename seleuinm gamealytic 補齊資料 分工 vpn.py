import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import threading
import time
import seleuinm_vpn

def web_selenium(csv1,csv2):
    
    #呼叫seleuinm_vpn內的vpn()
    driver = seleuinm_vpn.vpn()

    # 讀取原始CSV檔案
    input_file = csv1+'.csv'
    output_file = csv2+'.csv'

    # 讀取CSV檔案內容
    with open(input_file, mode='r', newline='', encoding='utf-16') as infile:
        reader = csv.DictReader(infile, delimiter='\t')
        fieldnames = reader.fieldnames + ['模式', '語言', '標籤', '玩家評價次數', '玩家平均每日遊玩人數', '關注人數', '玩家國家佔比']
        rows = list(reader)

    # 寫入新的CSV檔案
    with open(output_file, mode='a', newline='', encoding='utf-16') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()

        for row in rows:
            #讀取的CSV裡的網頁連結欄位，把值帶入url，並前往網頁
            url = row['網頁連結']
            driver.get('https://gamalytic.com' + url)
            
            #被IP限制的判斷
            while True:
                try:
                    
                    # 等待特定的 div 元素可見
                    WebDriverWait(driver, 60).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.MuiCardContent-root.css-1qw96cp')))

                    break

                except:

                    # 關閉瀏覽器
                    driver.quit()

                    time.sleep(5)

                    driver = seleuinm_vpn.vpn()

                    driver.get('https://gamalytic.com' + url)

                    time.sleep(5)

            # 獲取頁面內容
            page_content = driver.page_source

            # 解析網頁內容
            soup = BeautifulSoup(page_content, 'html.parser')
                    

            try:
                genres_value=''
                languages_value=''
                tags_value=''
                reviews_value=''
                average_value=''
                followers_value=''
                country_value=''

                # 提取包含 Overview 標題的父層 div 內容
                overview_section = soup.find('h6', string='Overview').find_parent('div', class_='MuiCardContent-root')

                # 提取模式、語言、標籤
                genres_value = overview_section.find('b', string='Genres: ').find_next('div').text.strip()
                languages_value = overview_section.find('b', string='Languages: ').find_next('div').text.strip()
                tags_value = overview_section.find('b', string='Tags: ').find_next('div').text.strip()

                # 提取統計信息
                stats_header = soup.find('h6', string='Stats').find_parent('div', class_='MuiCardContent-root')
                reviews_value = stats_header.find('b', string='Reviews: ').find_next('div').text.strip()
                average_value = stats_header.find('b', string='Average daily concurrent players: ').find_next('div').text.strip()
                followers_value = stats_header.find('b', string='Followers: ').find_next('div').text.strip()

                # 提取各國玩家占比
                players_by_country_header = soup.find('div', string='Players by country: ').find_parent('div', class_='MuiBox-root')
                players_by_country_items = players_by_country_header.find_all('div', class_='css-fhxiwe')
                country_data = []
                for item in players_by_country_items:
                    img_tag = item.find("img")
                    p_tag = item.find("p")
                    if img_tag and p_tag:
                        alt_value = img_tag.get("alt")
                        text_content = p_tag.text.strip()
                        country_data.append(f"{alt_value}: {text_content}")
                    else:
                        others_value = item.find('p').text.strip()
                country_data.append(others_value)
                country_value = ', '.join(country_data)

            except Exception as e:
                print(f"Error processing {url}: {e}")
            
            # 更新列的數據
            row.update({
                '模式': genres_value,
                '語言': languages_value,
                '標籤': tags_value,
                '玩家評價次數': reviews_value,
                '玩家平均每日遊玩人數': average_value,
                '關注人數': followers_value,
                '玩家國家佔比': country_value
                })

            # 寫入更新後的列到新的CSV
            writer.writerow(row)

    driver.quit()

csvs = [
    ('game_data1', 'game_data1_up'),
    ('game_data2', 'game_data2_up'),
    ('game_data3', 'game_data3_up'),
    ('game_data4', 'game_data4_up'),
    ('game_data5', 'game_data5_up'),
    ('game_data6', 'game_data6_up'),
    ('game_data7', 'game_data7_up'),
    ('game_data8', 'game_data8_up')
]

jobs = [threading.Thread(target=web_selenium, args=csv) for csv in csvs]

for job in jobs:
    job.start()
    time.sleep(10)
    

for job in jobs:
    job.join()