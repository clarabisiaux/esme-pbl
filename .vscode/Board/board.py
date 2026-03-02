from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QRadioButton, QButtonGroup, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MorpionView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster - Welcome !")
        self.setFixedSize(400, 300)
        self.setMinimumSize(400, 300)
        self.setStyleSheet("background-color: lightblue; font-size: 20px")
        