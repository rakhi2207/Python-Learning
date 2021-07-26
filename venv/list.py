from QtWidgets import*
from QtGui import*
from QtCore import*

class MyMainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MyMainWindow, self).__init__(*args,**kwargs)
        layout=QVBoxLayout()
        widget=Widget()
        widget.setLayout(layout)
        self.resize(1280,720)
        self.setCentralWidget(widget)

app=QApplication([])
window=MyMainWindow();
window.show()
app.exec()