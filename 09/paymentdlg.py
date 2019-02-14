import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_paymentdlg

class PaymentDlg(QDialog, ui_paymentdlg.Ui_PaymentDlg):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = PaymentDlg()
    form.show()
    app.exec_()