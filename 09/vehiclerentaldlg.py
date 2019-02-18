import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_vehiclerentaldlg

class VehicleRentalDlg(QDialog, ui_vehiclerentaldlg.Ui_VehicleRentalDlg):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.vehicleComboBox.setFocus()

    @pyqtSignature("QString")
    def on_vehicleComboBox_currentIndexChanged(self, text):
        if text == "Car":
            self.mileageLabel.setText("1000 miles")
        else:
            self.on_weightSpinBox_valueChanged(self.weightSpinBox.value())

    @pyqtSignature("int")
    def on_weightSpinBox_valueChanged(self, amount):
        self.mileageLabel.setText("{} miles".format(8000 / amount))

app = QApplication(sys.argv)
form = VehicleRentalDlg()
form.show()
app.exec_()
