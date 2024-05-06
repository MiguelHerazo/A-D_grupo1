import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QLabel, QTextEdit  
import pandas as pd  
import json 
import requests  
from pandas import json_normalize  


class SortingAlgorithms:  # O(1)
    @staticmethod
    def bubble_sort(arr, reverse=False):  # O(n^2)
        n = len(arr)  # O(1)
        for i in range(n - 1):  # O(n^2)
            for j in range(0, n - i - 1):  # O(n)
                if reverse:  # O(1)
                    if arr[j] < arr[j + 1]:  # O(n)
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(n)
                else:  # O(1)
                    if arr[j] > arr[j + 1]:  # O(n)
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(n)
        return arr  # O(1)

    @staticmethod
    def selection_sort(arr, reverse=False):  # O(n^2)
        n = len(arr)  # O(1)
        for i in range(n):  # O(n^2)
            min_idx = i  # O(1)
            for j in range(i+1, n):  # O(n)
                if reverse:  # O(1)
                    if arr[min_idx] < arr[j]:  # O(1)
                        min_idx = j  # O(1)
                else:  # O(1)
                    if arr[min_idx] > arr[j]:  # O(1)
                        min_idx = j  # O(1)
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # O(1)
        return arr  # O(1)

    @staticmethod
    def insertion_sort(arr, reverse=False):  # O(n^2)
        for i in range(1, len(arr)):  # O(n^2)
            key = arr[i]  # O(1)
            j = i - 1  # O(1)
            if reverse:  # O(1)
                while j >= 0 and key > arr[j]:  # O(n)
                    arr[j + 1] = arr[j]  # O(1)
                    j -= 1  # O(1)
            else:  # O(1)
                while j >= 0 and key < arr[j]:  # O(n)
                    arr[j + 1] = arr[j]  # O(1)
                    j -= 1  # O(1)
            arr[j + 1] = key  # O(1)
        return arr  # O(1)

    @staticmethod
    def merge_sort(arr, reverse=False):  # O(n log n)
        if len(arr) <= 1:  # O(1)
            return arr  # O(1)
        mid = len(arr) // 2  # O(1)
        left_half = arr[:mid]  # O(n)
        right_half = arr[mid:]  # O(n)
        left_half = SortingAlgorithms.merge_sort(left_half, reverse)  # O(n)
        right_half = SortingAlgorithms.merge_sort(right_half, reverse)  # O(n)
        return SortingAlgorithms.merge(left_half, right_half, reverse)  # O(n)

    @staticmethod
    def merge(left, right, reverse):  # O(n)
        result = []  # O(1)
        while left and right:  # O(n)
            if (not reverse and left[0] <= right[0]) or (reverse and left[0] >= right[0]):  # O(1)
                result.append(left.pop(0))  # O(1)
            else:  # O(1)
                result.append(right.pop(0))  # O(1)
        while left:  # O(n)
            result.append(left.pop(0))  # O(1)
        while right:  # O(n)
            result.append(right.pop(0))  # O(1)
        return result  # O(1)

    @staticmethod
    def quick_sort(arr, reverse=False):  # O(n log n) 
        if len(arr) <= 1:  # O(1)
            return arr  # O(1)
        pivot = arr[len(arr) // 2]  # O(1)
        left = [x for x in arr if x < pivot]  # O(n)
        middle = [x for x in arr if x == pivot]  # O(n)
        right = [x for x in arr if x > pivot]  # O(n)
        if reverse:  # O(1)
            return SortingAlgorithms.quick_sort(right, reverse) + middle + SortingAlgorithms.quick_sort(left, reverse)  # o(n)
        else:  # O(1)
            return SortingAlgorithms.quick_sort(left, reverse) + middle + SortingAlgorithms.quick_sort(right, reverse)  # o(n)

    @staticmethod
    def counting_sort(arr, columna, reverse=False):  # O(n)
        max_val = max(arr)  # O(n)
        min_val = min(arr)  # O(n)

        factor = 1000  # O(1)

        count = [0] * (int(max_val * factor) - int(min_val * factor) + 1)  # O(n)

        for num in arr:  # O(n)
            index = int(num * factor) - int(min_val * factor)  # O(1)
            count[index] += 1  # O(1)

        sorted_arr = []  # O(1)

        for i in range(len(count)):  # O(n)
            sorted_arr.extend([(i + int(min_val * factor)) / factor] * count[i])  # O(n)

        if reverse:  # O(1)
            sorted_arr.reverse()  # O(n)

        return sorted_arr  # O(1)

    @staticmethod
    def radix_sort(arr, columna):  # O(nk)
        max_val = max(arr, key=lambda x: x[columna])[columna]  # O(1)
        min_val = min(arr, key=lambda x: x[columna])[columna]  # O(1)

        exp = 1  # O(1)
        while max_val // exp > 0:  # O(n)
            SortingAlgorithms.counting_sort_radix(arr, exp, columna, min_val)  # O(n)
            exp *= 10  # O(1)

        return arr  # O(1)

    @staticmethod
    def counting_sort_radix(arr, exp, columna, min_val):  # O(n)
        n = len(arr)  # O(1)
        output = [0] * n  # O(n)
        count = [0] * 10  # O(1)

        for i in range(n):  # O(n)
            index = ((arr[i][columna] - min_val) // exp) % 10  # O(1)
            count[index] += 1  # O(1)

        for i in range(1, 10):  # O(1)
            count[i] += count[i - 1]  # O(1)

        i = n - 1  # O(1)
        while i >= 0:  # O(n)
            index = ((arr[i][columna] - min_val) // exp) % 10  # O(1)
            output[count[index] - 1] = arr[i]  # O(1)
            count[index] -= 1  # O(1)
            i -= 1  # O(1)

        for i in range(n):  # O(n)
            arr[i] = output[i]  # O(1)

    @staticmethod
    def heap_sort(arr, reverse=False):  # O(n log n)
        def heapify(arr, n, i):  # O(log n)
            largest = i  # O(1)
            l = 2 * i + 1  # O(1)
            r = 2 * i + 2  # O(1)
            if l < n and arr[i] < arr[l]:  # O(1)
                largest = l  # O(1)
            if r < n and arr[largest] < arr[r]:  # O(1)
                largest = r  # O(1)
            if largest != i:  # O(1)
                arr[i], arr[largest] = arr[largest], arr[i]  # O(1)
                heapify(arr, n, largest)  # o(log n)

        n = len(arr)  # O(1)
        for i in range(n, -1, -1):  # O(n)
            heapify(arr, n, i)  # 0(log n)
        for i in range(n - 1, 0, -1):  # O(n)
            arr[i], arr[0] = arr[0], arr[i]  # O(1)
            heapify(arr, i, 0)  # o(log n)
        if reverse:  # O(1)
            return arr[::-1]  # O(n)
        else:  # O(1)
            return arr  # O(1)
        
    @staticmethod
    def bucket_sort(arr, reverse=False):# n(lon)
        max_val = max(arr)# O(n)
        min_val = min(arr)# O(n)

        bucket = [[] for _ in range(len(arr))]# O(n)
        for num in arr:# O(n)
            index = int((num - min_val) / (max_val - min_val) * (len(arr) - 1))# O(1)
            bucket[index].append(num)# O(1)

        for i in range(len(arr)):# O(n)
            bucket[i] = SortingAlgorithms.quick_sort(bucket[i], reverse=reverse)# n(logn)

        sorted_arr = []# O(1)
        for b in bucket:# O(n)
            sorted_arr.extend(b)# O(n)

        if reverse:# O(1)
            return sorted_arr[::-1]# O(n)
        else:# O(1)
            return sorted_arr# O(1)


class MainWindow(QMainWindow):# O(1)
    def __init__(self):# O(1)
        super().__init__()# O(1)

        self.setWindowTitle("Sorting Algorithms")# O(1)
        self.setGeometry(100, 100, 400, 300)# O(1)
        self.setStyleSheet("background-color: #B0E0E6;")# O(1)

        self.initUI()# O(1)

    def initUI(self):
        self.label = QLabel("Seleccione un algoritmo de ordenamiento:", self)# O(1)
        self.label.setGeometry(20, 20, 250, 20)# O(1)

        self.combo_algo = QComboBox(self)# O(1)
        self.combo_algo.setGeometry(20, 50, 200, 30)# O(1)
        self.combo_algo.addItems(["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Counting Sort", "Radix Sort", "Heap Sort", "Bucket Sort"])# O(1)

        self.label_order = QLabel("Orden:", self)# O(1)
        self.label_order.setGeometry(20, 90, 100, 20)# O(1)

        self.combo_order = QComboBox(self)# O(1)
        self.combo_order.setGeometry(20, 120, 100, 30)# O(1)
        self.combo_order.addItems(["Ascendente", "Descendente"])# O(1)

        self.label_column = QLabel("Columna:", self)# O(1)
        self.label_column.setGeometry(150, 90, 100, 20) # O(1)

        self.combo_column = QComboBox(self)# O(1)
        self.combo_column.setGeometry(150, 120, 200, 30)# O(1)

        self.btn_sort = QPushButton("Ordenar", self)# O(1)
        self.btn_sort.setGeometry(20, 160, 100, 30)# O(1)
        self.btn_sort.setStyleSheet("background-color: #006400; color: white;")# O(1)
        self.btn_sort.clicked.connect(self.sort_list)# O(1)

        self.label_result = QLabel("Resultado:", self)# O(1)
        self.label_result.setGeometry(20, 200, 100, 20)# O(1)

        self.text_result = QTextEdit(self)# O(1)
        self.text_result.setGeometry(20, 230, 360, 100)# O(1)

    def init_columns(self, columns):# O(n)
        self.combo_column.clear()  # O(n)
        self.combo_column.addItems(columns)  # O(n)

    def sort_list(self):# O(n)
        selected_algo = self.combo_algo.currentText()# O(1)
        order = self.combo_order.currentText()# O(1)
        selected_column_index = self.combo_column.currentIndex() # O(1)
        # Almacenar el nombre de la columna seleccionada antes de ordenar
        selected_column_name = self.combo_column.currentText()# O(1)

        arr = self.get_data_from_api() # O(n)

        if arr:# O(1)
            # Obtener los datos de la columna seleccionada
            column_data = []# O(1)
            non_float_values = []# O(1)  # Listamos para el almacenamiento de los valores no convertibles a flotantes
            for item in arr:# O(n)
                try:# O(1)
                    column_data.append(float(item[selected_column_index]))# O(1)
                except ValueError:# O(1)
                    non_float_values.append(item[selected_column_index]) # O(1)

            # Ordenanamos la columna seleccionada utilizando el algoritmo seleccionado
            if selected_algo == "Bubble Sort":# O(1)
                sorted_column = SortingAlgorithms.bubble_sort(column_data, reverse=(order == "Descendente"))
            elif selected_algo == "Selection Sort":# O(1)
                sorted_column = SortingAlgorithms.selection_sort(column_data, reverse=(order == "Descendente"))
            elif selected_algo == "Insertion Sort":# O(1)
                sorted_column = SortingAlgorithms.insertion_sort(column_data, reverse=(order == "Descendente"))
            elif selected_algo == "Merge Sort":# O(1)
                sorted_column = SortingAlgorithms.merge_sort(column_data, reverse=(order == "Descendente"))
            elif selected_algo == "Quick Sort":# O(1)
                sorted_column = SortingAlgorithms.quick_sort(column_data, reverse=(order == "Descendente"))
            elif selected_algo == "Counting Sort":# O(1)
                sorted_column = SortingAlgorithms.counting_sort(column_data, selected_column_index, reverse=(order == "Descendente"))
            elif selected_algo == "Radix Sort":# O(1)
                sorted_column = SortingAlgorithms.radix_sort(arr, selected_column_index)
            elif selected_algo == "Heap Sort":# O(1)
                sorted_column = SortingAlgorithms.heap_sort(column_data, reverse=(order == "Descendente"))
            elif selected_algo == "Bucket Sort": # O(1)
                sorted_column = SortingAlgorithms.bucket_sort(column_data, reverse=(order == "Descendente"))

            
            sorted_str = [str(item) for item in sorted_column]# O(n)
            sorted_str.extend(non_float_values)# O(n)
            self.text_result.setText(", ".join(sorted_str))# O(n)

            
            index = self.combo_column.findText(selected_column_name) # O(n)
            if index >= 0: # O(1)
                self.combo_column.setCurrentIndex(index) # O(1)

    def get_data_from_api(self): # O(n)
        ruta = "https://www.datos.gov.co/resource/dyy8-9s4r.json" # api a consumi # O(1)
        try:
            datos = requests.get(ruta) # O(1)
            datos = json.loads(datos.text) # O(1)
            datos = json_normalize(datos) # O(1)

            # Obtenemos los nombres de las columnas
            columns = datos.columns.tolist() # O(n)
            self.init_columns(columns) # O(n)

            # Convertirtimos los valores de las columnas a numeros si es que se puede
            for col in datos.columns: # O(n)
                try:
                    datos[col] = pd.to_numeric(datos[col]) # O(1)
                except ValueError: # O(1)
                    pass # O(1)

            
            data_list = [] # O(1)
            for _, row in datos.iterrows(): # O(n)
                data_list.append(row.tolist()) # O(1)

            return data_list # O(1) 
        except Exception as e: # O(1)
            print("Error al obtener datos de la API:", e) # O(1)
            return None # O(1)

if __name__ == "__main__": # O(1)
    app = QApplication(sys.argv) # O(1)
    window = MainWindow() # O(1)
    window.show() # O(1)
    sys.exit(app.exec_()) # O(1)


# big O = mejor caso: 0(1)- peor caso 0(nlogn)
