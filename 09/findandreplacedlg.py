import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_findandreplacedlg

class FindAndReplaceDlg(QDialog, ui_findandreplacedlg.Ui_FindAndReplaceDlg):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.moreFrame.hide()
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = FindAndReplaceDlg()
    form.show()
    app.exec_()