import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class StringListDlg(QDialog):

    def __init__(self, name, stringlist=None, parent=None):
        super().__init__(parent)

        self.stringlist = stringlist
        self.name = name

        self.contentList = QListWidget()
        self.addButton = QPushButton("&Add...")
        self.editButton = QPushButton("&Edit...")
        self.removeButton = QPushButton("&Remove...")
        self.upButton = QPushButton("&Up")
        self.downButton = QPushButton("&Down")
        self.sortButton = QPushButton("&Sort")
        self.closeButton = QPushButton("Close")

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.editButton)
        buttonLayout.addWidget(self.removeButton)
        buttonLayout.addWidget(self.upButton)
        buttonLayout.addWidget(self.downButton)
        buttonLayout.addWidget(self.sortButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.closeButton)
        layout = QHBoxLayout()
        layout.addWidget(self.contentList)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        self.connect(self.addButton, SIGNAL("clicked()"), self.addList)
        self.connect(self.editButton, SIGNAL("clicked()"), self.editList)
        self.connect(self.removeButton, SIGNAL("clicked()"), self.removeList)
        self.connect(self.upButton, SIGNAL("clicked()"), self.upList)
        self.connect(self.downButton, SIGNAL("clicked()"), self.downList)
        self.connect(self.sortButton, SIGNAL("clicked()"), self.contentList.sortItems)
        self.connect(self.closeButton, SIGNAL("clicked()"), self.accept)

        self.setWindowTitle("Edit {} List".format(self.name))
        self.refreshList()

    def refreshList(self):
        self.contentList.clear()
        self.contentList.addItems(self.stringlist)

    def addList(self):
        row = self.contentList.currentRow()
        title = "Add {}".format(self.name)
        string, ok = QInputDialog.getText(self, title, title)
        if ok and string:
            self.contentList.insertItem(row, string)

    def editList(self):
        row = self.contentList.currentRow()
        item = self.contentList.item(row)
        if item is not None:
            title = "Edit {}".format(self.name)
            string, ok = QInputDialog.getText(self, title, title, QLineEdit.Normal, item.text())
            if ok and string:
                item.setText(string)

    def removeList(self):
        row = self.contentList.currentRow()
        item = self.contentList.item(row)
        if item is None:
            return
        reply = QMessageBox.question(self, "Remove {}".format(self.name), "Remove {} {}?".format(self.name, str(item.text())), QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            item = self.contentList.takeItem(row)
            del item

    def upList(self):
        row = self.contentList.currentRow()
        if row >= 1:
            item = self.contentList.takeItem(row)
            self.contentList.insertItem(row - 1, item)
            self.contentList.setCurrentItem(item)

    def downList(self):
        row = self.contentList.currentRow()
        if row < self.contentList.count() - 1:
            item = self.contentList.takeItem(row)
            self.contentList.insertItem(row + 1, item)
            self.contentList.setCurrentItem(item)

    def accept(self):
        self.stringlist = list()
        for row in range(self.contentList.count()):
            self.stringlist.append(self.contentList.item(row).text())
        self.emit(SIGNAL("acceptList(QStringList)"), self.stringlist)
        QDialog.accept(self)

    def reject(self):
        self.accept()

if __name__ == "__main__":
    fruit = ["Banana", "Apple", "Elderberry", "Clementine", "Fig",
             "Guava", "Mango", "Honeydew Melon", "Date", "Watermelon",
             "Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi",
             "Lemon", "Nectarine", "Plum", "Raspberry", "Strawberry",
             "Orange"]

app = QApplication(sys.argv)
form = StringListDlg("Fruit", fruit)
form.show()
app.exec_()
print("\n".join(x for x in form.stringlist))