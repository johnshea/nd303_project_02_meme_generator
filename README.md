# Meme Generator

This is the second project in Udacity's Intermediate Python Nanodegree program.

This project will create a meme by overlaying a quote with an author's name at a random position over an image.

The user can customize the output by providing an image, a quote, and an author's name. If any of these are omitted, one will be randomly provided.

## Project Setup

Clone the repo to your local machine.
```bash
git clone https://github.com/johnshea/nd303_project_02_meme_generator.git
```
Install the required dependencies.
```bash
pip install -r requirements.txt
```
Create required output directories.
-- Linux/Mac
```bash
mkdir static
mkdir tmp
```

## To Run The Full Project

Run
```bash
python3 meme.py
```

```
usage: meme.py [-h] [-p PATH] [-b BODY] [-a AUTHOR]

Create a meme

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  path to an image file
  -b BODY, --body BODY  quote body to add to the image
  -a AUTHOR, --author AUTHOR
                        quote author to add to the image
```

## Modules

### module MemeGenerator
#### class MemeEngine
Dependencies: `PIL`, `random`, `os`

A class to generate a meme.

Method `make_meme` will generate a meme from optionally provided arguments. This method will return the path of the generated mem.

Example:
```python
>>> from MemeGenerator import MemeEngine
>>> meme = MemeEngine('./output')
>>> meme.make_meme('./_data/photos/dog/xander_3.jpg', 'Go big or go home!', 'Slugger', width=250)
'./output/8943911.png'
>>> 
```

### Module QuoteEngine
#### class IngestorInterface
Dependencies: `abc`, `QuoteModel`, `typing`

An abstract base class upon which concrete ingestor classes are realized.

An ingestor class is concrete subclass which will parse file types based on its file extension.

Concrete classes must implement:
- abstract method `parse`. This method parses the provided file and returns a list of `QuoteModel` objects.
- override class variable `allowed_extensions` which is a list of file extensions types which is can parse. Example: `allowed_extensions = ['txt']`

#### class `Ingestor`
Dependencies: `IngestorInterface`, `TextIngestor`, `DocxIngestor`, `CSVIngestor`, `PDFIngestor`, `QuoteModel`, `typing`

A general class that is capable of ingesting multiple file types by delegating to individual ingestor classes.

A call to method `parse` will returns a list of `QuoteModel` objects.

Example:
```python
>>> from QuoteEngine import Ingestor
>>> print(Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
[<QuoteModel author='Bork' body='To bork or not to bork'>, <QuoteModel author='Stinky' body='He who smelt it...'>]
>>> 
```
#### class `CSVIngestor`
Dependencies: `IngestorInterface`, `QuoteModel`, `typing`, `pandas`

A concrete class to ingest a `csv` file.

A call to method `parse` will return a list of `QuoteModel` objects.

File Format:
```
body,author
Line 1,Author 1
Line 2,Author 2
```
Example:
```python
>>> from QuoteEngine import CSVIngestor
>>> print(CSVIngestor.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
[<QuoteModel author='Skittle' body='Chase the mailman'>, <QuoteModel author='Mr. Paws' body='When in doubt, go shoe-shopping'>]
>>> 
```
#### class `DocxIngestor`
Dependencies: `IngestorInterface`, `QuoteModel`, `typing`, `docx`

A concrete class to ingest a `docx` file.

A call to method `parse` will return a list of `QuoteModel` objects.

Example:
```python
>>> from QuoteEngine import DocxIngestor
>>> quotes = DocxIngestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx')
>>> print(quotes)
[<QuoteModel author='Rex' body='Bark like no one’s listening'>, <QuoteModel author='Chewy' body='RAWRGWAWGGR'>, <QuoteModel author='Peanut' body='Life is like peanut butter: crunchy'>, <QuoteModel author='Tiny' body='Channel your inner husky'>]
>>> 
```

#### class `PDFIngestor`
Dependencies: `IngestorInterface`, `QuoteModel`, `typing`, `subprocess`, `random`, `tempfile`, `os`

A concrete class to ingest a `pdf` file.

A call to method `parse` will return a list of `QuoteModel` objects.

Example:
```python
>>> from QuoteEngine import PDFIngestor
>>> quotes = PDFIngestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf')
>>> print(quotes)
[<QuoteModel author='Fluffles' body='Treat yo self'>, <QuoteModel author='Forrest Pup' body='Life is like a box of treats'>, <QuoteModel author='Bark Twain' body='It's the size of the fight in the dog'>]
>>>
```

#### class `TextIngestor`
Dependencies: `IngestorInterface`, `QuoteModel`, `typing`

A concrete class to ingest a `txt` file.

A call to method `parse` will return a list of `QuoteModel` objects.

File format:
```
"Line 1" - Author 1
"Line 2" - Author 2
```

Example:
```python
>>> from QuoteEngine import TextIngestor
>>> print(TextIngestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
[<QuoteModel author='Bork' body='To bork or not to bork'>, <QuoteModel author='Stinky' body='He who smelt it...'>]
>>>
```

#### class `QuoteModel`
Dependencies: None

A data class to hold a quote which contains a quote body and quote author.

Example:
```python
>>> from QuoteEngine import QuoteModel
>>> quote = QuoteModel("Body of Quote", "Author name")
>>> print(quote)
<QuoteModel author='Author name' body='Body of Quote'>
>>> 
```
