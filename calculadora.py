from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana2.ui", self)
        self.botonsuma.toggled.connect(self.suma)
        self.botonresta.toggled.connect(self.resta)
        self.botonproducto.toggled.connect(self.producto)
        self.botondivision.toggled.connect(self.division)

    def suma(self):
        sum = 0
        sum = int(self.int1.text()) + int(self.int2.text())
        self.lab.setText(str(sum))

    def resta(self):
        res = 0
        res = int(self.int1.text()) - int(self.int2.text())
        self.lab.setText(str(res))

    def producto(self):
        product = 0
        product = int(self.int1.text()) * int(self.int2.text())
        self.lab.setText(str(product))
        
    def division(self):
        div = 0
        if self.int2.text() == "0":
            self.lab.setText("No se puede dividir x 0")
        else:
            div = int(self.int1.text()) / int(self.int2.text())
            self.lab.setText(str(div))

app = QApplication ([])
win = MiVentana2()
win.show()
app.exec_()
