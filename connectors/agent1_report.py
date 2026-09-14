from dataclasses import dataclass, field
from typing import Any


@dataclass
class Agent1Report:
    asset: str

    news: list[Any] = field(default_factory=list)
    economic_data: list[Any] = field(default_factory=list)
    central_banks: list[Any] = field(default_factory=list)
    geopolitics: list[Any] = field(default_factory=list)
    upcoming_events: list[Any] = field(default_factory=list)
    contradictions: list[Any] = field(default_factory=list)

    confirmed_information: list[Any] = field(default_factory=list)
    information_to_confirm: list[Any] = field(default_factory=list)

    def to_dict(self):
        return {
            "asset": self.asset,
            "news": self.news,
            "economic_data": self.economic_data,
            "central_banks": self.central_banks,
            "geopolitics": self.geopolitics,
            "upcoming_events": self.upcoming_events,
            "contradictions": self.contradictions,
            "confirmed_information": self.confirmed_information,
            "information_to_confirm": self.information_to_confirm,
        }

