import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        self.connect(dial, SIGNAL("valueChanged(int)"), spinbox.setValue)
        self.connect(spinbox, SIGNAL("valueChanged(int)"), dial.setValue)
        self.setWindowTitle("Signals and Slots")

class Form2(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        self.connect(dial, SIGNAL("valueChanged(int)"), spinbox, SLOT("setValue(int)"))
        self.connect(spinbox, SIGNAL("valueChanged(int)"), dial, SLOT("setValue(int)"))
        self.setWindowTitle("Signals and Slots")

app = QApplication(sys.argv)
form = None
if len(sys.argv) == 1 or sys.argv[1] == "1":
    form = Form()
elif sys.argv[1] == "2":
    form = Form2()
if form is not None:
    form.show()
    app.exec_()