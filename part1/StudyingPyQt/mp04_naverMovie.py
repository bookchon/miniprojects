# Qt Designer로 디자인
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from NaverAPI import *
from urllib.request import urlopen
import webbrowser # 웹 브라우저 모듈

class qtApp(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('./studyingPyQt/NaverAPIMovie.ui', self)
        self.setWindowIcon(QIcon('./studyingPyQt/movie.png'))

        # 검색 버튼 클릭 시그널에 대한 슬롯 함수
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        # 검색어 입력 후 엔터를 치면 처리
        self.txtSearch.returnPressed.connect(self.txtSearchReturned)
        self.tblResult.doubleClicked.connect(self.tblResultDoubleClicked)

    def tblResultDoubleClicked(self):
        # row = self.tblResult.currentIndex().row()
        # colum = self.tblResult.currentIndex().colum()
        # print(row, colum)
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected, 5).text() # url 링크 컬럼 변경
        webbrowser.open(url) # 네이버 영화 웹사이트

    def txtSearchReturned(self):
        self.btnSearchClicked()

    def btnSearchClicked(self):
        search = self.txtSearch.text()

        if search == '':
            QMessageBox.warning(self, '경고', '영화명을 입력하세요.')
            return
        else:
            api = NaverApi() # NaverApi 클래스 객체 생성
            node = 'movie' # movie로 검색하면 영화검색
            display = 100

            result = api.get_naver_search(node, search, 1, display)
            # print(result)
            # 리스트 뷰에 출력

            items = result['items'] # json 결과 중 items 아래 배열만 추출
            self.makeTable(items) # 테이블 위젯에 데이터들을 할당하는 함수

    def makeTable(self, items) -> None:
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(7) # 컬럼갯수 변경
        self.tblResult.setRowCount(len(items)) # 현재 100개의 행 생성
        self.tblResult.setHorizontalHeaderLabels(['영화제목', '개봉년도', '감독', '배우진', '평점', '링크', '포스터'])
        self.tblResult.setColumnWidth(0, 150)
        self.tblResult.setColumnWidth(1, 70) # 개봉년도
        self.tblResult.setColumnWidth(4, 50) # 평점
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼 데이터 수정 금지

        for i, post in enumerate(items): # 0, 영화
            title = self.replaceHtmlTag(post['title']) # HTML 특수문자 변환 / 영어 제목 가져오기 추가
            subtitle = post['subtitle']
            title = f'{title} ({subtitle})'
            pubDate = post['pubDate']
            director = post['director'].replace('|', ',')[:-1]
            actor = post['actor'].replace('|', ',')[:-1] # 파이썬에서만 가능
            userRating = post['userRating']
            link = post['link']
            img_url = post['image']
            # image = QImage(requests.get(post['image'], stream = True))
            # imgData = urlopen(post['image']).read()
            # image = QPixmap()

            if img_url != '': # 빈 값이면 포스터가 없음
                data = urlopen(img_url).read() # 웹을 통해서 파이썬 2진 데이터를 만들어줌(텍스트 형태)
                image = QImage() # 텍스트 형태를 이미지 객체로 변경
                image.loadFromData(data)
                # QTableWidget 이미지를 그냥 넣을 수 없음. QLabel() 집어넣은 뒤 QLabel -> QTableWidget 할당
                imgLabel = QLabel()
                imgLabel.setPixmap(QPixmap(image))

                #테스트
                # f = open(f'./studyingPyQt/temp/image_{i+1}.png', mode='wb') # 파일쓰기
                # f.write(data)
                # f.close() # 파일에 있는 데이터를 이미지로 저장할 수 있음
                
            # if imgData != None:
            #     image.loadFromData(imgData)
            #     imgLabel = QLabel()
            #     imgLabel.setPixmap(image)
            #     imgLabel.setGeometry(0, 0, 60, 100)
            #     imgLabel.resize(60, 100)

            # setItem(행, 열, 넣을 데이터)
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(director))
            self.tblResult.setItem(i, 3, QTableWidgetItem(actor))
            self.tblResult.setItem(i, 4, QTableWidgetItem(userRating))
            self.tblResult.setItem(i, 5, QTableWidgetItem(link))
            self.tblResult.setItem(i, 6, QTableWidgetItem(img_url))

            if img_url != '':
                self.tblResult.setCellWidget(i, 6, imgLabel)
                self.tblResult.setRowHeight(i, 110) # 포스터가 있으면 쉘 높이를 늘림
            else:
                self.tblResultsetItem(1, 6, QTableWidgetItem('No Poster'))

    def replaceHtmlTag(self, sentence) -> str:
        result = sentence.replace('&lt;', '<').replace('&gt;', '.').replace('<b>', '').replace('</b>', '').replace('&apos', "'").replace('&quot', '"')   

        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())