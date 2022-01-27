from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import subprocess
import random
import tempfile
import os


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
