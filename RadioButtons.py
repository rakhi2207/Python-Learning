from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyMainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MyMainWindow, self).__init__(*args,**kwargs)
        layout = QVBoxLayout()
        male=QRadioButton("Male")
        male.toggled.connect(lambda :self.value_rb(male))
        female=QRadioButton("Female")
        female.toggled.connect(lambda: self.value_rb(female))
        self.label=QLabel("Nothing is selected")
        layout.addWidget(male)
        layout.addWidget(female)
        layout.addWidget(self.label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setWindowTitle("Radio Buttons")
        self.resize(1280,720)

    def value_rb(self,s):
        print(self.label.setText(s.text()))

app = QApplication([])
window = MyMainWindow()
window.show()
app.exec()
