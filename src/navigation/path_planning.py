"""
Path planning utilities for UAV navigation.

Provides algorithms for computing collision-free paths in 2D/3D environments,
including A*, RRT, and RL-based planners.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple

import numpy as np


@dataclass
class Waypoint:
    """A single waypoint in 3D space."""

    x: float
    y: float
    z: float

    def to_array(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z], dtype=np.float64)


@dataclass
class Path:
    """An ordered sequence of waypoints."""

    waypoints: List[Waypoint] = field(default_factory=list)

    def append(self, waypoint: Waypoint) -> None:
        self.waypoints.append(waypoint)

    def total_length(self) -> float:
        """Compute the total Euclidean length of the path."""
        if len(self.waypoints) < 2:
            return 0.0
        pts = np.array([w.to_array() for w in self.waypoints])
        return float(np.sum(np.linalg.norm(np.diff(pts, axis=0), axis=1)))

    def __len__(self) -> int:
        return len(self.waypoints)
