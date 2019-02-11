# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\pyqt\08\ans\addeditmoviedlg_ans.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AddEditMovieDlg(object):
    def setupUi(self, AddEditMovieDlg):
        AddEditMovieDlg.setObjectName(_fromUtf8("AddEditMovieDlg"))
        AddEditMovieDlg.resize(450, 360)
        self.verticalLayout_2 = QtGui.QVBoxLayout(AddEditMovieDlg)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(AddEditMovieDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.titleLineEdit = QtGui.QLineEdit(AddEditMovieDlg)
        self.titleLineEdit.setObjectName(_fromUtf8("titleLineEdit"))
        self.gridLayout.addWidget(self.titleLineEdit, 0, 1, 1, 5)
        self.label_2 = QtGui.QLabel(AddEditMovieDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.yearSpinBox = QtGui.QSpinBox(AddEditMovieDlg)
        self.yearSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.yearSpinBox.setMinimum(1890)
        self.yearSpinBox.setMaximum(2100)
        self.yearSpinBox.setProperty("value", 1890)
        self.yearSpinBox.setObjectName(_fromUtf8("yearSpinBox"))
        self.gridLayout.addWidget(self.yearSpinBox, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(AddEditMovieDlg)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.acquiredDateEdit = QtGui.QDateEdit(AddEditMovieDlg)
        self.acquiredDateEdit.setAlignment(QtCore.Qt.AlignRight)
        self.acquiredDateEdit.setObjectName(_fromUtf8("acquiredDateEdit"))
        self.gridLayout.addWidget(self.acquiredDateEdit, 1, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(48, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 5, 1, 1)
        self.label_3 = QtGui.QLabel(AddEditMovieDlg)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.minutesSpinBox = QtGui.QSpinBox(AddEditMovieDlg)
        self.minutesSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.minutesSpinBox.setMaximum(720)
        self.minutesSpinBox.setObjectName(_fromUtf8("minutesSpinBox"))
        self.gridLayout.addWidget(self.minutesSpinBox, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(AddEditMovieDlg)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)
        self.locationLineEdit = QtGui.QLineEdit(AddEditMovieDlg)
        self.locationLineEdit.setObjectName(_fromUtf8("locationLineEdit"))
        self.gridLayout.addWidget(self.locationLineEdit, 2, 4, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(AddEditMovieDlg)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.notesTextEdit = QtGui.QTextEdit(AddEditMovieDlg)
        self.notesTextEdit.setTabChangesFocus(True)
        self.notesTextEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.notesTextEdit.setAcceptRichText(False)
        self.notesTextEdit.setObjectName(_fromUtf8("notesTextEdit"))
        self.verticalLayout.addWidget(self.notesTextEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(AddEditMovieDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.label.setBuddy(self.titleLineEdit)
        self.label_2.setBuddy(self.yearSpinBox)
        self.label_4.setBuddy(self.acquiredDateEdit)
        self.label_3.setBuddy(self.minutesSpinBox)
        self.label_6.setBuddy(self.locationLineEdit)
        self.label_5.setBuddy(self.notesTextEdit)

        self.retranslateUi(AddEditMovieDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddEditMovieDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddEditMovieDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(AddEditMovieDlg)
        AddEditMovieDlg.setTabOrder(self.titleLineEdit, self.yearSpinBox)
        AddEditMovieDlg.setTabOrder(self.yearSpinBox, self.acquiredDateEdit)
        AddEditMovieDlg.setTabOrder(self.acquiredDateEdit, self.minutesSpinBox)
        AddEditMovieDlg.setTabOrder(self.minutesSpinBox, self.locationLineEdit)
        AddEditMovieDlg.setTabOrder(self.locationLineEdit, self.notesTextEdit)

    def retranslateUi(self, AddEditMovieDlg):
        AddEditMovieDlg.setWindowTitle(_translate("AddEditMovieDlg", "My Movies - Add Movie", None))
        self.label.setText(_translate("AddEditMovieDlg", "&Title:", None))
        self.label_2.setText(_translate("AddEditMovieDlg", "&Year:", None))
        self.yearSpinBox.setSpecialValueText(_translate("AddEditMovieDlg", "Unknown", None))
        self.label_4.setText(_translate("AddEditMovieDlg", "A&cquired:", None))
        self.acquiredDateEdit.setDisplayFormat(_translate("AddEditMovieDlg", "ddd MMM d, yyyy", None))
        self.label_3.setText(_translate("AddEditMovieDlg", "&Minutes:", None))
        self.minutesSpinBox.setSpecialValueText(_translate("AddEditMovieDlg", "Unknown", None))
        self.label_6.setText(_translate("AddEditMovieDlg", "&Location:", None))
        self.label_5.setText(_translate("AddEditMovieDlg", "&Notes:", None))

