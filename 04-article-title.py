import requests
from bs4 import BeautifulSoup

response = requests.get("https://entertain.naver.com/movie")

html = response.text

soup = BeautifulSoup(html,"html.parser")
#select_one() 은 해당하는 정보 하나를 가져온다.
#select()는 해당하는 정보라면 모두 골라서 다 가져온다.
titles = soup.select("a.tit")

# 미션1, 관심있는 키워드를 프로그램 실행시 직적 입력하자
keyword = input('관심있는 키워드를 입력하세요:')

for title in titles :
#내가 입력한 키워드가 포함된 제목만 화면에 출력하자
    if keyword in title.text :   
        print(title.text)

 

