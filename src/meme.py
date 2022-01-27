import os
import random
import argparse

from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None or author is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)

        if body is None:
            quote.body = quote.body.replace('\ufeff', '')
            quote.body = quote.body.replace('\u2019', "'")
            body = quote.body

        if author is None:
            author = quote.author

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, body, author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a meme')
    parser.add_argument('-p', '--path', help='path to an image file')
    parser.add_argument('-b', '--body', type=str,
                        help='quote body to add to the image')
    parser.add_argument('-a', '--author', type=str,
                        help='quote author to add to the image')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
