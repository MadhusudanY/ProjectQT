# Importing the components we need in our program
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

# sys is responsible for processing the command line arguments
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("MapMe Application")
    window.show()

    # Start the event loop
    app.exec()
