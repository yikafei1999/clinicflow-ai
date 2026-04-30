from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import List


@dataclass
class CaseRecord:
    client_name: str = ""
    requested_date: str = ""
    service_type: str = ""
    urgency: str = "normal"
    source_materials: List[str] = field(default_factory=list)
    pain_points: List[str] = field(default_factory=list)
    risk_flags: List[str] = field(default_factory=list)
    next_actions: List[str] = field(default_factory=list)
    summary: str = ""

    def to_dict(self) -> dict:
        return asdict(self)
