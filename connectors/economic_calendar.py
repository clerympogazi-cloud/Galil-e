from dataclasses import dataclass
from typing import Optional


@dataclass
class EconomicEvent:
    event: str
    country: str
    date: str
    time: Optional[str] = None
    actual: Optional[str] = None
    forecast: Optional[str] = None
    previous: Optional[str] = None
    importance: Optional[str] = None


def create_event(
    event,
    country,
    date,
    time=None,
    actual=None,
    forecast=None,
    previous=None,
    importance=None
):
    return EconomicEvent(
        event=event,
        country=country,
        date=date,
        time=time,
        actual=actual,
        forecast=forecast,
        previous=previous,
        importance=importance
    )
