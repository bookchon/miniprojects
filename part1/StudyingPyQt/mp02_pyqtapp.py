# Qt Designer로 디자인
import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *

class qtApp(QWidget):
    count = 0 # 클릭 횟수 카운트 변수

    def __init__(self):
        super().__init__()
        uic.loadUi('./studyingPyQt/mainapp.ui', self)

    # Qt Designer에서 구성한 위젯 시그널
        self.btnOk.clicked.connect(self.btnOkClicked)
        self.btnPOP.clicked.connect(self.btnPOPClicked)

    def btnPOPClicked(self):
        QMessageBox.about(self, 'popup', '까꿍')

    def btnOkClicked(self):
        self.count += 1
        self.lblMessage.clear()
        self.lblMessage.setText(f'메시지 ok + {self.count}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())