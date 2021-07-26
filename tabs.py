from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyMainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MyMainWindow, self).__init__(*args,**kwargs)
        layout=QVBoxLayout()
        tabs=QTabWidget()
        tabs.addTab(QLabel("This is Tab1"),"Tab 1")
        tabs.addTab(QLabel("This is Tab2"), "Tab 2")
        tabs.addTab(QLabel("This is Tab3"), "Tab 3")
        tabs.setMovable(True)
        layout.addWidget(tabs)
        widget=QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.resize(1280,720)


app=QApplication([])
window=MyMainWindow()
window.show()
app.exec()