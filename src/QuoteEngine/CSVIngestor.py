from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []

        df = pandas.read_csv(path, header=0)

        for _, data in df.iterrows():
            body, author = data['body'], data['author']
            new_quote = QuoteModel(body, author)
            quotes.append(new_quote)

        return quotes
