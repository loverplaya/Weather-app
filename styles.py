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