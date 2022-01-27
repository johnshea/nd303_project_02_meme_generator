"""Class to ingest a file of type csv."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas


class CSVIngestor(IngestorInterface):
    """Class to ingest a csv file.

    Attributes:
        allowed_extensions: A list of strings of the file extension(s)
            this class can parse.
    """

    allowed_extensions = ['csv']

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

        df = pandas.read_csv(path, header=0)

        for _, data in df.iterrows():
            body, author = data['body'], data['author']
            new_quote = QuoteModel(body, author)
            quotes.append(new_quote)

        return quotes
