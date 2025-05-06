import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 원하는 설치 경로 설정
custom_driver_folder = "C:/Users/User/Desktop/"

# 크롬드라이버 설치
driver_path = ChromeDriverManager().install()

# 크롬드라이버를 원하는 폴더로 이동 (설치된 드라이버 확인 후 이동)
if not os.path.exists(custom_driver_folder):
    os.makedirs(custom_driver_folder)  # 폴더 없으면 생성

new_driver_path = os.path.join(custom_driver_folder, "chromedriver.exe")

os.rename(driver_path, new_driver_path)  # 드라이버 이동

# 크롬 서비스 실행 (이동한 경로 사용)
service = Service(new_driver_path)
driver = webdriver.Chrome(service=service)

# 브라우저 열기
driver.get("https://www.google.com")
print(driver.title)

# 드라이버 종료
driver.quit()
