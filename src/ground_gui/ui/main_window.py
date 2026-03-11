from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QScrollArea,
    QSplitter,
    QSizePolicy,
)

from ground_gui.data.data import datasource
from ground_gui.models.models import systemstatus, telemtryframe
from ground_gui.ui.widgets.log_panel import logpanel
from ground_gui.ui.widgets.status_bar import statusbar
from ground_gui.ui.widgets.telemetry_cards import telemetrycardspanel
