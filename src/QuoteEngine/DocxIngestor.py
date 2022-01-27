from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
from docx import Document


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
