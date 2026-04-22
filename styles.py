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