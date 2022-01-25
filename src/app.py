from multiprocessing import AuthenticationError
import random
import os
import requests
from flask import Flask, render_template, abort, request
import requests
import tempfile

from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = None

    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    
    quote = random.choice(quotes)
    quote.body = quote.body.replace('\ufeff','')
    quote.body = quote.body.replace('\u2019',"'")

    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form.get('image_url')

    if image_url != '':
        result = requests.get(image_url)

        img = f'{tempfile.gettempdir()}/{random.randint(1,10000000)}.jpeg'

        with open(img, 'wb') as out:
            out.write(result.content)
    else:
        img = random.choice(imgs)

    body = request.form.get('body')

    if not body:
        quote = random.choice(quotes)
        body = quote.body

    author = request.form.get('author')

    if not author:
        quote = random.choice(quotes)
        author = quote.author

    path = meme.make_meme(img, body, author)

    if image_url != '':
        os.remove(img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
