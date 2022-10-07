# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:28:10 2021

@author: Mr.Pedro
"""
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel,QProgressBar
#from PyQt5 import QtSql
class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.esquerda = 100
        self.topo = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Hello"
        self.btn = QPushButton('click',self)
        self.probar = QProgressBar(self)
        self.probar.resize(300,50)
        self.probar.move(50,100)
        self.btn.move(350,100)
        self.btn.resize(100,50)
        self.btn.setStyleSheet(' background:#3339DE; border:1px solid #3339DE;color:#ccc;border-radius:4px;font-size:13pt;')
        self.btn.clicked.connect(self.hello)
        self.lb = QLabel(self)
        self.lb.move(250,150)
        self.lb.resize(350,200)
        self.lb.setStyleSheet(' color:#ccc; font-size:40pt;')
        self.carregar()
    def carregar(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.setStyleSheet('background:#26A0DE;')
        self.show()
    def hello(self):
       
        valor = 0
        while valor <= 100:
             
            time.sleep(0.1)
            self.probar.setValue(valor)
            if valor == 100:
                self.lb.setText("Olá, Mundo!")
            valor = valor + 1
       


app = QApplication(sys.argv)

j = Janela()

sys.exit(app.exec())