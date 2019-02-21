# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\pyqt\09\findandreplacedlg.ui'
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

class Ui_FindAndReplaceDlg(object):
    def setupUi(self, FindAndReplaceDlg):
        FindAndReplaceDlg.setObjectName(_fromUtf8("FindAndReplaceDlg"))
        FindAndReplaceDlg.resize(355, 274)
        self.horizontalLayout = QtGui.QHBoxLayout(FindAndReplaceDlg)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(FindAndReplaceDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.findLineEdit = QtGui.QLineEdit(FindAndReplaceDlg)
        self.findLineEdit.setObjectName(_fromUtf8("findLineEdit"))
        self.gridLayout.addWidget(self.findLineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(FindAndReplaceDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.replaceLineEdit = QtGui.QLineEdit(FindAndReplaceDlg)
        self.replaceLineEdit.setObjectName(_fromUtf8("replaceLineEdit"))
        self.gridLayout.addWidget(self.replaceLineEdit, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.caseCheckBox = QtGui.QCheckBox(FindAndReplaceDlg)
        self.caseCheckBox.setObjectName(_fromUtf8("caseCheckBox"))
        self.verticalLayout.addWidget(self.caseCheckBox)
        self.wholeCheckBox = QtGui.QCheckBox(FindAndReplaceDlg)
        self.wholeCheckBox.setChecked(True)
        self.wholeCheckBox.setObjectName(_fromUtf8("wholeCheckBox"))
        self.verticalLayout.addWidget(self.wholeCheckBox)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(231, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.moreFrame = QtGui.QFrame(FindAndReplaceDlg)
        self.moreFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.moreFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.moreFrame.setObjectName(_fromUtf8("moreFrame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.moreFrame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.backwardsCheckBox = QtGui.QCheckBox(self.moreFrame)
        self.backwardsCheckBox.setObjectName(_fromUtf8("backwardsCheckBox"))
        self.verticalLayout_3.addWidget(self.backwardsCheckBox)
        self.regexCheckBox = QtGui.QCheckBox(self.moreFrame)
        self.regexCheckBox.setObjectName(_fromUtf8("regexCheckBox"))
        self.verticalLayout_3.addWidget(self.regexCheckBox)
        self.ignoreNotesCheckBox = QtGui.QCheckBox(self.moreFrame)
        self.ignoreNotesCheckBox.setObjectName(_fromUtf8("ignoreNotesCheckBox"))
        self.verticalLayout_3.addWidget(self.ignoreNotesCheckBox)
        self.verticalLayout_4.addWidget(self.moreFrame)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.line = QtGui.QFrame(FindAndReplaceDlg)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.findButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.verticalLayout_2.addWidget(self.findButton)
        self.replaceButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.replaceButton.setObjectName(_fromUtf8("replaceButton"))
        self.verticalLayout_2.addWidget(self.replaceButton)
        self.closeButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout_2.addWidget(self.closeButton)
        self.moreButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.moreButton.setCheckable(True)
        self.moreButton.setObjectName(_fromUtf8("moreButton"))
        self.verticalLayout_2.addWidget(self.moreButton)
        spacerItem1 = QtGui.QSpacerItem(21, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.label.setBuddy(self.findLineEdit)
        self.label_2.setBuddy(self.replaceLineEdit)

        self.retranslateUi(FindAndReplaceDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), FindAndReplaceDlg.reject)
        QtCore.QObject.connect(self.moreButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.moreFrame.setVisible)
        QtCore.QMetaObject.connectSlotsByName(FindAndReplaceDlg)

    def retranslateUi(self, FindAndReplaceDlg):
        FindAndReplaceDlg.setWindowTitle(_translate("FindAndReplaceDlg", "Find and Replace", None))
        self.label.setText(_translate("FindAndReplaceDlg", "Find &what:", None))
        self.label_2.setText(_translate("FindAndReplaceDlg", "Replace w&ith:", None))
        self.caseCheckBox.setText(_translate("FindAndReplaceDlg", "&Case sensitive", None))
        self.wholeCheckBox.setText(_translate("FindAndReplaceDlg", "Wh&ole words", None))
        self.backwardsCheckBox.setText(_translate("FindAndReplaceDlg", "Search &Backwards", None))
        self.regexCheckBox.setText(_translate("FindAndReplaceDlg", "Regular E&xpression", None))
        self.ignoreNotesCheckBox.setText(_translate("FindAndReplaceDlg", "Ignore foot&notes and endnotes", None))
        self.findButton.setText(_translate("FindAndReplaceDlg", "&Find", None))
        self.replaceButton.setText(_translate("FindAndReplaceDlg", "&Replace", None))
        self.closeButton.setText(_translate("FindAndReplaceDlg", "Close", None))
        self.moreButton.setText(_translate("FindAndReplaceDlg", "&More", None))

