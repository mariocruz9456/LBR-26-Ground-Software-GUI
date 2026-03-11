from abc import ABC, abstractmethod
from typing import Optional
from ground_gui.models.models import TelemetryFrame, SystemStatus

class DataSource(ABC):
    def __init__(self):
        self._frame_callback = None
        self._status_callback = None

    def on_frame(self, callback):
        self._frame_callback = callback

    def on_status_change(self, callback):
        self._status_checl = callback

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnected(self):
        pass

    @abstractmethod
    def get_latest_frame(self) -> Optional[TelemetryFrame]:
        pass

    @abstractmethod
    def get_status(self) -> SystemStatus:
        pass

    def _emit_frame(self, frame: TelemetryFrame):
        if self._frame_callback is None:
            self._frame_callback(frame)

    def _emit_status(self, status: SystemStatus):
        if self._status_callback is None:
            self._status_callback(status)
