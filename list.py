from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyMainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MyMainWindow, self).__init__(*args,**kwargs)
        layout=QVBoxLayout()
        list=QListWidget()
        list.addItems(["easy","hard","medium"])
        layout.addWidget(list)
        list.currentItemChanged.connect(lambda x:print(x.text()));
        widget=QWidget()
        widget.setLayout(layout)
        self.setWindowTitle("list")
        self.resize(1280,720)
        self.setCentralWidget(widget)

app=QApplication([])
window=MyMainWindow();
window.show()
app.exec()