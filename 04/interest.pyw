import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        labelPrincipal = QLabel("Principal:")
        labelRate = QLabel("Rate:")
        labelYears = QLabel("Years:")
        labelAmount = QLabel("Amount")
        self.spinPrincipal = QDoubleSpinBox()
        self.spinPrincipal.setPrefix("$")
        self.spinPrincipal.setRange(0.01, 10000000.00)
        self.spinPrincipal.setValue(1000.00)
        self.spinRate = QDoubleSpinBox()
        self.spinRate.setSuffix("%")
        self.spinRate.setValue(5.00)
        self.comboYear = QComboBox()
        for year in range(1, 26):
            if year == 1:
                self.comboYear.addItem("1 year")
            else:
                self.comboYear.addItem("{} years".format(year))
        self.labelResult = QLabel("${0:.2f}".format(1000 * ((1 + (5 / 100.0)) ** 1)))

        grid = QGridLayout()
        grid.addWidget(labelPrincipal, 0, 0)
        grid.addWidget(self.spinPrincipal, 0, 1)
        grid.addWidget(labelRate, 1, 0)
        grid.addWidget(self.spinRate, 1, 1)
        grid.addWidget(labelYears, 2, 0)
        grid.addWidget(self.comboYear, 2, 1)
        grid.addWidget(labelAmount, 3, 0)
        grid.addWidget(self.labelResult, 3, 1)
        self.setLayout(grid)

        self.connect(self.spinPrincipal, SIGNAL("valueChanged(double)"), self.updateUi)
        self.connect(self.spinRate, SIGNAL("valueChanged(double)"), self.updateUi)
        self.connect(self.comboYear, SIGNAL("currentIndexChanged(int)"), self.updateUi)

        self.setWindowTitle("Interest")

    def updateUi(self):
        years = float(self.comboYear.currentText().split()[0])
        result = self.spinPrincipal.value() * ((1 + (self.spinRate.value() / 100.00)) ** years)
        self.labelResult.setText("${0:.2f}".format(result))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()