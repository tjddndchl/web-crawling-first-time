import requests #웹에다 정보요청하기
from bs4 import BeautifulSoup #정보 해석 기능 제공 클래스

# 네이버 증권 : https://finance.naver.com/

response = requests.get("https://finance.naver.com/")
html = response.text# 웹 페이지는 html언어로 되어있다!

result = BeautifulSoup(html,"html.parser")

# 이 사이트에서는 '오늘의 증시'라는 글자를 h2 태그에 h_market 클래스를 붙여 표시하고 있다!
# 그리고 나는 이 정보만 따로 가져와서 보고 싶다.

info = result.select_one("h2.h_market")
print(info.text)
