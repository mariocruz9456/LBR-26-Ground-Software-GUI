import sys
from PySide6 import QtWidgets
from PySide6 import QApplication

# Mock data just to test if the GUI works
from ground_gui.data.mock_data import mockdata

# Main window of GUI
from ground_gui.ui.main_window import mainwindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Ground GUI")

    source = mockdata(interval = 1000)

    window = mainwindow(datasource = source)

    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()