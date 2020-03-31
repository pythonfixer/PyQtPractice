import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import qrc_resources

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

ID = 0
CATEGORY = 1
SHORTDESC = 2
LONGDESC = 3

def createFakeData():
    import random

    print("Dropping tables...")
    query = QSqlQuery()
    query.exec_("DROP TABLE reference")
    QApplication.processEvents()

    print("Creating tables...")
    query.exec_("""CREATE TABLE reference (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                category VARCHAR(30) NOT NULL,
                shortdesc VARCHAR (20) NOT NULL,
                longdesc VARCHAR(80))""")
    QApplication.processEvents()

    print("Populating tables...")
    query.exec_("INSERT INTO reference (category, shortdesc, longdesc) "
                "VALUES ('Actions', 'Wait', 'Wait for Information')")
    query.exec_("INSERT INTO reference (category, shortdesc, longdesc) "
                "VALUES ('Actions', 'Progress', 'Progress to Next Stage')")
    query.exec_("INSERT INTO reference (category, shortdesc, longdesc) "
                "VALUES ('Actions', 'Escalate', 'Send to Supervisor')")
    QApplication.processEvents()


class MainForm(QDialog):

    def __init__(self):
        super().__init__()

        self.model = QSqlTableModel(self)
        self.model.setTable("reference")
        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, "ID")
        self.model.setHeaderData(CATEGORY, Qt.Horizontal, "Category")
        self.model.setHeaderData(SHORTDESC, Qt.Horizontal, "Short Desc.")
        self.model.setHeaderData(LONGDESC, Qt.Horizontal, "Long Desc.")
        self.model.select()

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setSelectionBehavior(QTableView.SelectRows)
        self.view.setColumnHidden(ID, True)
        self.view.resizeColumnsToContents()

        addButton = QPushButton("&Add")
        deleteButton = QPushButton("&Delete")
        sortButton = QPushButton("&Sort")
        closeButton = QPushButton("Close")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(addButton)
        buttonLayout.addWidget(deleteButton)
        buttonLayout.addWidget(sortButton)
        buttonLayout.addWidget(closeButton)
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        self.connect(addButton, SIGNAL("clicked()"), self.addRecord)
        self.connect(deleteButton, SIGNAL("clicked()"), self.deleteRecord)

        sortMenu = QMenu(self)
        sortByIdAction = QAction('ID', sortMenu)
        self.connect(sortByIdAction, SIGNAL("triggered()"), lambda: self.sort(ID))
        sortMenu.addAction(sortByIdAction)

        sortByCategoryAction = QAction('Category', sortMenu)
        self.connect(sortByCategoryAction, SIGNAL("triggered()"), lambda: self.sort(CATEGORY))
        sortMenu.addAction(sortByCategoryAction)

        sortByShortdescAction = QAction('Shortdesc', sortMenu)
        self.connect(sortByShortdescAction, SIGNAL("triggered()"), lambda: self.sort(SHORTDESC))
        sortMenu.addAction(sortByShortdescAction)
        sortButton.setMenu(sortMenu)

        self.connect(closeButton, SIGNAL("clicked()"), self.accept)


        self.setWindowTitle("Reference Data")


    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, CATEGORY)
        self.view.setCurrentIndex(index)
        self.view.edit(index)


    def deleteRecord(self):
        index = self.view.currentIndex()
        if not index.isValid():
            return
        if (QMessageBox.question(self, "Delete Record", "Delete this record?", QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes):
            self.model.removeRow(index.row())
            self.model.submitAll()


    def sort(self, column):
        self.model.setSort(column, Qt.AscendingOrder)
        self.model.select()


def main():
    app = QApplication(sys.argv)

    filename = os.path.join(os.path.dirname(__file__), "reference.db")
    create = not QFile.exists(filename)
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Reference Data",
            "Database Error: {}".format(db.lastError().text()))
        sys.exit(1)

    splash = None
    if create:
        app.setOverrideCursor(QCursor(Qt.WaitCursor))
        splash = QLabel()
        pixmap = QPixmap(":/assetmanagersplash.png")
        splash.setPixmap(pixmap)
        splash.setMask(pixmap.createHeuristicMask())
        splash.setWindowFlags(Qt.SplashScreen)
        rect = app.desktop().availableGeometry()
        splash.move((rect.width() - pixmap.width()) / 2,
                    (rect.height() - pixmap.height()) / 2)
        splash.show()
        app.processEvents()
        createFakeData()

    form = MainForm()
    form.show()
    if create:
        splash.close()
        app.processEvents()
        app.restoreOverrideCursor()
    app.exec_()
    del form
    del db


main()