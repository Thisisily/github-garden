import sys
from PyQt5.QtWidgets import QApplication
from gui_main import MainWindow

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()  # Ensure the main window is displayed
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
