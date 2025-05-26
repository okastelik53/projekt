from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QPushButton, QLabel

def run_gui():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Konwerter danych")
    window.resize(400, 200)

    label = QLabel("Kliknij przycisk, aby wybrać plik...", window)
    label.move(50, 30)

    def open_file():
        file, _ = QFileDialog.getOpenFileName()
        label.setText(f"Wybrano: {file}")

    button = QPushButton("Wybierz plik", window)
    button.clicked.connect(open_file)
    button.move(50, 80)

    window.show()
    app.exec_()

if __name__ == "__main__":
    run_gui()
