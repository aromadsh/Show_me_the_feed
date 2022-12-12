import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from bs4 import BeautifulSoup
import clipboard

def EngtoKor(txt_eng):
    txt=txt_eng+'.'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach',True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

    #driver.maximize_window()

    driver.get('https://papago.naver.com/')
    time.sleep(3)

    # 번역할 내용 입력
    driver.find_element(By.CLASS_NAME, 'edit_box___1KtZ3').send_keys(txt)
    time.sleep(1)

    # 번역 버튼 클릭
    driver.find_element(By.CLASS_NAME, 'btn_text___3-laJ').click()
    time.sleep(3)

    # 번역된 내용 복사 버튼 눌러 복사하기
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/section/div/div[1]/div[2]/div/div[7]/span[2]/span/span/button').click()
    time.sleep(2)

    result = clipboard.paste()
    return str(result)