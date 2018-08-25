import math
import random
import string
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):

    X_MAX = 26
    Y_MAX = 60

    def __init__(self, parent=None):
        super().__init__(parent)

        self.numbersFormatDlg = None
        self.format = dict(thousandsseparator=",", decimalmarker=".", decimalplaces=2, rednagetivates=False)
        self.numbers = {}
        for x in range(self.X_MAX):
            for y in range(self.Y_MAX):
                self.numbers[(x, y)] = (10000 * random.random()) - 5000

        self.table = QTableWidget()
        formatButton = QPushButton("Set Number Format...(&Model)")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(formatButton)
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        self.setWindowTitle("Numbers")

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()