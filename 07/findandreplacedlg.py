import re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_findandreplacedlg

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_manubar
except ImportError:
    MAC = False

class FindAndReplaceDlg(QDialog, ui_findandreplacedlg.Ui_FindAndReplaceDlg):

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.__text = text
        self.__index = 0
        self.setupUi(self)
        if not MAC:
            self.findButton.setFocusPolicy(Qt.NoFocus)
            self.replaceButton.setFocusPolicy(Qt.NoFocus)
            self.replaceAllButton.setFocusPolicy(Qt.NoFocus)
            self.closeButton.setFocusPolicy(Qt.NoFocus)
        self.updateUi()

    @pyqtSignature("QString")
    def on_findLineEdit_textEdited(self):
        self.__index = 0
        self.updateUi()

    def makeRegex(self):
        findText = self.findLineEdit.text()
        if self.syntaxComboBox.currentText() == "Literal":
            findText = re.escape(findText)
        flags = re.MULTILINE | re.DOTALL | re.UNICODE
        if not self.caseCheckBox.isChecked():
            flags |= re.IGNORECASE
        if self.wholeCheckBox.isChecked():
            findText = r"\b{}\b".format(findText)
        return re.compile(findText, flags)

    @pyqtSignature("")
    def on_findButton_clicked(self):
        regex = self.makeRegex()
        match = regex.search(self.__text, self.__index)
        if match is not None:
            self.__index = match.end()
            self.emit(SIGNAL("found"), match.start())
        else:
            self.emit(SIGNAL("notfound"))

    def updateUi(self):
        enable = bool(self.findLineEdit.text())
        self.findButton.setEnabled(enable)
        self.replaceButton.setEnabled(enable)
        self.replaceAllButton.setEnabled(enable)

    def text(self):
        return self.__text

if __name__ == "__main__":

    import sys

    text = "Hello"

    app = QApplication(sys.argv)
    form = FindAndReplaceDlg(text)
    form.show()
    app.exec_()