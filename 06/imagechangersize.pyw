import os
import platform
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import helpform
import newimagedlg
import resizeDlg
import qrc_resourcessize

__version__ = "1.0.0"

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.mirroredvertically = False
        self.mirroredhorizontally = False

        self.imageLabel = QLabel()
        self.imageLabel.setMinimumSize(200, 200)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setCentralWidget(self.imageLabel)

        logDockWidget = QDockWidget("Log", self)
        logDockWidget.setObjectName("LogDockWidget")
        logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.listWidget = QListWidget()
        logDockWidget.setWidget(self.listWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, logDockWidget)

        self.printer = None

        self.sizeLabel = QLabel()
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Ready", 5000)

        fileNewAction = self.createAction("&New", self.fileNew, QKeySequence.New, "filenew", "Create an image file")
        fileOpenAction = self.createAction("&Open", self.fileOpen, QKeySequence.Open, "fileopen", "Open an image file")
        fileSaveAction = self.createAction("&Save", self.fileSave, QKeySequence.Save, "filesave", "Save the exists image file")
        fileSaveAsAction = self.createAction("Save &As", self.fileSaveAs, QKeySequence.SaveAs, "filesaveas", "Save the image file as another name")
        filePrintAction = self.createAction("&Print", self.filePrint, QKeySequence.Print, "fileprint", "Print the image file")
        fileQuitAction = self.createAction("&Quit", self.close, "Ctrl+Q", "filequit", "Quit the application")
        editInvertAction = self.createAction("&Invert", self.editInvert, "Ctrl+I", "editinvert", "Invert the color of the image", True, "toggled(bool)")
        editSwapRedAndBlueAction = self.createAction("Swap &Red And Blue", self.editSwapRedAndBlue, "Ctrl+R", "editswap", "Swap the red and blue color of the image", True, "toggled(bool)")
        editZoomAction = self.createAction("&Zoom", self.editZoom, "Ctrl+Z", "editzoom", "Zoom the image")
        editResizeAction = self.createAction("&Resize", self.editResize, "Ctrl+R", "editresize", "Resize the image")
        editMirrorGroup = QActionGroup(self)
        editUnMirrorAction = self.createAction("&UnMirror", self.editUnMirror, "Ctrl+U", "editunmirror", "Unmirrored the image", True, "toggled(bool)")
        editMirrorGroup.addAction(editUnMirrorAction)
        editMirrorHorizAction = self.createAction("Mirrored &Horizontally", self.editMirrorHorizontal, "Ctrl+H", "editmirrorhoriz", "Mirrored horizontally the image", True, "toggled(bool)")
        editMirrorGroup.addAction(editMirrorHorizAction)
        editMirrorVertiAction = self.createAction("Mirrored &Vertically", self.editMirrorVertical, "Alt+V", "editmirrorvert", "Mirrored vertically the image", True, "toggled(bool)")
        editMirrorGroup.addAction(editMirrorVertiAction)
        editUnMirrorAction.setChecked(True)
        helpAboutAction = self.createAction("&About", self.helpAbout)
        helpHelpAction = self.createAction("&Help", self.helpHelp, QKeySequence.HelpContents)

        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenuActions = (fileNewAction, fileOpenAction, fileSaveAction, fileSaveAsAction, None, filePrintAction, fileQuitAction)
        self.connect(self.fileMenu, SIGNAL("aboutToShow()"), self.updateFileMenu)

        editMenu = self.menuBar().addMenu("&Edit")
        self.addActions(editMenu, (editInvertAction, editSwapRedAndBlueAction, editZoomAction, editResizeAction))
        editMirrorMenu = editMenu.addMenu(QIcon(":/editmirror.png"), "&Mirrored")
        self.addActions(editMirrorMenu, (editUnMirrorAction, editMirrorHorizAction, editMirrorVertiAction))
        helpMenu = self.menuBar().addMenu("&Help")
        self.addActions(helpMenu, (helpAboutAction, helpHelpAction))

        fileToolbar = self.addToolBar("File")
        fileToolbar.setObjectName("FileToolBar")
        self.addActions(fileToolbar, (fileNewAction, fileOpenAction, fileSaveAsAction))
        editToolbar = self.addToolBar("Edit")
        editToolbar.setObjectName("EditToolBar")
        self.addActions(editToolbar, (editInvertAction, editSwapRedAndBlueAction, editUnMirrorAction, editMirrorHorizAction, editMirrorVertiAction))

        self.zoomSpinBox = QSpinBox()
        self.zoomSpinBox.setRange(1, 400)
        self.zoomSpinBox.setSuffix(" %")
        self.zoomSpinBox.setValue(100)
        self.zoomSpinBox.setToolTip("Zoom the image")
        self.zoomSpinBox.setStatusTip(self.zoomSpinBox.toolTip())
        self.zoomSpinBox.setFocusPolicy(Qt.NoFocus)
        self.connect(self.zoomSpinBox, SIGNAL("valueChanged(int)"), self.showImage)
        editToolbar.addWidget(self.zoomSpinBox)

        self.addActions(self.imageLabel, (editInvertAction, editSwapRedAndBlueAction, editUnMirrorAction, editMirrorHorizAction, editMirrorVertiAction))

        self.resetableActions = ((editInvertAction, False), (editSwapRedAndBlueAction, False), (editUnMirrorAction, True))

        settings = QSettings()
        self.recentFiles = settings.value("RecentFiles") or []
        self.restoreGeometry(settings.value("MainWindow/Geometry", QByteArray()))
        self.restoreState(settings.value("MainWindow/State", QByteArray()))

        self.setWindowTitle("Image Changer")
        self.updateFileMenu()
        QTimer.singleShot(0, self.loadInitialFile)

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

    def closeEvent(self, event):
        if self.okToContinue():
            settings = QSettings()
            settings.setValue("LastFile", self.filename)
            settings.setValue("RecentFiles", self.recentFiles or [])
            settings.setValue("MainWindow/Geometry", self.saveGeometry())
            settings.setValue("MainWindow/State", self.saveState())
        else:
            event.ignore()

    def okToContinue(self):
        if self.dirty:
            reply = QMessageBox.question(self, "Image Changer - Unsaved Changes", "Save unsaved changes?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                return False
            elif reply == QMessageBox.Yes:
                return self.fileSave()
        return True

    def loadInitialFile(self):
        settings = QSettings()
        fname = settings.value("LastFile")
        if fname and QFile.exists(fname):
            self.loadFile(fname)

    def updateStatus(self, message):
        self.statusBar().showMessage(message, 5000)
        self.listWidget.addItem(message)
        if self.filename:
            self.setWindowTitle("Image Changer - {}[*]".format(os.path.basename(self.filename)))
        elif not self.image.isNull():
            self.setWindowTitle("Image Changer - Unnamed[*]")
        else:
            self.setWindowTitle("Image Changer[*]")
        self.setWindowModified(self.dirty)

    def updateFileMenu(self):
        self.fileMenu.clear()
        self.addActions(self.fileMenu, self.fileMenuActions[:-1])
        current = self.filename
        recentFiles = []
        for fname in self.recentFiles:
            if fname != current and QFile.exists(fname):
                recentFiles.append(fname)
        if recentFiles:
            self.fileMenu.addSeparator()
            for i, fname in enumerate(recentFiles):
                action = QAction(QIcon(":/icon.png"), "&{} {}".format(i+1, QFileInfo(fname).fileName()), self)
                action.setData(fname)
                self.connect(action, SIGNAL("triggered()"), self.loadFile)
                self.fileMenu.addAction(action)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileMenuActions[-1])

    def fileNew(self):
        if not self.okToContinue():
            return
        dialog = newimagedlg.NewImageDlg(self)
        if dialog.exec_():
            self.addRecentFile(self.filename)
            self.image = QImage()
            for action, check in self.resetableActions:
                action.setChecked(check)
            self.image = dialog.image()
            self.filename = None
            self.dirty = True
            self.showImage()
            self.sizeLabel.setText("{} x {}".format(self.image.width(), self.image.height()))
            self.updateStatus("Created new image")

    def fileOpen(self):
        if not self.okToContinue():
            return
        dir = (os.path.dirname(self.filename) if self.filename is not None else ".")
        formats = (["*.{}".format(format.data().decode("ascii").lower()) for format in QImageReader.supportedImageFormats()])
        fname = QFileDialog.getOpenFileName(self, "Image Changer - Choose Image", dir, "Image files ({})".format(" ".join(formats)))
        if fname:
            self.loadFile(fname)

    def loadFile(self, fname=None):
        if fname is None:
            action = self.sender()
            if isinstance(action, QAction):
                fname = action.data()
                if not self.okToContinue():
                    return
            else:
                return
        if fname:
            self.filename = None
            image = QImage(fname)
            if image.isNull():
                message = "Failed to read {}".format(fname)
            else:
                self.addRecentFile(fname)
                self.image = QImage()
                for action, check in self.resetableActions:
                    action.setChecked(check)
                self.image = image
                self.filename = fname
                self.showImage()
                self.dirty = False
                self.sizeLabel.setText("{} x {}".format(image.width(), image.height()))
                message = "Loaded {}".format(os.path.basename(fname))
            self.updateStatus(message)

    def addRecentFile(self, fname):
        if fname is None:
            return
        if fname not in self.recentFiles:
            self.recentFiles = [fname] + self.recentFiles[:8]

    def fileSave(self):
        if self.image.isNull():
            return True
        if self.filename is None:
            return self.fileSaveAs()
        else:
            if self.image.save(self.filename, None):
                self.updateStatus("Saved as {}".format(self.filename))
                self.dirty = False
                return True
            else:
                self.updateStatus("Failed to save {}".format(self.filename))
                return False

    def fileSaveAs(self):
        if self.image.isNull():
            return True
        fname = self.filename if self.filename is not None else "."
        formats = (["*.{}".format(format.data().decode("ascii").lower()) for format in QImageWriter.supportedImageFormats()])
        fname = QFileDialog.getSaveFileName(self, "Image Changer - Save Image", fname, "Image files ({})".format(" ".join(formats)))
        if fname:
            if "." not in fname:
                fname += ".png"
            self.addRecentFile(fname)
            self.filename = fname
            return self.fileSave()
        return False

    def filePrint(self):
        if self.image.isNull():
            return
        if self.printer is None:
            self.printer = QPrinter(QPrinter.HighResolution)
            self.printer.setPageSize(QPrinter.Letter)
        form = QPrintDialog(self.printer, self)
        if form.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.drawImage(0, 0, self.image)

    def editInvert(self, on):
        if self.image.isNull():
            return
        self.image.invertPixels()
        self.showImage()
        self.dirty = True
        self.updateStatus("Inverted" if on else "Uninverted")

    def editSwapRedAndBlue(self, on):
        if self.image.isNull():
            return
        self.image = self.image.rgbSwapped()
        self.showImage()
        self.dirty = True
        self.updateStatus(("Swapped Red and Blue" if on else "Unswapped Red and Blue"))

    def editUnMirror(self, on):
        if self.image.isNull():
            return
        if self.mirroredhorizontally:
            self.editMirrorHorizontal(False)
        if self.mirroredvertically:
            self.editMirrorVertical(False)

    def editMirrorHorizontal(self, on):
        if self.image.isNull():
            return
        self.image = self.image.mirrored(True, False)
        self.showImage()
        self.mirroredhorizontally = not self.mirroredhorizontally
        self.dirty = True
        self.updateStatus(("Mirrored Horizontally" if on else "Unmirrored Horizontally"))

    def editMirrorVertical(self, on):
        if self.image.isNull():
            return
        self.image = self.image.mirrored(False, True)
        self.showImage()
        self.mirroredvertically = not self.mirroredvertically
        self.dirty = True
        self.updateStatus(("Mirrored Vertically" if on else "Unmirrored Vertically"))

    def editZoom(self):
        if self.image.isNull():
            return
        percent, ok = QInputDialog.getInteger(self, "Image Changer - Zoom", "Percent:", self.zoomSpinBox.value(), 1, 400)
        if ok:
            self.zoomSpinBox.setValue(percent)

    def editResize(self):
        if self.image.isNull():
            return
        form = resizeDlg.ResizeDlg(self.image.width(), self.image.height(), self)
        if form.exec_():
            width, height = form.result()
        if width == self.image.width() and height == self.image.height():
            return
        self.image = self.image.scaled(width, height)
        self.showImage()
        self.dirty = True
        self.sizeLabel.setText("{} x {}".format(self.image.width(), self.image.height()))
        self.updateStatus("Resize the image")

    def showImage(self, percent=None):
        if self.image.isNull():
            return
        if percent is None:
            percent = self.zoomSpinBox.value()
        factor = percent / 100.0
        width = self.image.width() * factor
        height = self.image.height() * factor
        image = self.image.scaled(width, height, Qt.KeepAspectRatio)
        self.imageLabel.setPixmap(QPixmap.fromImage(image))

    def helpAbout(self):
        QMessageBox.about(self, "About Image Changer",
                """<b>Image Changer</b> v {0}
                <p>Copyright &copy; 2008-10 Qtrac Ltd.
                All rights reserved.
                <p>This application can be used to perform
                simple image manipulations.
                <p>Python {1} - Qt {2} - PyQt {3} on {4}""".format(
                __version__, platform.python_version(),
                QT_VERSION_STR, PYQT_VERSION_STR,
                platform.system()))

    def helpHelp(self):
        form = helpform.HelpForm("index.html", self)
        form.show()

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Pythonfixer")
    app.setOrganizationDomain("Pythonfixer")
    app.setApplicationName("Image Changer")
    app.setWindowIcon(QIcon(":/icon.png"))
    form = MainWindow()
    form.show()
    app.exec_()

main()