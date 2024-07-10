import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


def vpn():
    # 禁用瀏覽器彈窗避免預設路徑載入失敗
    prefs = {'profile.default_content_setting_values':{'notifications': 2}}

    # 使用 webdriver-manager 自動下載和配置 ChromeDriver
    service = Service(ChromeDriverManager().install())

    # 設置 Chrome 瀏覽器選項
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # 全螢幕啟動
    # chrome_options.add_argument("--disable-popup-blocking")  # 禁止彈出窗口
    # chrome_options.add_argument("--disable-extensions")     # 禁止擴展
    # chrome_options.add_argument("--disable-infobars")       # 禁止信息提示
    # chrome_options.add_argument("--disable-notifications")  # 禁止通知

    #找到Google擴充套件的檔案位置
    chrome_options.add_extension('1.2.7_0.crx')
    #將擴充套件放入至Webdriver的開啟網頁內容
    chrome_options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    time.sleep(5)
    while True:
        #啟動擴充套件連上VPN 
        driver.get("chrome-extension://nhnfcgpcbfclhfafjlooihdfghaeinfc/popup.html")

        try:
            # 等待特定的 div 元素可見
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.row'))
            )

            #透過find_element_by_xpath找到點擊的位置並且點擊
            driver.find_element(By.XPATH, '//*[@class="country-list"]/div['+str(random.randint(1,8))+']').click()

            #透過find_element_by_xpath找到點擊的位置並且點擊
            driver.find_element(By.XPATH, '//*[@class="switch"]/button[1]').click()

            time.sleep(5)

            break
        except:
            time.sleep(1)

    return driver

vpn()
