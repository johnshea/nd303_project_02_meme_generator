"""Module contains multiple ingestor for a variety of file types.

Exports:
    TextIngestor: Class to ingest a file of type txt.
    DocxIngestor: Class to ingest a file of type docx.
    CSVIngestor: Class to ingest a file of type csv.
    PDFIngestor: Class to ingest a file of type PDF.
    Ingestor: Class that is capable of ingesting multiple file
        types by delegating to individual ingestor classes.
    QuoteModel: Data class to hold a quote which contains a quote body
        and quote author.
"""
from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .Ingestor import Ingestor
from .QuoteModel import QuoteModel
