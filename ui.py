from main import *

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./SDES.ui")
        binEdit = self.ui.TextlineEdit    # 明密文输入框
        keyEdit = self.ui.KeylineEdit    # 密钥输入框
        encryptBtn = self.ui.EncryptButton    # 加密按钮
        decrypthBtn = self.ui.DecrypthButton    # 解密按钮
        MessageBsr = self.ui.MessageBrowser    # 信息显示区域

        encryptBtn.clicked.connect(lambda: MessageBsr.setText(encrypt_0(binEdit.text(), keyEdit.text())))
        decrypthBtn.clicked.connect(lambda: MessageBsr.setText(decrypt_0(binEdit.text(), keyEdit.text())))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.setWindowTitle('S-DES算法')
    w.ui.show()

    app.exec_()