from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class NewsItem:
    title: str
    source: str
    url: Optional[str] = None
    published_at: Optional[str] = None
    summary: Optional[str] = None
    sentiment: Optional[str] = None
    relevance: Optional[str] = None

    def to_dict(self):
        return asdict(self)

