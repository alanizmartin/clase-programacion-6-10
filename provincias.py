from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("comboprov.ui", self)
        # self.comboBox.currentIndexChanged.connect(self.change)
        self.comboBox.currentTextChanged.connect(self.change)
        self.removeBtn.clicked.connect(self.on_remove)
        self.addBtn.clicked.connect(self.on_add)

    def change(self):
        print(self.comboBox.currentText())
        print(self.comboBox.currentIndex())

    def on_remove(self):
        index = self.comboBox.currentIndex()
        self.comboBox.removeItem(index)

    def on_add(self):
        text = self.addText.text()
        self.comboBox.addItem(text)
        self.addText.setText("")
app = QApplication ([])
win = MiVentana2()
win.show()
app.exec_()