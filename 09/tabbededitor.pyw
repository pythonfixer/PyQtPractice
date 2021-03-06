import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import textedit
import qrc_resources

__version__ = "1.0.0"

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        #self.mdi = QMdiArea()
        self.tabWidget = QTabWidget()
        #self.setCentralWidget(self.mdi)
        self.setCentralWidget(self.tabWidget)

        fileNewAction = self.createAction("&New", self.fileNew, QKeySequence.New, "filenew", "Create a text file")
        fileOpenAction = self.createAction("&Open...", self.fileOpen, QKeySequence.Open, "fileopen", "Open an existing text file")
        fileSaveAction = self.createAction("&Save", self.fileSave, QKeySequence.Save, "filesave", "Save the text")
        fileSaveAsAction = self.createAction("Save &As...", self.fileSaveAs, icon="filesaveas", tip="Save the text using a new filename")
        fileSaveAllAction = self.createAction("Save A&ll", self.fileSaveAll, "filesave", tip="Save all the files")
        fileCloseTabAction = self.createAction("&Close Tab", self.fileCloseTab, "Ctrl+F4", "filequit", "Close the active tab")
        fileQuitAction = self.createAction("&Quit", self.close, "Ctrl+Q", "filequit", "Close the application")
        editCopyAction = self.createAction("&Copy", self.editCopy, QKeySequence.Copy, "editcopy", "Copy text to the clipboard")
        editCutAction = self.createAction("Cu&t", self.editCut, QKeySequence.Cut, "editcut", "Cut text to the clipboard")
        editPasteAction = self.createAction("&Paste", self.editPaste, QKeySequence.Paste, "editpaste", "Paste in the clipboard's text")
        '''self.windowNextAction = self.createAction("&Next", self.mdi.activateNextSubWindow, QKeySequence.NextChild)
        self.windowPrevAction = self.createAction("&Previous", self.mdi.activatePreviousSubWindow, QKeySequence.PreviousChild)
        self.windowCascadeAction = self.createAction("Casca&de", self.mdi.cascadeSubWindows)
        self.windowTileAction = self.createAction("&Tile", self.mdi.tileSubWindows)
        self.windowRestoreAction = self.createAction("&Restore All", self.windowRestoreAll)
        self.windowMinimizeAction = self.createAction("&Iconize All", self.windowMinimizeAll)
        self.windowArrangeIconsAction = self.createAction("&Arrange Icons", self.windowMinimizeAll)
        self.windowCloseAction = self.createAction("&Close", self.mdi.closeActiveSubWindow, QKeySequence.Close)'''

        self.windowMapper = QSignalMapper(self)
        #self.connect(self.windowMapper, SIGNAL("mapped(QWidget*)"), self.mdi, SLOT("setActiveWindow(QWidget*)"))
        self.connect(self.windowMapper, SIGNAL("mapped(QWidget*)"), self.tabWidget, SLOT("setActiveWindow(QWidget*)"))

        fileMenu = self.menuBar().addMenu("&File")
        self.addActions(fileMenu, (fileNewAction, fileOpenAction, fileSaveAction, fileSaveAsAction, fileSaveAllAction, None, fileCloseTabAction, fileQuitAction))
        editMenu = self.menuBar().addMenu("&Edit")
        self.addActions(editMenu, (editCopyAction, editCutAction, editPasteAction))
        #self.windowMenu = self.menuBar().addMenu("&Window")
        #self.connect(self.windowMenu, SIGNAL("aboutToShow()"), self.updateWindowMenu)

        fileToolbar = self.addToolBar("File")
        fileToolbar.setObjectName("FileToolbar")
        self.addActions(fileToolbar, (fileNewAction, fileOpenAction, fileSaveAction))
        editToolbar = self.addToolBar("Edit")
        editToolbar.setObjectName("EditToolbar")
        self.addActions(editToolbar, (editCopyAction, editCutAction, editPasteAction))

        settings = QSettings()
        self.restoreGeometry(settings.value("MainWindow/Geometry", QByteArray()))
        self.restoreState(settings.value("MainWindow/State", QByteArray()))

        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.showMessage("Ready", 5000)

        #self.updateWindowMenu()
        self.setWindowTitle("Text Editor")
        QTimer.singleShot(0, self.loadFiles)

    def createAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/{}.png".format(icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def fileCloseTab(self):
        failure = ""
        textEdit = self.tabWidget.currentWidget()
        if textEdit:
            if textEdit.isModified():
                try:
                    textEdit.save()
                except IOError as e:
                    failure = e
            if (failure and QMessageBox.warning(self, "Text Editor -- Save Error", "Failed to save{}\nQuit anyway?".format("\n\t".join(failure)), QMessageBox.Yes|QMessageBox.No) == QMessageBox.No):
                event.ignore()
                return
            textEdit.close()
            del textEdit

    '''def closeEvent(self, event):
        failures = []
        for textEdit in self.mdi.subWindowList():
            if textEdit.isModified():
                try:
                    textEdit.save()
                except IOError as e:
                    failures.append(e)
        if (failures and QMessageBox.warning(self, "Text Editor -- Save Error", "Failed to save{}\nQuit anyway?".format("\n\t".join(failures)), QMessageBox.Yes|QMessageBox.No) == QMessageBox.No):
            event.ignore()
            return
        settings = QSettings()
        settings.setValue("MainWindow/Geometry", self.saveGeometry())
        settings.setValue("MainWindow/State", self.saveState())
        files = []
        for textEdit in self.mdi.subWindowList():
            if not textEdit.filename.startswith("Unnamed"):
                files.append(textEdit.filename)
        settings.setValue("CurrentFiles", files)
        self.mdi.closeAllSubWindows()'''

    def closeEvent(self, event):
        failures = []
        for num in range(0, self.tabWidget.count()):
            textEdit = self.tabWidget.widget(num)
            if textEdit.isModified():
                try:
                    textEdit.save()
                except IOError as e:
                    failures.append(e)
        if (failures and QMessageBox.warning(self, "Text Editor -- Save Error", "Failed to save{}\nQuit anyway?".format("\n\t".join(failures)), QMessageBox.Yes|QMessageBox.No) == QMessageBox.No):
            event.ignore()
            return
        settings = QSettings()
        settings.setValue("MainWindow/Geometry", self.saveGeometry())
        settings.setValue("MainWindow/State", self.saveState())
        files = []
        for num in range(0, self.tabWidget.count()):
            textEdit = self.tabWidget.widget(num)
            if not textEdit.filename.startswith("Unnamed"):
                files.append(textEdit.filename)
        settings.setValue("CurrentFiles", files)
        self.tabWidget.close()

    def loadFiles(self):
        if len(sys.argv) > 1:
            #for filename in sys.argv[1:31]:
            for filename in sys.argv[1:11]:
                if QFileInfo(filename).isFile():
                    self.loadFile(filename)
                    QApplication.processEvents()
        else:
            settings = QSettings()
            files = settings.value("CurrentFiles") or []
            for filename in files:
                if QFile.exists(filename):
                    self.loadFile(filename)
                    QApplication.processEvents()

    '''def fileNew(self):
        textEdit = textedit.TextEdit()
        self.mdi.addSubWindow(textEdit)
        textEdit.show()'''

    def fileNew(self):
        textEdit = textedit.TextEdit()
        self.tabWidget.addTab(textEdit, textEdit.filename)
        self.tabWidget.setCurrentWidget(textEdit)

    '''def fileOpen(self):
        filename = QFileDialog.getOpenFileName(self, "Text Editor -- Open File")
        if filename:
            for textEdit in self.mdi.subWindowList():
                if textEdit.filename == filename:
                    self.mdi.setActiveWindow(textEdit)
                    break
            else:
                self.loadFile(filename)'''

    def fileOpen(self):
        filename = QFileDialog.getOpenFileName(self, "Text Editor -- Open File")
        if filename:
            for num in range(0, self.tabWidget.count()):
                textEdit = self.tabWidget.widget(num)
                if textEdit.filename == filename:
                    self.tabWidget.currentWidget()
                    break
            else:
                self.loadFile(filename)


    def loadFile(self, filename):
        textEdit = textedit.TextEdit(filename)
        try:
            textEdit.load()
        except EnvironmentError as e:
            QMessageBox.warning(self, "Text Editor -- Load Error", "Failed to load {}: {}".format(filename, e))
            textEdit.close()
            del textEdit
        else:
            #self.mdi.addWindow(textEdit)
            self.tabWidget.addTab(textEdit, textEdit.filename)
            textEdit.show()

    def fileSave(self):
        #textEdit = self.mdi.activeWindow()
        textEdit = self.tabWidget.currentWidget()
        if textEdit is None or not isinstance(textEdit, QTextEdit):
            return True
        try:
            textEdit.save()
            return True
        except EnvironmentError as e:
            QMessageBox.warning(self, "Text Editor -- Save Error", "Failed to save {}: {}".format(textEdit.filename, e))
            return False

    def fileSaveAs(self):
        #textEdit = self.mdi.activeWindow()
        textEdit = self.tabWidget.currentWidget()
        if textEdit is None or not isinstance(textEdit, QTextEdit):
            return
        filename = QFileDialog.getSaveFileName(self, "Text Editor -- Save File As", textEdit.filename, "Text files (*.txt *.*)")
        if filename:
            textEdit.filename = filename
            return self.fileSave()
        return True

    def fileSaveAll(self):
        errors = []
        #for textEdit in self.mdi.subWindowList():
        for num in range(0, self.tabWidget.count()):
            testEdit = self.tabWidget.widget(num)
            if textEdit.isModified():
                try:
                    textEdit.save()
                except EnvironmentError as e:
                    errors.append("{}: {}".format(textEdit.filename, e))
        if errors:
            QMessageBox.warning(self, "Text Editor -- Save All Error", "Failed to save\n{}".format("\n".join(errors)))

    def editCopy(self):
        textEdit = self.mdi.activeWindow()
        if textEdit is None or not isinstance(textEdit, QTextEdit):
            return
        cursor = textEdit.textCursor()
        text = cursor.selectedText()
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)

    def editCut(self):
        textEdit = self.mdi.activeWindow()
        if textEdit is None or not isinstance(textEdit, QTextEdit):
            return
        cursor = textEdit.textCursor()
        text = cursor.selectedText()
        if text:
            cursor.removeSelectedText()
            clipboard = QApplication.clipboard()
            clipboard.setText(text)

    def editPaste(self):
        textEdit = self.mdi.activeWindow()
        if textEdit is None or not isinstance(textEdit, QTextEdit):
            return
        clipboard = QApplication.clipboard()
        textEdit.insertPlainText(clipboard.text())

    '''def windowRestoreAll(self):
        for textEdit in self.mdi.subWindowList():
            textEdit.showNormal()

    def windowMinimizeAll(self):
        for textEdit in self.mdi.subWindowList():
            textEdit.showMinimized()

    def updateWindowMenu(self):
        self.windowMenu.clear()
        self.addActions(self.windowMenu, (self.windowNextAction, self.windowPrevAction, self.windowCascadeAction,
                                          self.windowTileAction, self.windowRestoreAction, self.windowMinimizeAction,
                                          self.windowArrangeIconsAction, None, self.windowCloseAction))
        textEdits = self.mdi.subWindowList()
        if not textEdits:
            return
        self.windowMenu.addSeparator()
        i = 1
        menu = self.windowMenu
        for textEdit in textEdits:
            title = textEdit.windowTitle()
            if i == 10:
                self.windowMenu.addSeparator()
                menu = menu.addMenu("&More")
            accel = ""
            if i < 10:
                accel = "&{} ".format(i)
            elif i < 36:
                accel = "&{} ".format(chr(i + ord("@") - 9))
            action = menu.addAction("{}{}".format(accel, title))
            self.connect(action, SIGNAL("triggered()"), self.windowMapper, SLOT("map()"))
            self.windowMapper.setMapping(action, textEdit)
            i += 1'''

app = QApplication(sys.argv)
app.setWindowIcon(QIcon(":/icon.png"))
app.setOrganizationName("Qtrac Ltd.")
app.setOrganizationDomain("qtrac.eu")
app.setApplicationName("Text Editor")
form = MainWindow()
form.show()
app.exec_()
