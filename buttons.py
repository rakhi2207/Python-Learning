from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle = "Buttons"
        self.resize(1280, 720)
        layout = QVBoxLayout()

        btn1 = QPushButton("btn1")
        btn2 = QPushButton("btn2")

        self.label = QLabel("Hello everyOne")
        font=self.label.font()
        font.setPointSize(49)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        btn1.clicked.connect(self.click_btn1)
        btn2.clicked.connect(self.click_btn2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def click_btn1(self):
            self.label.setText("button 1 clicked")

    def click_btn2(self):
            self.label.setText("button 2 clicked")


app = QApplication([])
window = MyMainWindow()
window.show()
app.exec()
