import chromedriver_autoinstaller

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)



driver.get('https://www.nike.com/kr/ko_kr/')


# id = input("아이디를 입력해주세요 : ")  #akdls7900@gmail.com
# pw = input("비밀번호를 입력해주세요 : ") #Akdls6661@

id = "akdls7900@gmail.com"
pw = "Akdls6661@"

try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'login')))
    elem_btn = driver.find_element(By.CLASS_NAME, 'login')
    elem_btn.click() # 버튼 클릭

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'j_username')))
    elem_id = driver.find_element(By.ID, 'j_username')
    elem_id.send_keys(id) # id 입력

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'j_password')))
    elem_pw = driver.find_element(By.ID, 'j_password')
    elem_pw.send_keys(pw)

    login_btn = driver.find_element(By.XPATH, '//button[@class="button large width-max"]')
    login_btn.click()
except: # 이미 로그인이 되어있는 경우
    pass


WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.LINK_TEXT, "Men")))
men_btn = driver.find_element(By.LINK_TEXT, "Men")
men_btn.click()

WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.LINK_TEXT, "신발")))
men_btn = driver.find_element(By.LINK_TEXT, "신발")
men_btn.click()

# WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/section/section/section/article/div/div[2]/ul/li[1]/div/div[1]/a/div[2]/div[1]/img")))
# shoe_btn = driver.find_element(By.XPATH, "/html/body/section/section/section/article/div/div[2]/ul/li[1]/div/div[1]/a/div[2]/div[1]/img")
# shoe_btn.click()

a = input()
