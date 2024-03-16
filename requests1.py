import requests
from bs4 import BeautifulSoup

# 크롤링 기본

# 크롤링하고 싶은 url get해오기
response = requests.get("https://youth.incheon.go.kr/youthpolicy/youthPolicyInfoList.do?")
html = response.text # html 전체 코드 들어있음.
soup = BeautifulSoup(html, 'html.parser') # html 번역기
# soup.select > 여러개 / soup.select_one > 한 개 선택
titles = soup.select(".tit")

for title in titles:
  print(title.text.strip())