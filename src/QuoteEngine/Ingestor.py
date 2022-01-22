from .IngestorInterface import IngestorInterface
from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .QuoteModel import QuoteModel
from typing import List

class Ingestor(IngestorInterface):
    ingestors = [TextIngestor, DocxIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
