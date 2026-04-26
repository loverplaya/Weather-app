from PyQt6.QtGui import QLinearGradient, QColor, QBrush, QPalette


class background:
    def __init__(self, widget):
        self.widget = widget
        self.current_theme = "light"

    def apply_gradient(self):
        w = self.widget.width() if self.widget.width() > 0 else 1366
        h = self.widget.height() if self.widget.height() > 0 else 768

        if self.current_theme == "light":
            gradient = QLinearGradient(0, 0, w, h)
            gradient.setColorAt(0.0, QColor(135, 206, 235))
            gradient.setColorAt(0.5, QColor(100, 180, 255))
            gradient.setColorAt(1.0, QColor(70, 130, 200))
        else:
            gradient = QLinearGradient(0, 0, w, h)
            gradient.setColorAt(0.0, QColor(10, 10, 35))
            gradient.setColorAt(0.5, QColor(35, 15, 65))
            gradient.setColorAt(1.0, QColor(60, 20, 85))

        palette = self.widget.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.widget.setPalette(palette)
        self.widget.setAutoFillBackground(True)

    def set_theme(self, theme):
        self.current_theme = theme
        self.apply_gradient()
