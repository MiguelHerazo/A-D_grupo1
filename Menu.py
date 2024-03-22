import sys
from ProyectoCombinatoria.PrincipioConteo import principio_conteo_aditivo, principio_conteo_multiplicativo
from ProyectoCombinatoria.Combinaciones import combinaciones_con_repeticion, combinaciones_sin_repeticion
from ProyectoCombinatoria.Variaciones import variaciones_con_repeticion, variaciones_sin_repeticion
from ProyectoCombinatoria.Permutaciones import permutacion_con_repeticion, permutacion_sin_repeticion
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import math

class App(QWidget): #0(1)
    def __init__(self): #0(1)
        super().__init__() #0(1)
        self.setWindowTitle("Calculadora de Permutaciones, Combinaciones, Variaciones, Conteo Aditivo y Conteo Multiplicativo") #0(1)
        self.inicializar_interfaz() #0(1)

    def inicializar_interfaz(self): #0(1)
        layout = QVBoxLayout() #0(1)
        self.setStyleSheet("background-color: skyblue") #0(1)

        self.label_desc = QLabel("Introduzca el tiipo de Operacion:") #0(1)
        self.label_desc.setStyleSheet("color: black ")  #0(1)
        layout.addWidget(self.label_desc) #0(1)
        self.entry_desc = QLineEdit() #0(1)
        layout.addWidget(self.entry_desc) #0(1)

        self.label_parametros = QLabel("Parametros:") #0(1)
        self.label_parametros.setStyleSheet("color: black")  #0(1)
        layout.addWidget(self.label_parametros) #0(1)

        self.label_m = QLabel("m:") #0(1)
        self.label_m.setStyleSheet("color: black")  #0(1)
        layout.addWidget(self.label_m) #0(1)
        self.entry_m = QLineEdit() #0(1)
        layout.addWidget(self.entry_m) #0(1)

        self.label_n = QLabel("n:") #0(1)
        self.label_n.setStyleSheet("color: black")  #0(1)
        layout.addWidget(self.label_n) #0(1)
        self.entry_n = QLineEdit() #0(1)
        layout.addWidget(self.entry_n) #0(1)

        
        self.boton_resolver = QPushButton("Resolver") #0(1)
        self.boton_resolver.setStyleSheet("color: red")  #0(1)
        self.boton_resolver.clicked.connect(self.resolver) #0(1)
        layout.addWidget(self.boton_resolver) #0(1)

        self.setLayout(layout) #0(1)

    def resolver(self):  # 0(1)
        descripcion = self.entry_desc.text()  # 0(1)
        m_text = self.entry_m.text()  # 0(1)
        n_text = self.entry_n.text()  # 0(1)

        try:
            m = int(m_text)
            n = int(n_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Los valores de m y n deben ser números enteros.")
            return
        resultado = self.calcular(descripcion, m, n)  # 0(1)

        QMessageBox.information(self, "Resultado", f"Resultado: {resultado}")  # 0(1)

    def calcular(self, descripcion, m, n): #0(1)
        if descripcion.lower() == "combinacion con repeticion": #0(1)
            resultado = self.c_con_repeticion(m, n) #0(1)
        elif descripcion.lower() == "combinacion sin repeticion": #0(1)
            resultado = self.c_sin_repeticion(m, n) #0(1)
        elif descripcion.lower() == "variacion con repeticion": #0(1)
            resultado = self.v_con_repeticion(m, n) #0(1)
        elif descripcion.lower() == "variacion sin repeticion": #0(1)
            resultado = self.v_sin_repeticion(m, n) #0(1)
        elif descripcion.lower() == "permutacion con repeticion": #0(1)
            resultado = self.p_con_repeticion(m, n) #0(1)
        elif descripcion.lower() == "permutacion sin repeticion": #0(1)
            resultado = self.p_sin_repeticion(m, n=1) #0(1)
        elif descripcion.lower() == "principio de conteo aditivo": #0(1)
            resultado = self.conteo_aditivo(m, n) #0(1)
        elif descripcion.lower() == "principio de conteo multiplicativo": #0(1)
            resultado = self.conteo_multiplicativo(m, n) #0(1)

        return resultado #0(1)

    def c_con_repeticion(self, m, n): #0(1)
        if n > m:
            return "El numero n no puede ser mayor que m"
        if n <= 0 or m <=0:
            return "el numero no puede ser negativo o cero"
        if n > 200 or m > 200:
            return "el numero no puede ser mayor a 200"
        else:
            return combinaciones_con_repeticion(m,n) #0(1)

    def c_sin_repeticion(self, m, n): #0(1)
        if n > m:
            return "El numero n no puede ser mayor que m"
        if n <= 0 or m <= 0:
            return "el numero no puede ser negativo o cero"
        if n > 200 or m > 200:
            return "el numero no puede ser mayor a 200"
        return combinaciones_sin_repeticion(m,n) #0(1)

    def v_con_repeticion(self, m, n): #0(1)
        if n > m:
            return "El numero n no puede ser mayor que m"
        if n <= 0 or m <= 0:
            return "el numero no puede ser negativo o cero"
        if n > 200 or m > 200:
            return "el numero no puede ser mayor a 200"
        return variaciones_con_repeticion(m,n)

    def v_sin_repeticion(self, m, n): #0(1)
        if n > m:
            return "El numero n no puede ser mayor que m"
        if n <= 0 or m <= 0:
            return "el numero no puede ser negativo o cero"
        if n > 200 or m > 200:
            return "el numero no puede ser mayor a 200"
        return variaciones_sin_repeticion(m,n) #0(1)

    def p_con_repeticion(self, m, n): #0(1)
        if n > m:
            return "El numero n no puede ser mayor que m"
        if n <= 0 or m <= 0:
            return "el numero no puede ser negativo o cero"
        if n > 200 or m > 200:
            return "el numero no puede ser mayor a 200"
        return permutacion_con_repeticion(m,n) #0(1)

    def p_sin_repeticion(self, m, n): #0(1)
        if m <= 0:
            return "el numero no puede ser negativo o cero"
        if m > 200:
            return "el numero no puede ser mayor a 200"
        return permutacion_sin_repeticion(m), "recuerde que solo se toma m" #0(1)

    def conteo_aditivo(self, m, n): #0(1)
        if n <= 0 or m <= 0:
            return "Ningun numero  puede ser negativo o cero"
        if n > 200 or m > 200:
            return "el numero no puede ser mayor a 200"
        return principio_conteo_aditivo(m,n)

    def conteo_multiplicativo(self, m, n): #0(1)
        if n <= 0 or m <= 0:
            return "Ningun numero  puede ser negativo o cero"
        if n > 200 or m > 200:
            return "el numero no puede ser mayor a 200"
        return principio_conteo_multiplicativo(m,n) #0(1)

if __name__ == '__main__': #0(1)
    app = QApplication(sys.argv) #0(1)
    ventana = App() #0(1)
    ventana.show() #0(1)
    sys.exit(app.exec_()) #0(1)

# Complejidad espacial y temporal = 0(1)
