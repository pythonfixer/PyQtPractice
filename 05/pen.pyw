import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PenPropertiesDlg(QDialog):

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

class Form(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.width = 1
        self.beveled = False
        self.style = "Solid"

        penButton = QPushButton("Set Pen...(Dumb &class")
        self.label = QLabel("The Pen has not been set")
        self.label.setTextFormat(Qt.RichText)

        layout = QVBoxLayout()
        layout.addWidget(penButton)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.connect(penButton, SIGNAL("clicked()"), self.setPenProperties)

        self.setWindowTitle("Pen")
        self.updateData()

    def setPenProperties(self):
        dialog = PenPropertiesDlg(self)
        dialog.widthSpinBox.setValue(self.width)
        dialog.beveledCheckBox.setChecked(self.beveled)
        dialog.styleComboBox.setCurrentIndex(dialog.styleComboBox.findText(self.style))
        if dialog.exec_():
            self.width = dialog.widthSpinBox.value()
            self.beveled = dialog.beveledCheckBox.isChecked()
            self.style = dialog.styleComboBox.currentText()
            self.updateData()

    def updateData(self):
        bevel = ""
        if self.beveled:
            bevel = "<br>Beveled"
        self.label.setText("Width={}<br>Style={}{}".format(self.width, self.style, bevel))

app = QApplication(sys.argv)
form = Form()
form.resize(200, 200)
form.show()
app.exec()