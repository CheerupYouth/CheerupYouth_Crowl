# 가져온 데이터 엑셀파일로 저장
import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r'C:\Users\tmdgm\Desktop\pyex\주거정책_data.xlsx'

wb = openpyxl.load_workbook(fpath)
ws = wb.active # 현재 활성화된 시트 선택 - 기본시트 선택

row = 2
for i in range(1, 5):
  response = requests.get(f'https://youth.incheon.go.kr/youthpolicy/youthPolicyInfoList.do?menudiv=dwelling&pgno={i}')
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  titles = soup.select(".boardList .con-box .tit") # 정책 title
  links = soup.select(".boardList .btn-box .btn:first-child") # 정책 url
  
  # for link in links:
  #   url = link.attrs['href']
  #   print(f'https://youth.incheon.go.kr{url}')
    
  for title in titles:
    print(title.text.strip())
    ws[f'B{row}'] = title.text
    row += 1
    
wb.save(fpath)