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

class ZeroSpinBox(QSpinBox):

    zeros = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.connect(self, SIGNAL("valueChanged(int)"), self.checkzero)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.emit(SIGNAL("atzero"), self.zeros)

class Form3(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)
        zerospinbox = ZeroSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(zerospinbox)
        self.setLayout(layout)

        self.connect(dial, SIGNAL("valueChanged(int)"), zerospinbox, SLOT("setValue(int)"))
        self.connect(zerospinbox, SIGNAL("valueChanged(int)"), dial, SLOT("setValue(int)"))
        self.connect(zerospinbox, SIGNAL("atzero"), self.announce)
        self.setWindowTitle("Signals and Slots")

    def announce(self, zeros):
        print("ZeroSpinBox has been at zero {} times".format(zeros))

app = QApplication(sys.argv)
form = None
if len(sys.argv) == 1 or sys.argv[1] == '1':
    form = Form()
elif sys.argv[1] == '2':
    form = Form2()
elif sys.argv[1] == '3':
    form = Form3()
if form is not None:
    form.show()
    app.exec_()