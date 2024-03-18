import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import math

class AplicacionPrincipiosDeConteoYCombinatoria(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Permutaciones, Combinaciones, Variaciones, Conteo Aditivo y Conteo Multiplicativo")
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        layout = QVBoxLayout()
        self.setStyleSheet("background-color: skyblue") 

        self.label_desc = QLabel("Introduzca el tiipo de Operacion:")
        self.label_desc.setStyleSheet("color: black ") 
        layout.addWidget(self.label_desc)
        self.entry_desc = QLineEdit()
        layout.addWidget(self.entry_desc)

        self.label_parametros = QLabel("Parametros:")
        self.label_parametros.setStyleSheet("color: black")  
        layout.addWidget(self.label_parametros)

        self.label_m = QLabel("m:")
        self.label_m.setStyleSheet("color: black") 
        layout.addWidget(self.label_m)
        self.entry_m = QLineEdit()
        layout.addWidget(self.entry_m)

        self.label_n = QLabel("n:")
        self.label_n.setStyleSheet("color: black")  
        layout.addWidget(self.label_n)
        self.entry_n = QLineEdit()
        layout.addWidget(self.entry_n)

        
        self.boton_resolver = QPushButton("Resolver")
        self.boton_resolver.setStyleSheet("color: red") 
        self.boton_resolver.clicked.connect(self.resolver)
        layout.addWidget(self.boton_resolver)

        self.setLayout(layout)

    def resolver(self):
        descripcion = self.entry_desc.text()
        m = int(self.entry_m.text())
        n = int(self.entry_n.text())

        
        resultado = self.calcular(descripcion, m, n)

        QMessageBox.information(self, "Resultado", f"Resultado: {resultado}")

    def calcular(self, descripcion, m, n):
        if descripcion.lower() == "combinacion con repeticion":
            resultado = self.combinacion_con_repeticion(m, n)
        elif descripcion.lower() == "combinacion sin repeticion":
            resultado = self.combinacion_sin_repeticion(m, n)
        elif descripcion.lower() == "variacion con repeticion":
            resultado = self.variacion_con_repeticion(m, n)
        elif descripcion.lower() == "variacion sin repeticion":
            resultado = self.variacion_sin_repeticion(m, n)
        elif descripcion.lower() == "permutacion con repeticion":
            resultado = self.permutacion_con_repeticion(m, n)
        elif descripcion.lower() == "permutacion sin repeticion":
            resultado = self.permutacion_sin_repeticion(m)
        elif descripcion.lower() == "principio de conteo aditivo":
            resultado = self.principio_conteo_aditivo(m, n)
        elif descripcion.lower() == "principio de conteo multiplicativo":
            resultado = self.principio_conteo_multiplicativo(m, n)

        return resultado

    def combinacion_con_repeticion(self, m, n):
        resultado = math.comb(m + n - 1, n)
        return resultado

    def combinacion_sin_repeticion(self, m, n):
        resultado = math.comb(m, n)
        return resultado

    def variacion_con_repeticion(self, m, n):
        resultado = m ** n
        return resultado

    def variacion_sin_repeticion(self, m, n):
        resultado = math.factorial(m) / math.factorial(m - n)
        return resultado

    def permutacion_con_repeticion(self, m, n):
        factorial_suma_repeticiones = math.factorial(m + n - 1)
        factorial_m = math.factorial(m)
        resultado = factorial_suma_repeticiones // factorial_m
        return resultado

    def permutacion_sin_repeticion(self, m):
        resultado = math.factorial(m)
        return resultado

    def principio_conteo_aditivo(self, m, n):
        return m + n

    def principio_conteo_multiplicativo(self, m, n):
        return m * n

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = AplicacionPrincipiosDeConteoYCombinatoria()
    ventana.show()
    sys.exit(app.exec_())
