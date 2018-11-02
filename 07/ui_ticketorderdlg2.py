# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\pyqt\07\ticketorderdlg2.ui'
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

class Ui_TicketOrderDlg(object):
    def setupUi(self, TicketOrderDlg):
        TicketOrderDlg.setObjectName(_fromUtf8("TicketOrderDlg"))
        TicketOrderDlg.resize(397, 144)
        self.verticalLayout = QtGui.QVBoxLayout(TicketOrderDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(TicketOrderDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.customerLineEdit = QtGui.QLineEdit(TicketOrderDlg)
        self.customerLineEdit.setObjectName(_fromUtf8("customerLineEdit"))
        self.horizontalLayout.addWidget(self.customerLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(TicketOrderDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.whenDateTimeEdit = QtGui.QDateTimeEdit(TicketOrderDlg)
        self.whenDateTimeEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.whenDateTimeEdit.setObjectName(_fromUtf8("whenDateTimeEdit"))
        self.horizontalLayout_2.addWidget(self.whenDateTimeEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(TicketOrderDlg)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.priceSpinBox = QtGui.QDoubleSpinBox(TicketOrderDlg)
        self.priceSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.priceSpinBox.setMaximum(5000.0)
        self.priceSpinBox.setObjectName(_fromUtf8("priceSpinBox"))
        self.horizontalLayout_3.addWidget(self.priceSpinBox)
        self.label_4 = QtGui.QLabel(TicketOrderDlg)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.quantitySpinBox = QtGui.QSpinBox(TicketOrderDlg)
        self.quantitySpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.quantitySpinBox.setMinimum(1)
        self.quantitySpinBox.setMaximum(50)
        self.quantitySpinBox.setObjectName(_fromUtf8("quantitySpinBox"))
        self.horizontalLayout_3.addWidget(self.quantitySpinBox)
        self.label_5 = QtGui.QLabel(TicketOrderDlg)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.amountLineEdit = QtGui.QLineEdit(TicketOrderDlg)
        self.amountLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.amountLineEdit.setReadOnly(False)
        self.amountLineEdit.setObjectName(_fromUtf8("amountLineEdit"))
        self.horizontalLayout_3.addWidget(self.amountLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(TicketOrderDlg)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.customerLineEdit)
        self.label_2.setBuddy(self.whenDateTimeEdit)
        self.label_3.setBuddy(self.priceSpinBox)
        self.label_4.setBuddy(self.quantitySpinBox)
        self.label_5.setBuddy(self.amountLineEdit)

        self.retranslateUi(TicketOrderDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TicketOrderDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TicketOrderDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(TicketOrderDlg)

    def retranslateUi(self, TicketOrderDlg):
        TicketOrderDlg.setWindowTitle(_translate("TicketOrderDlg", "Ticket Order", None))
        self.label.setText(_translate("TicketOrderDlg", "&Customer:", None))
        self.label_2.setText(_translate("TicketOrderDlg", "&When:", None))
        self.whenDateTimeEdit.setDisplayFormat(_translate("TicketOrderDlg", "dd/MM/yyyy HH:mm:ss", None))
        self.label_3.setText(_translate("TicketOrderDlg", "&Price:", None))
        self.priceSpinBox.setPrefix(_translate("TicketOrderDlg", "$", None))
        self.label_4.setText(_translate("TicketOrderDlg", "&Quantity:", None))
        self.label_5.setText(_translate("TicketOrderDlg", "Amount:", None))

