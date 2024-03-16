import requests
from bs4 import BeautifulSoup

response = requests.get("https://youth.incheon.go.kr/youthpolicy/youthPolicyInfoList.do?menudiv=dwelling")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select(".boardList .con-box .tit") # 정책 title
links = soup.select(".boardList .btn-box .btn:first-child") # 해당 정책 URL 접근

for link in links:
  url = link.attrs['href']
  print(f'https://youth.incheon.go.kr{url}')

  