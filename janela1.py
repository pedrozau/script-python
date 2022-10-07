import sys
from PyQt5.QtWidgets import QApplication, QMainWindow , QPushButton , QLabel

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.altura = 600
        self.largura = 800
        self.titulo = "Janela"
        self.btn = QPushButton('Click',self)
        self.lb = QLabel(self)
        self.lb.move(350,100)
        self.btn.move(350,400)
        self.btn.clicked.connect(self.msg)
        
        self.carregar()

    def carregar(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    def msg(self):
        self.lb.setText("Hello Pedro")
    
app = QApplication(sys.argv)

janela = Janela()

sys.exit(app.exec())