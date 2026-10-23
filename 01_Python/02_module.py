# 1. 내부(표준) 모듈 - 별도의 설치가 필요하지 않음
import math
print("루트 16", math.sqrt(16)) # 제곱 math.pow(4,3)

import random
print("점심 메뉴 선정:", random.choice(["김밥", "라면", "비빔밥"]))

from datetime import datetime
print("현재시간: ", datetime.now())
print("현재시간: ", datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분"))
print()

# 2. 외부모듈 - 별도의 설치가 필요
#   패키지(모듈:라이브러리) 설치 도구 pip
# 설치 목록 확인 : pip list

# 1) HTTP 통신을 위한 외부 모듈 requests
# 설치 방법
# > python3.15 -m pip install requests
# > python -m pip install requests # PATH 지정된 python 버전으로 설치
# > pip install requests # 위와 동일
import requests
response = requests.get("https://example.com", timeout=5)
print("응답코드: ", response.status_code)
# 200 OK
# 404, 403 에러
print("응답글씨: ", response.text)

# 여러개의 모듈을 한번에 설치.
# numpy, pandas, matplotlib, selenium
# pip install numpy pandas matplotlib selenium
# 한번에 설치 가능 띄어쓰기로 구분, 모듈의 이름에 띄어쓰기가 있으면 "" 로 하기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

aaa = np.array([10,20,30])
print(aaa.mean()) # 평균

bbb = pd.DataFrame({
    "name":["sam", "robin", "hong"],
    "score" :[80, 95, 70]
})
print(bbb)
print(round(bbb["score"].mean(),3))
# round 반올림 원하는 자릿수 round(###, n)

plt.figure(figsize=(5,3))
plt.bar(bbb["name"], bbb["score"])
plt.title("student scores")
plt.ylim(0, 100) # limit
plt.tight_layout()
# plt.show()

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
save_path = BASE_DIR / "student_scores.png"
plt.savefig(save_path)
plt.close()

# 웹 브라우저 자동화 모듈 - RPA 작업 또는 AI Agent 만들때 활용 가능
from selenium import webdriver
chrome = webdriver.Chrome()
chrome.get("https://naver.com")

import time
time.sleep(2)

from selenium.webdriver.common.by import By

search_box = chrome.find_element(By.ID, "query")
search_box.send_keys("스타벅스")
time.sleep(2)

from selenium.webdriver.common.keys import Keys
search_box.send_keys(Keys.ENTER)

time.sleep(3)

# 가상환경 만들기
# python -m venv venv

# 가상환경 실행
# venv/Scripts/activate -- windows
# source venv/bin/activate -- macos, linux

# 가상환경 종료
# deactivate