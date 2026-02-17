import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(600, 200, 800, 600)
        self.setWindowTitle("Прогноз погоды")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):




app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
