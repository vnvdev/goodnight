from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random

nn  = ['Ngủ ngon em nhé <3 <3', 'Anh chúc em ngủ ngon. <3', 'Em ngủ ngon <3']
nm = ['Chúc em ngày mới tốt lành <3', 'Anh chúc em ngày mới gặp nhiều may mắn <3', 'Chúc em buổi sáng bình an <3']

while True:
    t = time.localtime(time.time())
    hr = t.tm_hour
    mi = t.tm_min
    m = random.randint(30, 45)
    if hr == 22 and mi >= m:
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\")
        options.add_argument(f"--profile-directory=Profile 1")
        driver = webdriver.Chrome(options=options)
        driver.get(f"https://www.facebook.com/tran1337av.n")
        h1_element = driver.find_element(By.CSS_SELECTOR, "h1.x1heor9g.x1qlqyl8.x1pd3egz.x1a2a7pz")
        text = h1_element.text
        js_script = "var addButton = null; \
                    var divs = document.getElementsByTagName('div'); \
                    for (var i = 0; i < divs.length; i++) { \
                        if (divs[i].getAttribute('aria-label') == 'Nhắn tin') { \
                            addButton = divs[i]; \
                            break; \
                        } \
                    } \
                    if (addButton != null) { \
                        addButton.click(); \
                    }"
        driver.execute_script(js_script)
        time.sleep(3)
        message = random.choice(nn)
        wait = WebDriverWait(driver, 10)
        input_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox'][aria-label='Tin nhắn']")))
        input_box.send_keys(f"{message}"+ Keys.RETURN)
        time.sleep(3)
        driver.quit()
        time.sleep(25200)
    if hr == 6 and mi >= m:
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\")
        options.add_argument(f"--profile-directory=Profile 1")
        driver = webdriver.Chrome(options=options)
        driver.get(f"https://www.facebook.com/tran1337av.n")
        h1_element = driver.find_element(By.CSS_SELECTOR, "h1.x1heor9g.x1qlqyl8.x1pd3egz.x1a2a7pz")
        text = h1_element.text
        js_script = "var addButton = null; \
                    var divs = document.getElementsByTagName('div'); \
                    for (var i = 0; i < divs.length; i++) { \
                        if (divs[i].getAttribute('aria-label') == 'Nhắn tin') { \
                            addButton = divs[i]; \
                            break; \
                        } \
                    } \
                    if (addButton != null) { \
                        addButton.click(); \
                    }"
        driver.execute_script(js_script)
        time.sleep(3)
        message = random.choice(nm)
        wait = WebDriverWait(driver, 10)
        input_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox'][aria-label='Tin nhắn']")))
        input_box.send_keys(f"{message}"+ Keys.RETURN)
        time.sleep(3)
        driver.quit()
        time.sleep(57000)        
    time.sleep(20)
