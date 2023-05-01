from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 開啟目標網頁
url = "https://www.barco.com/eu-en/support/clickshare-extended-warranty/warranty"
driver = webdriver.Chrome()
driver.get(url)

# 處理網頁彈窗
try:
    # 等待彈窗出現
    popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "onetrust-banner-sdk")))
    # 用 JavaScript 關閉彈窗
    driver.execute_script("arguments[0].style.display='none';", popup)
    # 等待彈窗消失
    WebDriverWait(driver, 10).until_not(EC.visibility_of_element_located((By.ID, "onetrust-banner-sdk")))
except:
    print("No cookie popup found.")

# 等待網頁加載完成
try:
    # 等待 Warranty 欄位出現
    warranty_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "serial")))
except:
    print("Warranty field not found.")
    driver.quit()
    exit()

# 輸入序號，點擊 Get Info 按鈕
warranty_field.send_keys("1863552437")

# 等待 Get Info 按鈕出現，再點擊該按鈕
try:
    get_info_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get info')]")))
    get_info_button.click()
except:
    print("Get Info button not found.")
    driver.quit()
    exit()

# 確認是否有出現指定的文字
try:
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//dd[text()='CLICKSHARE CX-50 SET NA']"), "CLICKSHARE CX-50 SET NA"))
    print("Test Description Passed!")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dd[contains(text(),'R9861522NA')]")))
    print("Test Part number Passed!")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dd[contains(text(),'28 September 2020')]")))
    print("Test Installation date Passed!")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dd[contains(text(),'27 September 2021')]")))
    print("Test Warranty end date Passed!")
except:
    print("Test Failed!")
finally:
    driver.quit()
