from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyMainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MyMainWindow, self).__init__(*args,**kwargs)
        layout=QVBoxLayout()
        combo=QComboBox()
        combo.addItems(["easy","medium","hard"])
        btn=QPushButton("Start")
        btn.pressed.connect(lambda :self.show_value(combo))
        layout.addWidget(combo)
        layout.addWidget(btn)
        widget=QWidget()
        widget.setLayout(layout)
        self.setWindowTitle("Combo Boxes")
        self.resize(1280,720)
        self.setCentralWidget(widget)

    def show_value(self,s):
        print(s.currentText())

app=QApplication([])
window=MyMainWindow()
window.show()
app.exec()