import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import qrc_resources

class ResizeDlg(QDialog):

    def __init__(self, width, height, parent=None):
        super().__init__(parent)

        widthLabel = QLabel("&Width:")
        self.widthSpinBox = QSpinBox()
        widthLabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignRight)
        self.widthSpinBox.setRange(4, width * 4)
        self.widthSpinBox.setValue(width)
        heightLabel = QLabel("&Height:")
        self.heightSpinBox = QSpinBox()
        heightLabel.setBuddy(self.heightSpinBox)
        self.heightSpinBox.setAlignment(Qt.AlignRight)
        self.heightSpinBox.setRange(4, height * 4)
        self.heightSpinBox.setValue(height)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.size = (width, height)

        grid = QGridLayout()
        grid.addWidget(widthLabel, 0, 0)
        grid.addWidget(self.widthSpinBox, 0, 1)
        grid.addWidget(heightLabel, 1, 0)
        grid.addWidget(self.heightSpinBox, 1, 1)
        grid.addWidget(buttonBox, 2, 0, 1, 2)
        self.setLayout(grid)

        self.connect(buttonBox, SIGNAL("accepted()"), self, SLOT("accept()"))
        self.connect(buttonBox, SIGNAL("rejected()"), self, SLOT("reject()"))

        self.setWindowIcon(QIcon(":/icon.png"))
        self.setWindowTitle("Image Changer - Resize")

    def accept(self):
        self.size = (self.widthSpinBox.value(), self.heightSpinBox.value())
        QDialog.accept(self)

    def result(self):
        return  self.size