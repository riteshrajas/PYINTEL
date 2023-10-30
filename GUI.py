
import pyautogui
import PyQt5.QtGui as QtGui
import time as Time
import importlib
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QProgressBar, QLayout, QPlainTextEdit, QWidget, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap
from API import process_user_input as processor
import sys
Screen_width, Screen_height = pyautogui.size()
print(Screen_width,Screen_height)

class Ui():
    def __init__(self):
        
        self.ProgressBar_Value = 0
        
        

        self.app = QApplication(sys.argv)
        self.app.setStyle('Fusion')
        self.app.setApplicationName('PYNTEL')
        self.app.setWindowIcon(QtGui.QIcon(r"P:\PYINTEL_3.0\Utility\Pyintel_data\Pyintel_media\Pyntel_icon.png"))
        
        self.MainWindow = QMainWindow()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setGeometry(0, 0, Screen_width, Screen_height)
        self.MainWindow.resize(Screen_width, Screen_height)
        self.MainWindow.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.MainWindow.setStyleSheet(u"background-color:#000;")
        self.MainWindow.setWindowTitle("Pyntel")
       
        self.Pyintel_title = QLabel(self.MainWindow)
        self.Pyintel_title.setText("PYNTEL")
        self.Pyintel_title.setStyleSheet(u"color: #FFF; text-align: center; font-family: Inter; font-size: 40px; font-style: italic; font-weight: 900; line-height: 182.023%; letter-spacing: 20px; text-transform: capitalize;")
        self.Pyintel_title.setGeometry(QRect(int(Screen_width/2) - 200, 50, 400, 100))
        self.Pyintel_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        
        self.Pyintel_Icon = QLabel(self.MainWindow)
        self.Pyintel_Icon.setPixmap(QPixmap(r"P:\PYINTEL_3.0\Utility\Pyintel_data\Pyintel_media\Pyntel_icon.png").scaled(200,200,transformMode=Qt.TransformationMode.SmoothTransformation))
        self.Pyintel_Icon.setGeometry(QRect(0,-50,200,150))
        self.Pyintel_Icon.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        self.Notification_led = QProgressBar(self.MainWindow)
        self.Notification_led.setGeometry(Screen_width- 280, 80, 200, 40)
        self.Notification_led.setMinimum(0)
        self.Notification_led.setMaximum(100)
        self.Notification_led.setValue(self.ProgressBar_Value)
        self.Notification_led.setStyleSheet(u"""
            QProgressBar { 
                border-radius: 20px; 
                text-align: center;		 
                background-color: rgb(255, 255, 255);
            } 
            QProgressBar::chunk { 
                background-color: #00ff00; 
                border-radius: 20px;
            }""")
    
    
        self.Central_Widget = QWidget(self.MainWindow)
        self.Central_Widget.setObjectName("Central_Widget")
        self.Central_Widget.setStyleSheet(u"""
            border-radius: 80px 80px 0px 0px;
            background: rgba(70, 70, 70, 0);
        """)
        self.Central_Widget.setGeometry(QRect(0, 200, self.MainWindow.width(), self.MainWindow.height() - 150))
        
        self.Toolbar = QWidget(self.Central_Widget)
        self.Toolbar.setGeometry(QRect(10, self.Central_Widget.height() - 100 -10, self.Central_Widget.width() - 20, 100))
        self.Toolbar.setStyleSheet(u"border-radius:50px;background-color: #000000; border: 2px solid ;border-color: #47d1ad;")
    
        self.Textbox = QPlainTextEdit(self.Toolbar)
        self.Textbox.setGeometry(QRect(30, self.Central_Widget.height() - 100 -10, self.Central_Widget.width() - 280,100))
        self.Textbox.setStyleSheet("""
            background: #f2f2f2;
            border: 5px solid #00ff00;
            border-radius: 50px;
            padding: 30px;
            font-size: 25px;
            font-family: Arial, sans-serif;
            color: #333;
        """)

        self.send_button = QPushButton(self.Toolbar)
        self.send_button.setText("")
        self.send_button.setGeometry(QRect(self.Textbox.width() + 100, 705, 110, 110))
        self.send_button.setStyleSheet(u"""
        QToolButton {
            padding: 10px;
            border: 80px;
            border-radius: 55px;
            background-color: #50f902;
            color: #ffffff;
            font-size: 25px;
            outline: none;
        }
        QToolButton:hover {
            background-color: #2f9404;
            color: #333333;
        }
    
        """)
        self.send_button.pressed.connect(self.SendPress)
        
        
        
        self.chat_view = QListWidget(self.Central_Widget)
        self.chat_view.setGeometry(QRect(6, 0, self.Central_Widget.width()-15, self.Central_Widget.height() - 250))
        self.chat_view.setStyleSheet(f"""
            border-radius: 80px 80px 0px 0px;
            background-color: rgba(70, 70, 70, 0.50);
            font-size: 20px;
            color: white;
        """)
        
        self.MainWindow.show() 
        


        required_package = [  
                "pyttsx4",
                "datetime",
                "json",
                "time",
                "urllib.request",
                "pandas",
                "re",
                "webbrowser",
                "wikipedia",
                "Utility.Aid.getJsonData",
                "Utility.Aid.InternetAnalaysis",
                "Utility.Aid.Server",
                "Utility.Aid.similarity",
                "Utility.Aid.Telegrammer",
                "Utility.Aid.Weather",
                "Utility.Aid.patternIdentifier",
                "Utility.Aid.Machine_Learning_Models",
                "Utility.Aid.Fitness",
                "Utility.Aid.Mailer",
                "Utility.Aid.transcriber"]
        for i in range(100):
            try:
                module = importlib.import_module(required_package[i])
                print("Imported",required_package[i])
                globals()[module.__name__] = module
            except:
                pass
            self.Notification_led.setValue(i+1)
            Time.sleep(0.01)
        self.Notification_led.setFormat("Ready!")
        
    def SendPress(self):
        user_input = self.Textbox.toPlainText()
        self.chat_view.addItem(QListWidgetItem(user_input))
        self.Textbox.clear()
        answer = processor(user_input)
        answer = "Hello"
        self.chat_view.addItem(QListWidgetItem(answer))
        


if __name__ == "__main__":
    AppUi = Ui()
    sys.exit(AppUi.app.exec())
    

