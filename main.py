import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui import Ui_Dialog
from MyQR import myqr

class Dialog(Ui_Dialog, QMainWindow):
    def __init__(self):
        super(Dialog, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.on_pushbutton)


    def on_pushbutton(self):
        info = self.lineEdit.text()
        info2 = self.plainTextEdit.toPlainText()
        text = info
        myqr.run(
            text,
            picture=info2,
            colorized=True,
            version=8
        )

        msgbox = QMessageBox.information(self, "msg", "已完成!!!请在本目录查看")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = Dialog()
    m.show()
    sys.exit(app.exec_())
