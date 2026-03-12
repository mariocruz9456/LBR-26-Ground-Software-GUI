"""

Main file which gets everything running

"""

import sys
from PySide6.QtWidgets import QApplication
from ground_gui.data.mockdata import MockDataSource
from ground_gui.ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Ground Station GUI")

    # MockDataSource sends fake telemtry data every 1000 ms (1 second)
    # Replaced later with real data source
    source = MockDataSource(interval_ms = 1000)

    window = MainWindow(datasource = source)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()