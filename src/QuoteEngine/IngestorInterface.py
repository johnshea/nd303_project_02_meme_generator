from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel
from typing import List

class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
