from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel
from typing import List

class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        extension = path.split('.')[-1]
        if extension not in cls.allowed_extensions:
            raise Exception("cannot ingest exception")

        return True

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
