import sys
import os

from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QUrl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.setWindowTitle("BroTL")

        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "index.html")
        self.browser.setUrl(QUrl.fromLocalFile(path))
        
        self.setCentralWidget(self.browser)

        self.show()

app = QApplication(sys.argv)
window = MainWindow()

app.exec_()