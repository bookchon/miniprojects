# NaverApi 클래스 - OpneApi 인터넷 통한 데이터 전달
from urllib.request import Request, urlopen
from urllib.parse import quote
import datetime
import json # 결과는 json으로 리턴 받음

class NaverApi:
    # 생성자
    def __init__(self) -> None:
        print('Naver API 생성')

    # Naver API를 호출하는 제일 중요한 함수 
    def get_request_url(self, url):
        req = Request(url)
        req.add_header('X-Naver-Client-Id', 'O4O_jXgzMYX6jZHmxa8M')
        req.add_header('X-Naver-Client-Secret', 'qyoahKw5MU')

        try:
            res = urlopen(req) # 요청 결과가 바로 돌아옴
            if res.getcode() == 200: # response OK
                print(f'[{datetime. datetime.now()}] NaverAPI 요청 성공')
                return res.read().decode('utf-8')
            else:
                print(f'[{datetime. datetime.now()}] NaverAPI 요청 실패')
                return None
        except Exception as e:
            print(f'[{datetime. datetime.now()}] 예외발생 : {e}')
            return None
        
    # 호출함수
    def get_naver_search(self, node, search, start, display):
        base_url = 'https://openapi.naver.com/v1/search'
        node_url = f'/{node}.json'
        params = f'?query={quote(search)}&start={start}&display={display}'

        url = base_url + node_url + params
        retData = self.get_request_url(url)

        if retData == None:
            return None
        else:
            return json.loads(retData) # json으로 return

    # # json으로 받은 데이터 - list로 바꿈
    # def get_postdata(self, post, outputs):
    #     title = post['title']
    #     description = post['description']
    #     originallink = post['originallink']
    #     link = post['link']

    #     # Tue, 07 Mar 2023 17:04:00 +0900 문자열로 들어온 것을 날짜형으로 변경
    #     pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d, %b, %Y, %H:%M:%S+0900')
    #     pubDate = pDate.strftime('%Y-%m-%d %H:%M:%S') # 2023-03-07 17:04:00로 변경

    #     # outputs에 옮기기
    #     outputs.append({'title':title, 'descritption':description,
    #                     'originallink':originallink, 'link':link,
    #                     'pubDate':pubDate})