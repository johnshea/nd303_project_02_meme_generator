from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
