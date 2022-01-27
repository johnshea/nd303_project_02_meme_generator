"""Class to ingest a file of type docx."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
from docx import Document


class DocxIngestor(IngestorInterface):
    """Class to ingest a docx file.

    Attributes:
        allowed_extensions: A list of strings of the file extension(s)
            this class can parse.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file and return list of QuoteModel objects.

        Args:
            path: A string containing a path to the file to parse.

        Returns:
            A list of QuoteModel objects.

        Raises:
            Exception: An error if class cannot parse this file type.
        """
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []

        doc = Document(path)

        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            if len(text) > 0:
                data = text.split('-')
                body, author = data[0].strip('" '), data[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
