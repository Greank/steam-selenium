from selenium import webdriver
import time
import csv
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 使用 webdriver-manager 自動下載和配置 ChromeDriver
service = Service(ChromeDriverManager().install())

# 設置 Chrome 瀏覽器選項
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # 全螢幕啟動

driver = webdriver.Chrome(service=service, options=chrome_options)

# 前往目標網站
driver.get("https://gamalytic.com/game-list")

# 等待網頁讀取完成
driver.implicitly_wait(10)

try:
    # 等待特定的 div 元素可見
    target_div = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'div.MuiDataGrid-virtualScroller.css-1grl8tv'))
    )

    # 修改網頁指定的 div 元素
    script = """
    var targetDiv = document.querySelector('div.MuiDataGrid-virtualScrollerContent.MuiDataGrid-virtualScrollerContent--overflowed.css-0'); 
    targetDiv.style.height = '10000px';
    """
    driver.execute_script(script)

    time.sleep(10)

    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", target_div)

    # 修改網頁指定的 div 元素
    script = """
    var targetDiv = document.querySelector('div.MuiDataGrid-virtualScroller.css-1grl8tv');
    targetDiv.style.height = '10000px';
    """
    driver.execute_script(script)

    time.sleep(10)

except Exception as e:
    print(f"Error: {e}")

# 創建 CSV 文件並寫入標題行
with open('game_data.csv', 'w', newline='', encoding='utf-16') as csvfile:
    fieldnames = ['遊戲名稱', '網頁連結', '發售日期', '售出數量', '遊戲單價'
    , '銷售總額', '玩家平均遊玩時間', '玩家評價分數', '開發商分級', '發行商', '開發商']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()

    while True:
        try:

            # 獲取網頁內容
            html = driver.page_source

            # 解析 HTML
            soup = BeautifulSoup(html, 'html.parser')
            # 透過字典抓取 role = row的所有元素 與 class = MuiDataGrid-row 的所有元素
            rows = soup.find_all('div', {'role': 'row', 'class': 'MuiDataGrid-row'})
                

            # 解析每一行並寫入 CSV 文件
            for row in rows:
                game_data = {}
                #透過字典抓取 data-field 各個指定的text，並放入字典中
                game_data['遊戲名稱'] = row.find('div', {'data-field': 'name'}).get_text(strip=True)
                game_data['網頁連結'] = row.find('div', {'data-field': 'name'}).find('a')['href']
                game_data['發售日期'] = row.find('div', {'data-field': 'releaseDate'}).get_text(strip=True)
                game_data['售出數量'] = row.find('div', {'data-field': 'copiesSold'}).get_text(strip=True)
                game_data['遊戲單價'] = row.find('div', {'data-field': 'price'}).get_text(strip=True)
                game_data['銷售總額'] = row.find('div', {'data-field': 'revenue'}).get_text(strip=True)
                game_data['玩家平均遊玩時間'] = row.find('div', {'data-field': 'avgPlaytime'}).get_text(strip=True)
                game_data['玩家評價分數'] = row.find('div', {'data-field': 'reviewScore'}).get_text(strip=True)
                game_data['開發商分級'] = row.find('div', {'data-field': 'publisherClass'}).get_text(strip=True)
                game_data['發行商'] = row.find('div', {'data-field': 'publishers'}).get_text(strip=True)
                game_data['開發商'] = row.find('div', {'data-field': 'developers'}).get_text(strip=True)
                print(game_data)
                writer.writerow(game_data)

            # 找到並點擊下一頁按鈕
            next_button = driver.find_element(By.CSS_SELECTOR, 'svg[data-testid="KeyboardArrowRightIcon"]')
            next_button.click()
            time.sleep(5)  # 給予頁面加載時間
        except e:
            print(e)
            break
# 關閉瀏覽器
driver.quit()