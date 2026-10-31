from PyQt6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QPushButton,QComboBox,QTextEdit,QWidget
from modules.app import app 
import random
window = QMainWindow()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
width_screen = screen_size.width()
height_screen = screen_size.height()

window.setGeometry(
    (width_screen // 2) - (WINDOW_WIDTH // 2), 
    (height_screen // 2) - (WINDOW_HEIGHT // 2), 
    WINDOW_WIDTH, WINDOW_HEIGHT
)

def generate():
    length = int(menu1.currentText())
    choice = menu2.currentText()
    if choice == "only numbers":
        chars = "0123456789"
    elif choice == "only letters":
        chars = "abcdefghijklmnopqrstuvwxyz"
    else:
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for i in range(length):
        password += random.choice(chars)      
    text1.setText(password)

def clear():
    text1.clear()


main_layout = QHBoxLayout()
frame_layout = QHBoxLayout()
frame1 = QFrame()
frame1.setStyleSheet("background-color: purple") 

menu1 = QComboBox()
menu1.addItems(["6", "8", "12","16","24"])

menu2 = QComboBox()
menu2.addItems(["only numbers","both","only letters"])

button1 = QPushButton(text="generate", parent= frame1)
button1.setFixedSize(150, 60)
button1.setStyleSheet("border: 1px solid black")

button2 = QPushButton(text = "clear", parent = frame1)
button2.setFixedSize(150,60)
button2.setStyleSheet("border :1px solid black")

button1.clicked.connect(generate)
button2.clicked.connect(clear)

text1 = QTextEdit()
text1.setMaximumHeight(60)
text1.setMaximumWidth(200)
frame_layout.addWidget(menu1)
frame_layout.addWidget(menu2)
frame_layout.addWidget(button1)
frame_layout.addWidget(text1)
frame_layout.addWidget(button2)

main_layout.addWidget(frame1)

frame1.setLayout(frame_layout)
central_widget = QWidget()
central_widget.setLayout(main_layout)
window.setCentralWidget(central_widget)

window.show()