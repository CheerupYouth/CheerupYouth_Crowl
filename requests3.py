import requests
from bs4 import BeautifulSoup

# 여러 페이지 가져오기
pageNum = 1 
for i in range(1, 10):
  print(f'{pageNum}페이지입니다.')
  response = requests.get(f'https://youth.incheon.go.kr/youthpolicy/youthPolicyInfoList.do?menudiv=dwelling&pgno={i}')
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  titles = soup.select(".boardList .con-box .tit") # 정책 title
  links = soup.select(".boardList .btn-box .btn:first-child") # 정책 title
  
  # for link in links:
  #   url = link.attrs['href']
  #   print(f'https://youth.incheon.go.kr{url}')
    
  for title in titles:
    print(title.text.strip())
  pageNum += 1