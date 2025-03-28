from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from AppOpener_ui import Ui_Form
import os


class TestApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.openApp)

    def openApp(self):
        if self.comboBox.currentIndex() == 0:
            os.popen("python main.py")
            # os.popen("A_and_B.exe")
        else:
            os.popen("python main.py")
            # os.popen("B_only.exe")

        self.close()

if __name__ == "__main__":
    app = QApplication([])
    window = TestApp()
    window.show()
    app.exec()