"""Abstract base class used for realizing specific ingestors."""
from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel
from typing import List


class IngestorInterface(ABC):
    """Abstract base class for deriving concrete ingestor classes.

    Attribute:
        allowed_extensions: overridden by concrete class. A list of strings
            of the file extension(s) the concreate class can parse.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Determine if concrete class can parse this file type.

        Args:
            path: A string containing a path to the file to parse.

        Returns:
            A boolean set to True if class can parse files of this type.
        """
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract class method defined in realized class used to parse file.

        Args:
            path: A string containing a path to the file to parse.

        Returns:
            A list of QuoteModel objects.

        Raises:
            Exception: An error if class cannot parse this file type.
        """
        pass
