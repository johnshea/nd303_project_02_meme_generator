"""Class to store one quote with its author."""


class QuoteModel:
    """Data class to hold the body and the author of a quote.

    Attributes:
        body - A string to store the body of the quote.
        author - A string to store the author of the quote.
    """

    def __init__(self, body, author):
        """Init QuoteModel with the body and the author of a quote."""
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Repr of the QuoteModel object."""
        return f"<QuoteModel author='{self.author}' body='{self.body}'>"
