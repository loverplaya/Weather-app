class ButtonStyle:
    weather_btn = """QPushButton {
                                            background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                            stop: 0 #3498db, stop: 1 #9b59b6); 
                                            color: white;
                                            border: none;
                                            border-radius: 25px;
                                            font-size: 16px;
                                            font-weight: bold;
                                            padding: 10px 20px;
                                        }
                                                                     QPushButton:hover {
                                            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                                                       stop: 0 #2980b9, stop: 1 #1c6ea9);
                                            border: 2px solid white;
                                        }
                                        QPushButton:pressed {
                                            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                                                       stop: 0 #1c6ea9, stop: 1 #154360);
                                        }
                                    """
    weather_btn_dark = """QPushButton {
                                            background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                                stop: 0 #3a1c6e, stop: 1 #1e3a5f);
                                            color: white;
                                            border: 2px solid #7c4dff;
                                            border-radius: 25px;
                                            font-size: 16px;
                                            font-weight: bold;
                                            padding: 10px 20px;
                                        }
                                        QPushButton:hover {
                                            background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                                stop: 0 #4a2c8e, stop: 1 #2e4a7f);
                                            border: 2px solid #9b6dff;
                                        }
                                        QPushButton:pressed {
                                            background-color: #2a1050;
                                            border: 2px solid #5a2dff;
                                        }"""

    back_btn = """QPushButton {
        background-color: #555;
        color: white;
        border: none;
        border-radius: 15px;
        font-size: 14px;
        padding: 8px 16px;
    }
    QPushButton:hover {
        background-color: #777;
    }"""

    back_btn_dark = """QPushButton {
        background-color: #333;
        color: white;
        border: none;
        border-radius: 15px;
        font-size: 14px;
        padding: 8px 16px;
    }
    QPushButton:hover {
        background-color: #555;
    }"""

    fav_btn = """
        QPushButton {
            font-size: 24px;
            font-weight: bold;
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 #3a1c6e, stop: 1 #1e3a5f);
            color: #ffd700;
            border: 2px solid #ffd700;
            border-radius: 25px;
            padding: 8px;
        }
        QPushButton:hover {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 #4a2c8e, stop: 1 #2e4a7f);
            border: 2px solid #ffea00;
            color: #ffea00;
        }
        QPushButton:pressed {
            background: #2a1050;
        }
    """

    fav_btn_active = """
            QPushButton {
                font-size: 28px;
                background-color: gold;
                color: black;
                border: 2px solid gold;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: rgba(255, 215, 0, 0.8);
            }
        """


class LineEdit_Style:
    writeCity_LineEdit =  """QLineEdit {
            border: 2px solid rgba(255, 255, 255, 0.5);
            border-radius: 20px;
            padding: 8px 15px;
            background-color: rgba(255, 255, 255, 0.2);
            color: black;
            font-size: 16px;
        }
        QLineEdit:focus {
            border: 2px solid white;
            background-color: rgba(255, 255, 255, 0.3);
        }
        QLineEdit::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }
    """

    writeCity_LineEdit_second =  """
QLineEdit {
    border: 2px solid #9b59b6;
    border-radius: 8px;
    padding: 3px 8px;
    background-color: rgba(155, 89, 182, 0.1);
    color: black;
    font-size: 11px;
    font-weight: bold;
}
QLineEdit:focus {
    border: 2px solid #8e44ad;
    background-color: rgba(155, 89, 182, 0.2);
    color: white;
}
QLineEdit::placeholder {
    color: rgba(255, 255, 255, 0.6);
}
"""
    writeCity_LineEdit_dark = """QLineEdit {
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        padding: 8px 15px;
        background-color: rgba(0, 0, 0, 0.4);
        color: white;
        font-size: 16px;
    }
    QLineEdit:focus {
        border: 2px solid #7c4dff;
        background-color: rgba(0, 0, 0, 0.6);
    }
    QLineEdit::placeholder {
    color: #cccccc;
    }"""

class MessageStyle:
    base_style = """
        QMessageBox {
            background-color: rgba(30, 60, 110, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 15px;
        }
        QMessageBox QLabel {
            color: #ffffff;
            font-family: "Segoe UI", sans-serif;
            font-size: 15px;
            padding: 10px;
        }
        QPushButton {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                        stop:0 #4facfe, stop:1 #00f2fe);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 8px 20px;
            font-size: 13px;
            font-weight: bold;
            min-width: 80px;
            margin-right: 10px;
            margin-bottom: 10px;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                        stop:0 #5fcfff, stop:1 #20f5ff);
        }
        QPushButton:pressed {
            background-color: #3d84c6;
        }
    """

    warning = base_style + """
        QMessageBox QLabel { color: #ffeb3b; }
    """  # если пустое поле

    error = base_style + """
        QMessageBox QLabel { color: #ff8a80; }
    """ # город не найден и тд

    info = base_style + """
        QMessageBox QLabel { color: #80d8ff; }
    """

