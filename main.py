from selenium import webdriver
import time

# 변수 설정
ionId = 'ionID' # 여기에 ionID를 입력하세요.
ionPw = 'ionPW' # 여기에 ionPW를 입력하세요.
place = '노트북실' # 여기에 장소를 입력하세요.
teacher = '정두원' # 여기에 선생님 성함을 입력하세요.
cause = '전자기기사용' # 여기에 신청사유를 입력하세요.
when = [0, 1, 2] # 여기에 신청할 시간대를 입력하세요. (0: 8면, 1: 1면, 2: 2면)

# 밑에 있는 코드는 건들지 마세요.
driver = webdriver.Chrome()
url = 'http://ionya.cc'


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
while True:
    try:
        driver.get(url)
        time.sleep(0.75)
        driver.find_element(By.ID, "ionid").send_keys(ionId)
        driver.find_element(By.ID, "pwd").send_keys(ionPw)
        driver.find_element(By.ID, "pwd").send_keys(Keys.ENTER)
        time.sleep(0.75)
    except:
        break

url += '/ns'
driver.get(url)
time.sleep(0.25)

from selenium.webdriver.support.select import Select
ns_time = Select(driver.find_element(By.CLASS_NAME, "form-select"))
ns_place = driver.find_elements(By.CSS_SELECTOR, '.form-control')[0]
ns_teacher = driver.find_elements(By.CSS_SELECTOR, '.form-control')[1]
ns_cause = driver.find_elements(By.CSS_SELECTOR, '.form-control')[2]
ns_place.send_keys(place)
ns_teacher.send_keys(teacher)
ns_cause.send_keys(cause)
ns_zali = driver.find_element(By.ID, 'lnsRr')
ns_zali.click()
for i in when:
    try:
        while True:
            ns_time.select_by_value(str(i))
            time.sleep(1)
            zali = driver.find_elements(By.TAG_NAME, 'button')[-2]
            zali.click()
            submit = driver.find_elements(By.TAG_NAME, 'button')[-1]
            submit.click()
            if driver.find_elements(By.CSS_SELECTOR, 'p')[-1].text == '사용자 보호를 위해 지금은 신청할 수 없습니다.':
                continue
            elif driver.find_elements(By.CSS_SELECTOR, 'p')[-1].text == '신청이 완료되었습니다.':
                break
            elif driver.find_elements(By.CSS_SELECTOR, 'p')[-1].text == '이미 신청한 시간입니다.':
                break
        time.sleep(1)
    except:
        continue

while True:
    pass