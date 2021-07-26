from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyDialog(QDialog):
    def __init__(self,*args,**kwargs):
        super(MyDialog, self).__init__(*args,**kwargs)
        self.setWindowTitle("Another Dialogue box")
        label=QLabel("Another Dialogue box")
        self.layout=QVBoxLayout()
        self.layout.addWidget(label)
        self.setLayout(self.layout)
        self.resize(320,200)

class MyMainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MyMainWindow, self).__init__(*args,**kwargs)
        self.setWindowTitle("Dialogue Box")
        layout=QVBoxLayout()
        btn=QPushButton("Press ")
        layout.addWidget(btn)
        btn.pressed.connect(lambda :MyDialog().exec())
        widget=QWidget()
        widget.setLayout(layout)
        self.resize(1280,720)
        self.setCentralWidget(widget)

app=QApplication([])
window=MyMainWindow()
window.show()
app.exec()