"""Class to ingest a file of type txt."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TextIngestor(IngestorInterface):
    """Class to ingest a text file.

    Attributes:
        allowed_extensions: A list of strings of the file extension(s)
            this class can parse.
    """

    allowed_extensions = ['txt']

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

        fp = open(path, 'r')

        for line in fp.readlines():
            line = line.strip('\n').strip('\x0c')
            if len(line) > 0:
                data = line.split('-')
                body, author = data[0].strip('" '), data[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        fp.close()

        return quotes
