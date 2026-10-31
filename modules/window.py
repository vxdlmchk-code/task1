from PyQt6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox
from modules.app import app 

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

main_layout = QVBoxLayout()

button1 = QPushButton(text="Press")
button1.setFixedSize(100, 50)
button1.setStyleSheet("border: 2px solid green")

frame1 = QFrame()
frame1.setStyleSheet("background-color: rgb(150, 150, 150)") 
frame1.setFixedSize(600, 400)

layout2 = QHBoxLayout()

menu = QComboBox()
menu.addItems(["опція 1", "опція 2", "опція 3"])

line1 = QLineEdit()
line1.setPlaceholderText("Введіть текст")

layout2.addWidget(menu)
layout2.addWidget(line1)
frame1.setLayout(layout2)

main_layout.addWidget(button1)
main_layout.addWidget(frame1)

from PyQt6.QtWidgets import QWidget
central_widget = QWidget()
central_widget.setLayout(main_layout)
window.setCentralWidget(central_widget)

window.show()