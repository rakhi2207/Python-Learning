from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()

        ch1=QCheckBox("Do this")
        ch1.toggled.connect(lambda: self.something_written(ch1))
        ch2=QCheckBox("Learn Pyqt5")
        ch2.toggled.connect(lambda: self.something_written(ch2))

        self.label=QLabel("");
        self.content=[]
        layout.addWidget(ch1)
        layout.addWidget(ch2)
        layout.addWidget(self.label)
        widget = QWidget()
        widget.setLayout(layout)
        self.resize(1280,720)
        self.setCentralWidget(widget)

    def something_written(self,s):
        text_string = ""
        if(s.isChecked()):
            self.content.append(s.text())
            for value in self.content:
                text_string+=value+"\n"
            self.label.setText(text_string)
        else:
            self.content=list(filter(lambda value:(value!=s.text()) ,self.content))
        print(self.content)

app = QApplication([])
window = MyMainWindow()
window.show()
app.exec()
