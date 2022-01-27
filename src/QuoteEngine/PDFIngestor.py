"""Class to ingest a file of type pdf."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import subprocess
import random
import tempfile
import os


class PDFIngestor(IngestorInterface):
    """Class to ingest a pdf file.

    Attributes:
        allowed_extensions: A list of strings of the file extension(s)
            this class can parse.
    """

    allowed_extensions = ['pdf']

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

        outfile = f'{tempfile.gettempdir()}/{random.randint(1,10000000)}.txt'
        subprocess.run(['pdftotext', '-table', path, outfile])

        fp = open(outfile, 'r')

        for line in fp.readlines():
            line = line.strip('\n').strip('\x0c')
            if len(line) > 0:
                data = line.split('-')
                body, author = data[0].strip('" '), data[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        fp.close()
        os.remove(outfile)

        return quotes
