from PIL import Image, ImageDraw, UnidentifiedImageError
import random
import os


class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:

        try:
            im = Image.open(img_path)
        except FileNotFoundError:
            raise FileNotFoundError(
                f'File "{img_path}" was not found'
            ) from None
        except UnidentifiedImageError:
            raise UnidentifiedImageError(f"Unknown image type") from None

        out = im.resize(
            self._scale_image_dimensions(width, im.width, im.height)
        )

        quote = self._format_quote(text, author)

        draw = ImageDraw.Draw(out)

        text_anchor_pos = self._randomly_position_text(out, draw, quote)

        draw.text(text_anchor_pos, quote, fill=(255, 255, 255, 255))

        outfile = os.path.join(
            self.output_dir,
            f'{random.randint(1,10000000)}.png'
        )

        try:
            out.save(outfile)
        except OSError:
            raise OSError(f'There was a problem saving file "{outfile}"')

        return outfile

    def _scale_image_dimensions(self, desired_width: int, image_width: int,
                                image_height: int) -> tuple[int, int]:
        new_width = min(desired_width, 500)
        new_height = int((new_width / image_width) * image_height)
        return new_width, new_height

    def _format_quote(self, body: str, author: str) -> str:
        return f'"{body}" - {author}'

    def _randomly_position_text(self, image: Image, draw: ImageDraw,
                                quote: str) -> tuple[int, int]:
        text_width, text_height = draw.textsize(quote)

        upper_bound_width = max(0, image.width - text_width)
        upper_bound_height = max(0, image.height - text_height)

        text_anchor_pos = (
            random.randint(0, upper_bound_width),
            random.randint(0, upper_bound_height)
        )

        return text_anchor_pos
