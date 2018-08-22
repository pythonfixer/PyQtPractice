import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PenProperties(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        widthlabel = QLabel("&Wdith")
        self.widthSpinBox = QSpinBox()
        widthlabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.widthSpinBox.setRange(0, 24)
        self.beveledCheckBox = QCheckBox("&Beveled edges")
        stylelabel = QLabel("&Style")
        self.styleComboBox = QComboBox()
        stylelabel.setBuddy(self.styleComboBox)
        self.styleComboBox.addItems(["Solid", "Dashed", "Dotted", "DashDotted", "DashDotDotted"])
        okButton = QPushButton("&OK")
        cancelButton = QPushButton("Cancel")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QGridLayout()
        layout.addWidget(widthlabel, 0, 0)
        layout.addWidget(self.widthSpinBox, 0, 1)
        layout.addWidget(self.beveledCheckBox, 0, 2)
        layout.addWidget(stylelabel, 1, 0)
        layout.addWidget(self.styleComboBox, 1, 1, 1, 2)
        layout.addLayout(buttonLayout, 2, 0, 1, 3)
        self.setLayout(layout)

        self.connect(okButton, SIGNAL("clicked()"), SLOT("accept()"))
        self.connect(cancelButton, SIGNAL("clicked()"), SLOT("reject()"))
        self.setWindowTitle("Pen Properties")

app = QApplication(sys.argv)
form = PenProperties()
form.show()
app.exec()