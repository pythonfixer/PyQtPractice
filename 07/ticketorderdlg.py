import re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_ticketorderdlg2

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class TicketOrderDlg(QDialog, ui_ticketorderdlg2.Ui_TicketOrderDlg):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        now = QDateTime.currentDateTime()
        rangeStart = now.addDays(1)
        rangeEnd = now.addYears(1)
        self.whenDateTimeEdit.setCalendarPopup(True)
        self.whenDateTimeEdit.setDateTimeRange(rangeStart, rangeEnd)

        if not MAC:
            self.buttonBox.setFocusPolicy(Qt.NoFocus)
        self.updateUi()

    @pyqtSignature("QString")
    def on_customerLineEdit_textEdited(self, text):
        self.updateUi()

    @pyqtSignature("double")
    def on_priceSpinBox_valueChanged(self):
        amount = self.priceSpinBox.value() * self.quantitySpinBox.value()
        self.amountLineEdit.setText("{}".format(amount))

    @pyqtSignature("int")
    def on_quantitySpinBox_valueChanged(self):
        amount = self.priceSpinBox.value() * self.quantitySpinBox.value()
        self.amountLineEdit.setText("{}".format(amount))

    def updateUi(self):
        enable = bool(self.customerLineEdit.text() and (self.quantitySpinBox.value() >= 1))
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)

    def result(self):
        customer = self.customerLineEdit.text()
        datetime = self.whenDateTimeEdit.text()
        price = self.priceSpinBox.value()
        quantity = self.quantitySpinBox.value()
        result = dict(Customer=customer, DateTime=datetime, Price=price, Quantity=quantity)
        return result

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = TicketOrderDlg()
    form.show()
    app.exec_()
    result = form.result()
    print("Customer:{}\tDateTime:{}\nPrice:{}\tQuantity:{}".format(result["Customer"], result["DateTime"], result["Price"], result["Quantity"]))
