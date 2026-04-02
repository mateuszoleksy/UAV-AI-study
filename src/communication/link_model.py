"""
Communication link model for UAV swarms.

Provides a simple abstraction for modelling wireless links between UAVs
and ground stations, including path-loss estimation.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class LinkParameters:
    """Parameters describing a wireless communication link."""

    frequency_hz: float = 2.4e9    # carrier frequency [Hz]
    tx_power_dbm: float = 20.0     # transmit power [dBm]
    rx_sensitivity_dbm: float = -90.0  # receiver sensitivity [dBm]

    def __post_init__(self) -> None:
        """Validate link parameters."""
        if not math.isfinite(self.frequency_hz) or self.frequency_hz <= 0:
            raise ValueError("frequency_hz must be a finite value greater than 0")
    def free_space_path_loss_db(self, distance_m: float) -> float:
        """Compute free-space path loss (Friis) in dB."""
        if distance_m <= 0:
            return 0.0
        wavelength = 3e8 / self.frequency_hz
        return 20 * math.log10(4 * math.pi * distance_m / wavelength)

    def received_power_dbm(self, distance_m: float) -> float:
        """Estimated received power [dBm] at a given distance."""
        return self.tx_power_dbm - self.free_space_path_loss_db(distance_m)

    def is_link_viable(self, distance_m: float) -> bool:
        """Return True if the link is expected to be above sensitivity threshold."""
        return self.received_power_dbm(distance_m) >= self.rx_sensitivity_dbm
