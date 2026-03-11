"""
This file is used to define data we may use.

dataclasses creates simple data-holding classes without us having to make them.
datatime is sued to record exactly when a packet is received and more.
enum is used to create fixed named options
typing lets vales refereence specific data types or None
"""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import Optional


class ConnectionStatus(Enum):
    Disconnected = auto()
    Connecting = auto()
    Connected = auto()
    Error = auto()

@dataclass
class SDRConfig:
    device: str = "idk"
    sample_rate_hz = 1_000_000
    center_freq_hz = 915_000_000
    gain_db = float = 12.0
    output_path = str = "telemetry.bin"
    verbose = bool = False

    @property
    def sample_rate_mhz(self):
        return self.sample_rate_hz / 1_000_000
    
    @property
    def center_freq_hmz(self):
        return self.center_frez_hz / 1_000_000
    

@dataclass
class TelemetryFrame:
    timestamp: datetime = None

    altitude_m: float = 0.0
    velocity_mps: float = 0.0
    acceleration: float = 0.0

    pitch_deg: float = 0.0
    roll_deg: float = 0.0
    yaw_deg: float = 0.0

    temperature: float = 0.0
    battery: float = 0.0

    signal: float = 0.0
    packet_count: int = 0

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

@dataclass
class SystemStatus:
    connection_state: ConnectionStatus = ConnectionStatus.Disconnected
    sdr_config: Optional[SDRConfig] = None
    last_packet_time: Optional[datetime] = None
    packets_received: int = 0
    packets_lost: int = 0
    uptime_seconds: float = 0.0

    @property
    def is_connected(self):
        return self.connection_state == ConnectionStatus.Connected