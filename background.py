from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QLinearGradient, QColor, QBrush, QPalette

class background:
    def __init__(self, widget):
        self.widget = widget

    def apply_gradient(self):
        gradient = QLinearGradient(0, 0, self.widget.width(), self.widget.height())
        gradient.setColorAt(0.0, QColor(135, 206, 235))
        gradient.setColorAt(0.5, QColor(100, 180, 255))
        gradient.setColorAt(1.0, QColor(70, 130, 200))

        palette = self.widget.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.widget.setPalette(palette)
