"""Class capable of ingesting multiple file types.

Class is able to ingest multiple file types by delegating to
  multiple individual ingestor classes based on filte type.
"""
from .IngestorInterface import IngestorInterface
from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .QuoteModel import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    """Class able to ingest a multiple file types.

    Attributes:
        ingestors: A list of classes that are capable of ingesting
            particular file types.
    """

    ingestors = [TextIngestor, DocxIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file and return list of QuoteModel objects.

        Args:
            path: A string containing a path to the file to parse.

        Returns:
            A list of QuoteModel objects.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
